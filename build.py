#!/usr/bin/env python3
"""Build the BLV Projects static site.

Reads page content from src/content/<slug>.html, wraps it in the shared layout
(header, navigation, project header, footer) and writes the finished site to
docs/, which is the folder GitHub Pages publishes.

    python build.py

Only the Python standard library is needed. Run it after every content change,
then commit both src/ and docs/.

Special tags you can use inside src/content/*.html:
    <btn href="...">Label</btn>          a button-style link
    <btn href="download:FILE.zip">..</btn> link to a file in the GitHub release
    <yt id="VIDEO_ID" title="..."></yt>  a YouTube video (loads on click)
    Links and images that start with "/" are site paths, e.g. /about,
    /assets/img/photo.jpg - they are rewritten to work from any folder.
"""
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "docs"

SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
PAGES = json.loads((ROOT / "pages.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def release_url(name):
    return (f"https://github.com/{SITE['github_user']}/{SITE['github_repo']}"
            f"/releases/download/{SITE['release_tag']}/{name}")


def download_size(name):
    for info in SITE["downloads"].values():
        if info["name"] == name:
            return info.get("size", "")
    return ""


def render_components(body):
    # <btn href="...">Label</btn>
    def btn(m):
        href, label = m.group(1), m.group(2)
        cls = "btn"
        extra = ""
        if href.startswith("download:"):
            name = href[len("download:"):]
            href = release_url(name)
            cls += " btn-dl"
            size = download_size(name)
            if size:
                extra = f' title="{html.escape(name)} ({size})"'
        target = ' target="_blank" rel="noopener"' if href.startswith("http") and "btn-dl" not in cls else ""
        return f'<a class="{cls}" href="{href}"{target}{extra}>{label}</a>'
    body = re.sub(r'<btn href="([^"]*)">(.*?)</btn>', btn, body, flags=re.S)

    # <yt id="..." title="..."></yt>
    def yt(m):
        vid = m.group(1)
        title = m.group(2) or "YouTube video"
        return (f'<figure class="yt"><button class="yt-play" data-id="{vid}" '
                f'aria-label="Play: {title}"><img loading="lazy" '
                f'src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt=""></button>'
                f'<figcaption>{title}</figcaption></figure>')
    body = re.sub(r'<yt id="([\w-]{11})"(?: title="([^"]*)")?>\s*</yt>', yt, body)

    # Small images keep their original display width
    def img(m):
        tag = m.group(0)
        w = re.search(r'data-w="(\d+)"', tag)
        tag = re.sub(r'\s*data-w="\d*"', "", tag)
        if w and int(w.group(1)) < 700:
            tag = tag.replace("<img ", f'<img style="max-width:{int(w.group(1))}px" ', 1)
        if "loading=" not in tag:
            tag = tag.replace("<img ", '<img loading="lazy" ', 1)
        return tag
    body = re.sub(r"<img\b[^>]*>", img, body)

    # Give headings an id (e.g. "Main Electronics" -> #mainelectronics) so in-page links work
    used = set(re.findall(r'\bid="([^"]+)"', body))
    def heading_id(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        if "id=" in attrs:
            return m.group(0)
        hid = re.sub(r"[^a-z0-9]", "", re.sub(r"<[^>]+>", "", inner).lower())[:40]
        if not hid or hid in used:
            return m.group(0)
        used.add(hid)
        return f'<{tag}{attrs} id="{hid}">{inner}</{tag}>'
    body = re.sub(r"<(h[1-4])([^>]*)>(.*?)</\1>", heading_id, body, flags=re.S)
    return body


def relativize(page_html, depth):
    """Rewrite root paths (/x) so the site works on any domain or sub-folder."""
    prefix = "../" * depth

    def fix(m):
        attr, path = m.group(1), m.group(2)
        if path.startswith("//"):
            return m.group(0)
        frag = ""
        if "#" in path:
            path, frag = path.split("#", 1)
            frag = "#" + frag
        if path in ("", "/"):
            new = (prefix or "./")
        elif path.startswith("/assets/") or re.search(r"\.\w{2,4}$", path):
            new = prefix + path.lstrip("/")
        else:
            new = prefix + path.strip("/") + "/"
        return f'{attr}="{new}{frag}"'
    return re.sub(r'\b(href|src)="(/[^"]*)"', fix, page_html)


# ---------------------------------------------------------------------------
# Layout pieces
# ---------------------------------------------------------------------------

def header(slug):
    path = PAGES[slug]["path"]
    projects_active = path.startswith("/blv-")

    def cls(active):
        return ' class="active"' if active else ""
    items = "".join(f'<li><a href="{p["path"]}">{html.escape(p["title"])}</a></li>'
                    for p in SITE["projects"])
    return f"""
<header class="site-header">
  <div class="wrap header-inner">
    <a class="logo" href="/" aria-label="BLV Projects home"><img src="/assets/img/blv-logo-6da88bb8.png" alt="BLV" width="46" height="46"></a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="main-nav">
      <ul>
        <li><a href="/"{cls(slug == "home")}>Home</a></li>
        <li class="has-sub"><a href="{SITE['projects'][0]['path']}"{cls(projects_active)}>Projects</a>
          <ul class="sub">{items}</ul></li>
        <li><a href="{SITE['blog_url']}" target="_blank" rel="noopener">Updates</a></li>
        <li><a href="/about"{cls(slug == "about")}>About</a></li>
      </ul>
      <a class="btn btn-donate" href="{SITE['donate_url']}" target="_blank" rel="noopener">Donate</a>
    </nav>
  </div>
</header>"""


def cube_header(slug):
    path = PAGES[slug]["path"]
    active = ' class="active" aria-current="page"'
    tabs = "".join(
        f'<a href="{t["path"]}"{active if t["path"] == path else ""}>{html.escape(t["title"])}</a>'
        for t in SITE["cube_tabs"])
    return f"""
<section class="project-hero">
  <div class="wrap project-hero-inner">
    <div>
      <h1 class="project-title">BLV mgn Cube</h1>
      <div class="project-tag"><span></span><b>3D Printer</b></div>
      <p>Hi, my name is Ben Levi and This is <strong>BLV mgn Cube</strong> - an open-source 3D printer project.
      Building your own good and reliable 3D printer is the main purpose of this project.
      Basically, it's an open front structure CoreXY 3D printer, based on mgn linear rails for maximum accuracy,
      efficiency and high print quality.</p>
    </div>
    <img src="/assets/img/blv-cubg-mgn-trans-min-7ea675f5.png" alt="BLV mgn Cube 3D printer" width="268">
  </div>
</section>
<nav class="tabs" aria-label="BLV mgn Cube sections"><div class="wrap tabs-inner">{tabs}</div></nav>"""


def pager(slug):
    path = PAGES[slug]["path"]
    tabs = SITE["cube_tabs"]
    idx = next((i for i, t in enumerate(tabs) if t["path"] == path), None)
    if idx is None:
        return ""
    prev_link = (f'<a class="prev" href="{tabs[idx - 1]["path"]}"><small>Previous</small>{html.escape(tabs[idx - 1]["title"])}</a>'
                 if idx > 0 else "<span></span>")
    next_link = (f'<a class="next" href="{tabs[idx + 1]["path"]}"><small>Next</small>{html.escape(tabs[idx + 1]["title"])}</a>'
                 if idx + 1 < len(tabs) else "<span></span>")
    return f'<nav class="pager wrap" aria-label="Guide pages">{prev_link}{next_link}</nav>'


def footer():
    icons = "".join(
        f'<a href="{s["url"]}" target="_blank" rel="noopener" aria-label="{s["name"]}">'
        f'<img src="/assets/img/{s["icon"]}-icon.png" alt="" width="28" height="28"></a>'
        for s in SITE["social"])
    return f"""
<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="social">{icons}</div>
    <p>© {date.today().year} Ben Levi · BLV Projects. Free for non-commercial use.</p>
  </div>
</footer>"""


def page(slug, body):
    meta = PAGES[slug]
    path = meta["path"]
    title = meta["title"] if slug == "home" else f'{meta["title"]} | {SITE["site_name"]}'
    canonical = SITE["domain"] + ("" if path == "/" else path)
    desc = html.escape(meta.get("description", ""), quote=True)
    verify = (f'\n<meta name="google-site-verification" content="{SITE["google_site_verification"]}">'
              if slug == "home" and SITE.get("google_site_verification") else "")
    hero = cube_header(slug) if slug.startswith("blv-mgn-cube") else ""
    main_cls = "page-home" if slug == "home" else f"page page-{slug}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['domain']}/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">{verify}
<link rel="icon" type="image/png" href="/assets/img/blv-logo-6da88bb8.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@200;300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
{header(slug)}
{hero}
<main class="{main_cls}">
{body}
{pager(slug) if slug.startswith("blv-mgn-cube") else ""}
</main>
{footer()}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(SRC / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("")

    for slug, meta in PAGES.items():
        src = SRC / "content" / f"{slug}.html"
        body = render_components(src.read_text(encoding="utf-8"))
        depth = 0 if meta["path"] == "/" else 1
        out_dir = OUT if depth == 0 else OUT / meta["path"].strip("/")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(relativize(page(slug, body), depth), encoding="utf-8")
        print(f"built {meta['path']}")

    # 404 page: GitHub Pages serves it for any missing path, so links must be absolute
    home = SITE["domain"] + "/"
    (OUT / "404.html").write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | BLVprojects</title>
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#242424;color:#fff;font-family:Poppins,system-ui,sans-serif;text-align:center}}
h1{{font-family:Anton,Impact,sans-serif;font-size:72px;margin:0;color:#ff0072}}a{{color:#ff0072}}</style></head>
<body><div><h1>404</h1><p>This page doesn't exist.</p><p><a id="home" href="{home}">Go to the home page</a></p></div>
<script>var p=location.pathname.split('/');if(location.hostname.endsWith('github.io')&&p.length>2)document.getElementById('home').href='/'+p[1]+'/';</script>
</body></html>
""", encoding="utf-8")

    urls = "".join(
        f"<url><loc>{SITE['domain']}{'' if m['path'] == '/' else m['path']}</loc></url>"
        for m in PAGES.values())
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    print(f"done -> {OUT}")


if __name__ == "__main__":
    build()
