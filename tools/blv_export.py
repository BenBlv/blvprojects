#!/usr/bin/env python3
"""
blv_export.py - Export the BLV Projects Wix site (project pages only) for migration.

Crawls benlevi8.wixsite.com/blvprojects starting from the home page and the known project
pages, follows internal links, skips the blog/posts and Wix system pages, and
saves everything needed to rebuild the site as a static website:

  pages/<slug>/raw.html            server HTML, as fetched
  pages/<slug>/rendered.html       HTML after JavaScript ran (render mode)
  pages/<slug>/desktop.png/.jpg    full-page desktop screenshot (render mode)
  pages/<slug>/mobile.png/.jpg     full-page mobile screenshot (render mode)
  pages/<slug>/embeds/             custom HTML embeds used on the page
  pages/<slug>/page.json           title, text, headings, links, media found
  assets/images/                   original-resolution images
  assets/images_web/               web-sized copies (needs Pillow)
  assets/files/                    downloadable files (zip, pdf, ...)
  assets/videos/                   Wix-hosted videos (unless --skip-videos)
  manifest.json                    everything found + URL -> local file map
  crawl.log                        log of the run
  content.zip                      pages + web images + manifest, to send back

Large files (assets/files, assets/videos, original images) are NOT put in
content.zip - they stay on disk and will be published separately.

Setup (once):
  pip install requests beautifulsoup4 pillow playwright
  playwright install chromium

Run:
  python blv_export.py
  python blv_export.py --out D:\\blvprojects-export --skip-videos

The script can be re-run: files that were already downloaded are skipped.
"""

import argparse
import json
import logging
import os
import re
import sys
import time
import zipfile
from collections import deque
from pathlib import Path
from urllib.parse import parse_qs, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

try:
    from playwright.sync_api import sync_playwright
    HAVE_PLAYWRIGHT = True
except ImportError:
    HAVE_PLAYWRIGHT = False

try:
    from PIL import Image
    HAVE_PIL = True
except ImportError:
    HAVE_PIL = False


# ---------------------------------------------------------------------------
# Site configuration
# ---------------------------------------------------------------------------

# The custom domain (blvprojects.com) is not connected right now, so crawl the
# free Wix address. Links that still point to blvprojects.com count as internal.
BASE = "https://benlevi8.wixsite.com/blvprojects"
SITE_HOSTS = {"www.blvprojects.com", "blvprojects.com"}
WIXSITE_HOST = "benlevi8.wixsite.com"
WIXSITE_PREFIX = "/blvprojects"

START_PATHS = [
    "/",
    "/about",
    "/blv-mgn-cube-3d-printer",
    "/blv-mgn-cube-bom",
    "/blv-mgn-cube-download",
    "/blv-mgn-cube-assembly-guide",
    "/blv-mgn-cube-community",
    "/blv-ender-3-pro",
    "/blv-mgn12-mod-3d-printer",
]

# Paths that are never crawled (blog, posts, Wix system pages, old pages)
EXCLUDE_PREFIXES = (
    "/blog", "/post", "/forum", "/members", "/account", "/profile",
    "/search", "/cart", "/checkout", "/category", "/tag", "/product-page",
    "/_api", "/_partials", "/_files", "/_serverless", "/__",
)
EXCLUDE_CONTAINS = ("-old",)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)

BOILERPLATE_LINES = {
    "top of page", "bottom of page", "use tab to navigate through the menu items.",
    "more", "get started",
}

# ---------------------------------------------------------------------------
# Patterns for assets embedded in Wix HTML / JSON
# ---------------------------------------------------------------------------

