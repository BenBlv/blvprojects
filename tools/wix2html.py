"""Convert a Wix rendered page (from blv_export.py) into clean, structured HTML.

Usage: python wix2html.py <export_dir> <out_dir>

Walks #SITE_PAGES in document order and keeps only meaningful structure:
sections, column strips, boxes, rich text, images, buttons, YouTube videos.
Decorative vectors and lines are dropped. Output is a starting point that is
then curated by hand into the final site content.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

from bs4 import BeautifulSoup, NavigableString, Tag

SITE_HOSTS = {"www.blvprojects.com", "blvprojects.com"}
WIX_PREFIX = "/blvprojects"

KEEP_INLINE = {"a", "strong", "b", "em", "i", "u", "br", "span", "sup", "sub"}
KEEP_BLOCK = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li", "blockquote"}

IMG_ID_RE = re.compile(r"static\.wixstatic\.com/media/([A-Za-z0-9_~.\-]+?\.(?:jpe?g|png|gif|webp|svg|avif|bmp))", re.I)
YT_RE = re.compile(r"youtube(?:-nocookie)?\.com/embed/([\w-]{11})")


def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def color_class(rgb):
    r, g, b = rgb
    if r > 200 and g < 90 and b > 60:
        return "c-pink"
    if r < 120 and g > 170 and b > 170:
        return "c-cyan"
    if r > 200 and g < 90 and b < 60:
        return "c-red"
    if g > 150 and r < 120 and b < 120:
        return "c-green"
    if r > 200 and g > 170 and b < 80:
        return "c-yellow"
    return None


class Converter:
    def __init__(self, export_dir: Path):
        self.export = export_dir
        m = json.loads((export_dir / "manifest.json").read_text(encoding="utf-8"))
        self.images = m["images"]
        self.files = m["files"]
        self.theme = {}

    # -- links ----------------------------------------------------------
    def fix_href(self, href):
        if not href:
            return href
        p = urlparse(href)
        host = p.netloc.lower()
        path = unquote(p.path)
        if host == "benlevi8.wixsite.com" and path.startswith(WIX_PREFIX):
            path = path[len(WIX_PREFIX):] or "/"
            host = "www.blvprojects.com"
        if host in SITE_HOSTS:
            m = re.search(r"ugd/([0-9a-f]{6}_[0-9a-f]{32}\.\w+)", path, re.I)
            if m:
                return "file:" + m.group(1).lower()
            if path.startswith(("/blog", "/post")):
                return href.replace("benlevi8.wixsite.com/blvprojects", "www.blvprojects.com")
            path = path.rstrip("/") or "/"
            return path + (("#" + p.fragment) if p.fragment else "")
        m = re.search(r"/(?:archives|ugd)/([0-9a-f]{6}_[0-9a-f]{32}\.\w+)", href, re.I)
        if m and ("usrfiles" in host or "filesusr" in host or "wixstatic" in host):
            return "file:" + m.group(1).lower()
        return href

    # -- text -----------------------------------------------------------
    def clean_inline(self, node):
        out = []
        for ch in node.children:
            if isinstance(ch, NavigableString):
                t = str(ch)
                out.append(t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
                continue
            if not isinstance(ch, Tag):
                continue
            name = ch.name
            inner = self.clean_inline(ch)
            if name in KEEP_BLOCK:
                if name in ("ul", "ol"):
                    out.append(f"<{name}>{inner}</{name}>")
                elif name == "li":
                    out.append(f"<li>{inner.strip()}</li>")
                else:
                    if inner.strip() and inner.strip() != "&nbsp;" and inner.strip() != "​":
                        out.append(f"<{name}>{inner.strip()}</{name}>")
                continue
            if name == "br":
                out.append("<br>")
                continue
            if name == "a":
                if not ch.get("href"):
                    out.append(inner)  # link without a target in Wix - keep the text
                    continue
                href = self.fix_href(ch.get("href"))
                tgt = ' target="_blank" rel="noopener"' if href and href.startswith("http") else ""
                out.append(f'<a href="{href}"{tgt}>{inner}</a>')
                continue
            style = (ch.get("style") or "").replace(" ", "").lower()
            wraps = []
            if name in ("strong", "b") or "font-weight:bold" in style or re.search(r"font-weight:[6-9]00", style):
                wraps.append(("strong", ""))
            if name in ("em", "i") or "font-style:italic" in style:
                wraps.append(("em", ""))
            if name == "u" or "text-decoration:underline" in style:
                wraps.append(("u", ""))
            cm = re.search(r"color:#([0-9a-f]{3,6})", style)
            cls = None
            if cm:
                cls = color_class(hex_to_rgb(cm.group(1)))
            else:
                for c in ch.get("class", []):
                    if c in self.theme:
                        cls = color_class(self.theme[c])
                        break
            if cls:
                wraps.append(("span", f' class="{cls}"'))
            for tag, attr in reversed(wraps):
                inner = f"<{tag}{attr}>{inner}</{tag}>"
            out.append(inner)
        return "".join(out)

    def tidy(self, html):
        html = html.replace("​", "").replace("\xa0", " ")
        for _ in range(3):
            html = re.sub(r"<(strong|em|u)>\s*</\1>", "", html)
            html = re.sub(r"</strong><strong>", "", html)
            html = re.sub(r'</span><span class="(c-\w+)">', lambda m: "", html) if False else html
        html = re.sub(r"<p>\s*(<br>)?\s*</p>", "", html)
        html = re.sub(r"[ \t]+", " ", html)
        return html.strip()

    # -- structure ------------------------------------------------------
    def walk(self, node, depth=0):
        out = []
        for ch in node.children:
            if not isinstance(ch, Tag):
                continue
            classes = ch.get("class", [])
            cls = " ".join(classes)
            ind = "  " * depth
            if "wixui-rich-text" in classes and not any("wixui-rich-text__" in c for c in classes):
                html = self.tidy(self.clean_inline(ch))
                if html:
                    out.append(f"{ind}{html}")
                continue
            if "wixui-video-player" in classes:
                ifr = ch.find("iframe")
                src = ifr.get("src", "") if ifr else ""
                m = YT_RE.search(src)
                if m:
                    title = (ifr.get("title") or "").replace('"', "&quot;")
                    out.append(f'{ind}<yt id="{m.group(1)}" title="{title}"></yt>')
                else:
                    out.append(f"{ind}<!-- video: unknown source -->")
                continue
            if "wixui-image" in classes:
                img = ch.find("img")
                if img:
                    src = (img.get("src") or "").replace("%7E", "~")
                    m = IMG_ID_RE.search(src)
                    if m:
                        mid = m.group(1)
                        alt = (img.get("alt") or "").replace('"', "&quot;")
                        w = img.get("width") or ""
                        tag = f'<img src="img:{mid}" alt="{alt}" data-w="{w}">'
                        a = ch.find("a", href=True)
                        if a:
                            tag = f'<a href="{self.fix_href(a["href"])}">{tag}</a>'
                        out.append(ind + tag)
                continue
            if "wixui-button" in classes:
                label = ch.get_text(" ", strip=True)
                a = ch.find("a", href=True) if ch.name != "a" else ch
                href = self.fix_href(a.get("href")) if a is not None and a.get("href") else ""
                if label:
                    out.append(f'{ind}<btn href="{href}">{label}</btn>')
                elif href:
                    # icon-only button: attach the link to nearby text later
                    out.append(f'{ind}<lnk href="{href}"></lnk>')
                continue
            if any(c in classes for c in ("wixui-vector-image", "wixui-horizontal-line", "wixui-vertical-line")):
                a = ch.find("a", href=True) if ch.name != "a" else ch
                if a is not None and a.get("href"):
                    out.append(f'{ind}<lnk href="{self.fix_href(a["href"])}"></lnk>')
                continue
            if "wixui-section" in classes:
                inner = self.walk(ch, depth + 1)
                if inner:
                    out.append(f'{ind}<section data-id="{ch.get("id","")}">\n' + "\n".join(inner) + f"\n{ind}</section>")
                continue
            if "wixui-column-strip" in classes:
                cols = []
                for col in ch.find_all(class_="wixui-column-strip__column"):
                    if col.find_parent(class_="wixui-column-strip") is not ch:
                        continue
                    inner = self.walk(col, depth + 2)
                    cols.append(f'{ind}  <div class="col">\n' + "\n".join(inner) + f"\n{ind}  </div>")
                if cols:
                    out.append(f'{ind}<div class="cols">\n' + "\n".join(cols) + f"\n{ind}</div>")
                continue
            if "wixui-box" in classes:
                inner = self.walk(ch, depth + 1)
                if inner:
                    out.append(f'{ind}<div class="box">\n' + "\n".join(inner) + f"\n{ind}</div>")
                continue
            if "wixui-repeater" in classes:
                # Community mods list: one card per item (title, author, text, image, link)
                cards = []
                for item in ch.find_all(class_="wixui-repeater__item"):
                    texts = [t for t in item.find_all(class_="wixui-rich-text")
                             if not any("wixui-rich-text__" in c for c in t.get("class", []))]
                    parts = [self.tidy(self.clean_inline(t)) for t in texts]
                    a = item.find("a", href=True)
                    img = item.find("img")
                    href = self.fix_href(a["href"]) if a else ""
                    src = img.get("src", "") if img else ""
                    title = re.sub(r"<[^>]+>", "", parts[0]).strip() if parts else ""
                    rest = parts[1:]
                    author = re.sub(r"<[^>]+>", "", rest[0]).strip() if rest else ""
                    desc = re.sub(r"<a\b[^>]*>(.*?)</a>", r"\1", "".join(rest[1:]))
                    cards.append(
                        f'{ind}  <a class="mod" href="{href}" target="_blank" rel="noopener">'
                        f'<img src="{src}" alt="{title}" loading="lazy"><h4>{title}</h4>'
                        f'<span class="by">{author}</span><div class="desc">{desc}</div></a>')
                out.append(f'{ind}<div class="mods">\n' + "\n".join(cards) + f"\n{ind}</div>")
                continue
            if "wixui-anchor-menu" in classes:
                continue
            cid = ch.get("id") or ""
            if cid.startswith("comp-") and ch.find(attrs={"data-hook": "item-container"}) \
                    and not ch.find(class_="wixui-rich-text"):
                # Wix Pro Gallery: collect every item image in order
                seen, imgs = set(), []
                for item in ch.find_all(attrs={"data-hook": "item-container"}):
                    img = item.find("img")
                    src = (img.get("src") or "") if img else ""
                    if not src:
                        srcset = item.find("source")
                        src = (srcset.get("srcset") or "") if srcset else ""
                    m = IMG_ID_RE.search(src.replace("%7E", "~"))
                    if m and m.group(1) not in seen:
                        seen.add(m.group(1))
                        alt = (img.get("alt") or "").replace('"', "&quot;") if img else ""
                        imgs.append(f'{ind}  <img src="img:{m.group(1)}" alt="{alt}">')
                    elif item.find(attrs={"data-hook": re.compile("video")}):
                        imgs.append(f"{ind}  <!-- gallery video item -->")
                if imgs:
                    out.append(f'{ind}<div class="gallery">\n' + "\n".join(imgs) + f"\n{ind}</div>")
                continue
            if ch.name == "div" and cid.startswith("comp-") and not any(c.startswith("wixui-") for c in classes):
                # Wix "group" component (no wixui class) - keep it as a grouping box
                inner = self.walk(ch, depth + 1)
                if len(inner) >= 2:
                    out.append(f'{ind}<div class="group">\n' + "\n".join(inner) + f"\n{ind}</div>")
                else:
                    out.extend(inner)
                continue
            out.extend(self.walk(ch, depth))
        return out

    def load_theme(self, soup):
        css = " ".join(s.get_text() for s in soup.find_all("style"))
        for m in re.finditer(r"--color_(\d+):\s*(\d+),\s*(\d+),\s*(\d+)", css):
            self.theme[f"color_{m.group(1)}"] = tuple(int(x) for x in m.groups()[1:])

    def convert(self, slug):
        html = (self.export / "pages" / slug / "rendered.html").read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        self.theme = {}
        self.load_theme(soup)
        root = soup.find(id="SITE_PAGES") or soup.body
        return "\n".join(self.walk(root))


def main():
    export, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    conv = Converter(export)
    for pdir in sorted((export / "pages").iterdir()):
        if (pdir / "rendered.html").exists():
            result = conv.convert(pdir.name)
            (out / f"{pdir.name}.html").write_text(result, encoding="utf-8")
            print(f"{pdir.name}: {len(result)} chars")


if __name__ == "__main__":
    main()