# Image ids: 0f2c48_<32 hex>~mv2.jpg (with or without the static.wixstatic.com host)
IMAGE_HOST_RE = re.compile(
    r"static\.wixstatic\.com/media/([A-Za-z0-9_~.\-]+?\.(?:jpe?g|png|gif|webp|svg|avif|bmp))",
    re.I,
)
IMAGE_BARE_RE = re.compile(
    r"\b([0-9a-f]{6}_[0-9a-f]{32}(?:~mv2)?(?:_d_\d+_\d+_s_[\d_]+)?\.(?:jpe?g|png|gif|webp|svg))",
    re.I,
)
# Document uploads: /_files/ugd/<id>.<ext>  or  static.wixstatic.com/ugd/<id>.<ext>
UGD_RE = re.compile(r"ugd/([0-9a-f]{6}_[0-9a-f]{32}\.[A-Za-z0-9]{1,6})", re.I)
# Archives / user files on usrfiles.com / filesusr.com (keep full URL incl. ?dn=)
USRFILES_RE = re.compile(
    r"https?://[A-Za-z0-9\-]+\.(?:usrfiles|filesusr)\.com/(?:archives|ugd)/"
    r"[A-Za-z0-9_]+\.[A-Za-z0-9]{1,6}(?:\?[^\"'\s<>\\]*)?",
    re.I,
)
# Wix-hosted videos
WIX_VIDEO_RE = re.compile(r"video\.wixstatic\.com/video/([A-Za-z0-9_]+)/", re.I)
# YouTube
YOUTUBE_RE = re.compile(
    r"(?:youtube(?:-nocookie)?\.com/(?:embed/|watch\?v=|shorts/)|youtu\.be/)([A-Za-z0-9_\-]{11})"
)
# Custom HTML embeds
HTML_EMBED_RE = re.compile(r"https?://[A-Za-z0-9\-]+\.filesusr\.com/html/[A-Za-z0-9_]+\.html", re.I)
# Plain hrefs in raw HTML / JSON
HREF_RE = re.compile(r"https?://[^\s\"'<>\\]+")


def normalize_blob(text: str) -> str:
    """Undo JSON escaping and URL-encoding that hide URLs inside Wix page data."""
    return (
        text.replace("\\/", "/")
        .replace("\\u002F", "/")
        .replace("\\u002f", "/")
        .replace("%7E", "~")
        .replace("%7e", "~")
        .replace("&amp;", "&")
    )


def safe_name(name: str) -> str:
    name = unquote(name).strip()
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    return name[:180] or "file"


def slug_for(path: str) -> str:
    if path in ("", "/"):
        return "home"
    return path.strip("/").replace("/", "__")


def site_path(url: str):
    """Return the site-relative path for an internal URL, or None if external."""
    try:
        p = urlparse(url)
    except ValueError:
        return None
    host = (p.netloc or "").lower()
    path = unquote(p.path or "/")
    if host in SITE_HOSTS:
        pass
    elif host == WIXSITE_HOST and (path == WIXSITE_PREFIX or path.startswith(WIXSITE_PREFIX + "/")):
        path = path[len(WIXSITE_PREFIX):] or "/"
    else:
        return None
    if len(path) > 1:
        path = path.rstrip("/")
    return path or "/"


def is_crawlable(path: str) -> bool:
    low = path.lower()
    if any(low.startswith(p) for p in EXCLUDE_PREFIXES):  # /blog, /blog-x, /post/..., /_api...
        return False
    if any(c in low for c in EXCLUDE_CONTAINS):
        return False
    last = low.rsplit("/", 1)[-1]
    if "." in last:  # looks like a file, not a page
        return False
    return True


# ---------------------------------------------------------------------------
# Exporter
# ---------------------------------------------------------------------------

class Exporter:
    def __init__(self, out: Path, render: bool, mobile: bool, videos: bool,
                 max_pages: int, delay: float):
        self.out = out
        self.render = render
        self.mobile = mobile
        self.videos = videos
        self.max_pages = max_pages
        self.delay = delay

        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT

        self.pages = {}            # slug -> info
        self.images = {}           # media id -> info
        self.files = {}            # key -> info
        self.wix_videos = {}       # video id -> info
        self.youtube = {}          # yt id -> [slugs]
        self.external_links = {}   # url -> [slugs]
        self.failures = []

        (out / "pages").mkdir(parents=True, exist_ok=True)
        (out / "assets" / "images").mkdir(parents=True, exist_ok=True)
        (out / "assets" / "files").mkdir(parents=True, exist_ok=True)
        if HAVE_PIL:
            (out / "assets" / "images_web").mkdir(parents=True, exist_ok=True)
        if videos:
            (out / "assets" / "videos").mkdir(parents=True, exist_ok=True)

    # -- helpers ----------------------------------------------------------

    def fail(self, what, url, reason):
        logging.warning("FAILED %s %s: %s", what, url, reason)
        self.failures.append({"type": what, "url": url, "reason": str(reason)})

    def rel(self, p: Path) -> str:
        return p.relative_to(self.out).as_posix()

    # -- crawling ---------------------------------------------------------

    def crawl(self):
        queue = deque(START_PATHS)
        seen = set(START_PATHS)

        pw = browser = desk_ctx = mob_ctx = None
        if self.render:
            pw = sync_playwright().start()
            browser = pw.chromium.launch()
            desk_ctx = browser.new_context(viewport={"width": 1440, "height": 900},
                                           user_agent=USER_AGENT)
            if self.mobile:
                mob_ctx = browser.new_context(viewport={"width": 390, "height": 844},
                                              is_mobile=True, has_touch=True,
                                              device_scale_factor=1)
        try:
            while queue and len(self.pages) < self.max_pages:
                path = queue.popleft()
                for link in self.export_page(path, desk_ctx, mob_ctx):
                    if link not in seen and is_crawlable(link):
                        seen.add(link)
                        queue.append(link)
                time.sleep(self.delay)
        finally:
            if browser:
                browser.close()
            if pw:
                pw.stop()

        if queue:
            logging.warning("Stopped at --max-pages=%d; %d pages not visited: %s",
                            self.max_pages, len(queue), list(queue))

    def export_page(self, path, desk_ctx, mob_ctx):
        url = BASE + ("" if path == "/" else path)
        slug = slug_for(path)
        pdir = self.out / "pages" / slug
        logging.info("PAGE %s", url)

        try:
            r = self.session.get(url, timeout=60)
        except requests.RequestException as e:
            self.fail("page", url, e)
            return []
        if r.status_code != 200:
            self.fail("page", url, f"HTTP {r.status_code}")
            return []
        final_path = site_path(r.url) or path
        if final_path != path:
            logging.info("  redirected to %s", r.url)

        pdir.mkdir(parents=True, exist_ok=True)
        raw = r.text
        (pdir / "raw.html").write_text(raw, encoding="utf-8")

        rendered = None
        if desk_ctx is not None:
            rendered = self.render_page(desk_ctx, url, pdir / "desktop.png")
            if rendered:
                (pdir / "rendered.html").write_text(rendered, encoding="utf-8")
            if mob_ctx is not None:
                self.render_page(mob_ctx, url, pdir / "mobile.png")

        html = rendered or raw
        info = self.extract(html, url)
        info["url"] = url
        info["path"] = path
        info["final_url"] = r.url

        blob = normalize_blob(raw + "\n" + (rendered or ""))
        info["image_ids"] = self.collect_images(blob, slug)
        info["file_keys"] = self.collect_files(blob, slug)
        info["wix_videos"] = self.collect_wix_videos(blob, slug)
        info["youtube"] = sorted(set(YOUTUBE_RE.findall(blob)))
        for yt in info["youtube"]:
            self.youtube.setdefault(yt, []).append(slug)
        info["embeds"] = self.save_embeds(blob, pdir)

        # Internal links -> crawl queue; external links -> report
        internal = set()
        candidates = [l["href"] for l in info["links"]] + HREF_RE.findall(blob)
        for href in candidates:
            sp = site_path(href)
            if sp is not None:
                internal.add(sp)
        for l in info["links"]:
            href = l["href"]
            if href.startswith("http") and site_path(href) is None:
                self.external_links.setdefault(href, [])
                if slug not in self.external_links[href]:
                    self.external_links[href].append(slug)
        info["internal_links"] = sorted(internal)

        (pdir / "page.json").write_text(json.dumps(info, indent=2, ensure_ascii=False),
                                        encoding="utf-8")
        self.pages[slug] = {"url": url, "title": info["title"], "dir": self.rel(pdir)}
        return sorted(internal)

    def render_page(self, ctx, url, shot_path):
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="load", timeout=90000)
            page.wait_for_timeout(2500)
            # Scroll down slowly so lazy-loaded images and sections appear
            y, height = 0, page.evaluate("document.body.scrollHeight")
            while y < height and y < 80000:
                y += 600
                page.evaluate(f"window.scrollTo(0, {y})")
                page.wait_for_timeout(200)
                height = page.evaluate("document.body.scrollHeight")
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(1500)
            html = page.content()
            try:
                page.screenshot(path=str(shot_path), full_page=True)
                self.jpeg_copy(shot_path)
            except Exception as e:  # very long pages can fail; not critical
                self.fail("screenshot", url, e)
            return html
        except Exception as e:
            self.fail("render", url, e)
            return None
        finally:
            page.close()

    def jpeg_copy(self, png: Path):
        if not HAVE_PIL or not png.exists():
            return
        try:
            with Image.open(png) as im:
                im = im.convert("RGB")
                if im.width > 1440:
                    im = im.resize((1440, int(im.height * 1440 / im.width)))
                im.save(png.with_suffix(".jpg"), "JPEG", quality=70, optimize=True)
        except Exception as e:
            logging.warning("  could not make JPEG of %s: %s", png.name, e)

    # -- content extraction -----------------------------------------------

    def extract(self, html, url):
        soup = BeautifulSoup(html, "html.parser")

        def meta(attr, name):
            tag = soup.find("meta", attrs={attr: name})
            return tag.get("content", "").strip() if tag else ""

        title = soup.title.get_text(strip=True) if soup.title else ""
        links = []
        for a in soup.find_all("a", href=True):
            href = urljoin(url, a["href"].strip())
            text = " ".join(a.get_text(" ", strip=True).split())
            if not text:
                img = a.find("img")
                text = (img.get("alt") or "").strip() if img else ""
            links.append({"text": text, "href": href})

        images = []
        for img in soup.find_all("img"):
            src = img.get("src") or img.get("data-src") or ""
            m = IMAGE_HOST_RE.search(normalize_blob(src))
            images.append({
                "alt": (img.get("alt") or "").strip(),
                "media_id": m.group(1) if m else None,
                "src": src,
            })

        iframes = [urljoin(url, f.get("src")) for f in soup.find_all("iframe") if f.get("src")]

        for tag in soup(["script", "style", "noscript", "svg", "template"]):
            tag.decompose()
        headings = []
        for h in soup.find_all(re.compile(r"^h[1-6]$")):
            t = " ".join(h.get_text(" ", strip=True).split())
            if t:
                headings.append({"level": int(h.name[1]), "text": t})

        lines, prev = [], None
        for line in soup.get_text("\n").splitlines():
            line = " ".join(line.split())
            if not line or line.lower() in BOILERPLATE_LINES or "built on wix" in line.lower():
                continue
            if line != prev:
                lines.append(line)
            prev = line

        return {
            "title": title,
            "description": meta("name", "description"),
            "og_image": meta("property", "og:image"),
            "headings": headings,
            "text": "\n".join(lines),
            "links": links,
            "images": images,
            "iframes": iframes,
        }

    # -- assets -----------------------------------------------------------

    def collect_images(self, blob, slug):
        ids = set(IMAGE_HOST_RE.findall(blob)) | set(IMAGE_BARE_RE.findall(blob))
        for mid in sorted(ids):
            entry = self.images.setdefault(mid, {
                "url": f"https://static.wixstatic.com/media/{mid}", "pages": []})
            if slug not in entry["pages"]:
                entry["pages"].append(slug)
        return sorted(ids)

    def collect_files(self, blob, slug):
        keys = []
        for fid in set(UGD_RE.findall(blob)):
            key = fid.lower()
            self.files.setdefault(key, {"url": f"{BASE}/_files/ugd/{fid}",
                                        "fallback": f"https://static.wixstatic.com/ugd/{fid}",
                                        "pages": []})
            keys.append(key)
        for full in set(USRFILES_RE.findall(blob)):
            key = urlparse(full).path.rsplit("/", 1)[-1].lower()
            entry = self.files.setdefault(key, {"url": full, "pages": []})
            if "?dn=" in full and "?dn=" not in entry["url"]:
                entry["url"] = full  # prefer the URL that carries the real file name
            keys.append(key)
        for key in keys:
            if slug not in self.files[key]["pages"]:
                self.files[key]["pages"].append(slug)
        return sorted(set(keys))

    def collect_wix_videos(self, blob, slug):
        ids = set(WIX_VIDEO_RE.findall(blob))
        for vid in ids:
            entry = self.wix_videos.setdefault(vid, {"pages": []})
            if slug not in entry["pages"]:
                entry["pages"].append(slug)
        return sorted(ids)

    def save_embeds(self, blob, pdir):
        saved = []
        for i, url in enumerate(sorted(set(HTML_EMBED_RE.findall(blob))), 1):
            try:
                r = self.session.get(url, timeout=60)
                r.raise_for_status()
                (pdir / "embeds").mkdir(exist_ok=True)
                dest = pdir / "embeds" / f"embed_{i}.html"
                dest.write_text(r.text, encoding="utf-8")
                saved.append({"url": url, "local": self.rel(dest)})
            except requests.RequestException as e:
                self.fail("embed", url, e)
        return saved

    def stream_to(self, resp, dest: Path):
        tmp = dest.with_name(dest.name + ".part")
        with open(tmp, "wb") as f:
            for chunk in resp.iter_content(1 << 16):
                f.write(chunk)
        tmp.replace(dest)

    def download_images(self):
        logging.info("Downloading %d images", len(self.images))
        for mid, entry in self.images.items():
            dest = self.out / "assets" / "images" / safe_name(mid)
            if not (dest.exists() and dest.stat().st_size > 0):
                try:
                    r = self.session.get(entry["url"], stream=True, timeout=60)
                    if r.status_code != 200:
                        self.fail("image", entry["url"], f"HTTP {r.status_code}")
                        continue
                    self.stream_to(r, dest)
                except requests.RequestException as e:
                    self.fail("image", entry["url"], e)
                    continue
            entry["local"] = self.rel(dest)
            web = self.web_copy(dest)
            if web:
                entry["web"] = self.rel(web)

    def web_copy(self, src: Path):
        if not HAVE_PIL:
            return None
        dest = self.out / "assets" / "images_web" / src.name
        if dest.exists():
            return dest
        if src.suffix.lower() in (".svg", ".gif"):
            dest.write_bytes(src.read_bytes())
            return dest
        try:
            with Image.open(src) as im:
                if im.width > 1920:
                    im = im.resize((1920, int(im.height * 1920 / im.width)))
                fmt = (im.format or src.suffix.lstrip(".")).upper()
                if src.suffix.lower() in (".jpg", ".jpeg"):
                    im.convert("RGB").save(dest, "JPEG", quality=82, optimize=True)
                elif src.suffix.lower() == ".png":
                    im.save(dest, "PNG", optimize=True)
                else:
                    im.save(dest)
            return dest
        except Exception as e:
            logging.warning("  could not resize %s: %s", src.name, e)
            return None

    def download_files(self):
        logging.info("Downloading %d files", len(self.files))
        used = set()
        for key, entry in self.files.items():
            url = entry["url"]
            qs = parse_qs(urlparse(url).query)
            name = qs.get("dn", [None])[0]
            r, last_err = None, None
            for candidate in [url, entry.get("fallback")]:
                if not candidate:
                    continue
                try:
                    resp = self.session.get(candidate, stream=True, timeout=120)
                except requests.RequestException as e:
                    last_err = e
                    continue
                if resp.status_code == 200:
                    r, entry["url"] = resp, candidate
                    break
                last_err = f"HTTP {resp.status_code}"
                resp.close()
            if r is None:
                self.fail("file", url, last_err)
                continue
            if not name:
                cd = r.headers.get("Content-Disposition", "")
                m = re.search(r"filename\*?=(?:UTF-8'')?\"?([^\";]+)", cd, re.I)
                name = m.group(1) if m else key
            name = safe_name(name)
            if name.lower() in used:
                name = f"{Path(name).stem}__{key}"
            used.add(name.lower())
            dest = self.out / "assets" / "files" / name
            if dest.exists() and dest.stat().st_size > 0:
                r.close()
            else:
                logging.info("  %s", name)
                self.stream_to(r, dest)
            entry["name"] = name
            entry["local"] = self.rel(dest)
            entry["size_mb"] = round(dest.stat().st_size / 1e6, 2)

    def download_videos(self):
        if not self.videos:
            return
        logging.info("Downloading %d Wix videos", len(self.wix_videos))
        for vid, entry in self.wix_videos.items():
            dest = self.out / "assets" / "videos" / f"{vid}.mp4"
            if dest.exists() and dest.stat().st_size > 0:
                entry["local"] = self.rel(dest)
                continue
            for q in ("1080p", "720p", "480p", "360p"):
                url = f"https://video.wixstatic.com/video/{vid}/{q}/mp4/file.mp4"
                try:
                    r = self.session.get(url, stream=True, timeout=120)
                except requests.RequestException:
                    continue
                if r.status_code == 200:
                    self.stream_to(r, dest)
                    entry.update(url=url, quality=q, local=self.rel(dest),
                                 size_mb=round(dest.stat().st_size / 1e6, 2))
                    break
                r.close()
            else:
                self.fail("video", vid, "no downloadable quality found")

    # -- output -----------------------------------------------------------

    def write_manifest(self):
        manifest = {
            "site": BASE,
            "exported_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "render_mode": self.render,
            "pages": self.pages,
            "images": self.images,
            "files": self.files,
            "wix_videos": self.wix_videos,
            "youtube": self.youtube,
            "external_links": self.external_links,
            "failures": self.failures,
        }
        (self.out / "manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    def make_content_zip(self):
        zpath = self.out / "content.zip"
        img_dir = "images_web" if HAVE_PIL else "images"
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
            for name in ("manifest.json", "crawl.log"):
                if (self.out / name).exists():
                    z.write(self.out / name, name)
            for f in (self.out / "pages").rglob("*"):
                if not f.is_file():
                    continue
                # Prefer the small JPEG screenshots over the PNG originals
                if f.suffix == ".png" and f.with_suffix(".jpg").exists():
                    continue
                z.write(f, self.rel(f))
            for f in (self.out / "assets" / img_dir).glob("*"):
                if f.is_file():
                    z.write(f, self.rel(f))
        return zpath


def main():
    default_out = Path("D:/blvprojects-export") if Path("D:/").exists() else Path("blvprojects-export")
    ap = argparse.ArgumentParser(description="Export the BLV Projects Wix site for migration.")
    ap.add_argument("--out", type=Path, default=default_out, help=f"output folder (default: {default_out})")
    ap.add_argument("--no-render", action="store_true", help="skip the browser (no screenshots, faster)")
    ap.add_argument("--no-mobile", action="store_true", help="skip mobile screenshots")
    ap.add_argument("--skip-videos", action="store_true", help="do not download Wix-hosted videos")
    ap.add_argument("--max-pages", type=int, default=80, help="safety limit on pages to crawl")
    ap.add_argument("--delay", type=float, default=0.5, help="seconds to wait between pages")
    args = ap.parse_args()

    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(out / "crawl.log", mode="w", encoding="utf-8"),
                  logging.StreamHandler(sys.stdout)],
    )

    render = not args.no_render
    if render and not HAVE_PLAYWRIGHT:
        logging.warning("Playwright not installed - continuing without screenshots. "
                        "Install with: pip install playwright && playwright install chromium")
        render = False
    if not HAVE_PIL:
        logging.warning("Pillow not installed - no web-sized images. Install with: pip install pillow")

    ex = Exporter(out, render=render, mobile=not args.no_mobile, videos=not args.skip_videos,
                  max_pages=args.max_pages, delay=args.delay)
    ex.crawl()
    ex.download_images()
    ex.download_files()
    ex.download_videos()
    ex.write_manifest()
    zpath = ex.make_content_zip()

    def folder_mb(p: Path):
        return sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) / 1e6 if p.exists() else 0

    print("\n" + "=" * 60)
    print(f"Pages exported : {len(ex.pages)}")
    for slug, p in ex.pages.items():
        print(f"   - {slug:35s} {p['title']}")
    print(f"Images         : {len(ex.images)}")
    print(f"Files          : {len(ex.files)}  ({folder_mb(out / 'assets' / 'files'):.0f} MB)")
    print(f"Wix videos     : {len(ex.wix_videos)}  ({folder_mb(out / 'assets' / 'videos'):.0f} MB)")
    print(f"YouTube videos : {len(ex.youtube)}")
    print(f"Failures       : {len(ex.failures)}  (see manifest.json)")
    print(f"\nSend this file back: {zpath}  ({zpath.stat().st_size / 1e6:.1f} MB)")
    print(f"Keep the rest of {out} - downloads and videos will be published separately.")
    print("=" * 60)


if __name__ == "__main__":
    main()
