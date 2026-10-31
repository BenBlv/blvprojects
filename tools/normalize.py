"""Turn wix2html output into clean page content using a small component vocabulary.

Usage: python normalize.py <raw_content_dir> <content_dir>

Components produced:
  <div class="banner"><h2>TITLE</h2><p>subtitle</p></div>   pink title band
  <div class="card q|opt"><div class="card-h">..</div><div class="card-b">..</div></div>
  <div class="card-row">cards side by side</div>
  <div class="grid">columns</div>
  <div class="videos">YouTube embeds</div>
  <div class="gallery">images</div>
  <yt id=".." title=".."></yt>, <btn href="..">..</btn>  (resolved by build.py)
"""
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

WIX_BLOG = "https://benlevi8.wixsite.com/blvprojects"

CUBE_SUBPAGES = (
    "/blv-mgn-cube-3d-printer", "/blv-mgn-cube-start", "/blv-mgn-cube-bom",
    "/blv-mgn-cube-download", "/blv-mgn-cube-assembly-guide", "/blv-mgn-cube-wiring",
    "/blv-mgn-cube-calibrations", "/blv-mgn-cube-community", "/blv-mgn-cube-license",
)


def elems(node):
    return [c for c in node.children if isinstance(c, Tag)]


def text_of(node):
    return " ".join(node.get_text(" ", strip=True).split())


def unwrap_all(soup, selector_fn):
    changed = True
    while changed:
        changed = False
        for el in soup.find_all(True):
            if selector_fn(el):
                el.unwrap()
                changed = True
                break


def _between(a, b):
    out, x = [], a.next_sibling
    while x is not None and x is not b:
        out.append(x)
        x = x.next_sibling
    return out


def is_heading_like(el):
    return el.name in ("p", "h1", "h2", "h3", "h4", "h5", "h6") and 0 < len(text_of(el)) <= 70 \
        and not el.find(["img", "btn", "yt", "ul"])


def normalize(html, slug):
    soup = BeautifulSoup(html, "html.parser")

    # 1. Links: blog posts stay on Wix, the old page maps to the current overview
    for a in soup.find_all(["a", "btn"], href=True):
        h = a["href"]
        m = re.match(r"https?://(?:www\.)?blvprojects\.com(/(?:post|blog)\b.*)", h)
        if m:
            a["href"] = WIX_BLOG + m.group(1)
            a["target"] = "_blank"
            a["rel"] = "noopener"
        elif h.startswith("https://www.blvprojects.com") or h.startswith("https://blvprojects.com"):
            a["href"] = re.sub(r"^https://(www\.)?blvprojects\.com", "", h) or "/"
            a.attrs.pop("target", None)
            a.attrs.pop("rel", None)
        if a["href"].startswith("/blv-mgn-cube-3d-printer-old"):
            a["href"] = "/blv-mgn-cube-3d-printer"

    # 1b. Icon-only links (Wix buttons without a label): attach them to nearby text
    def wrap_link(el, href):
        a = soup.new_tag("a", href=href)
        if href.startswith("http"):
            a["target"] = "_blank"
            a["rel"] = "noopener"
        for c in list(el.contents):
            a.append(c.extract())
        el.append(a)

    for lnk in soup.find_all("lnk"):
        if lnk.parent is None:
            continue
        run = [lnk]
        nxt = lnk.find_next_sibling()
        while nxt is not None and nxt.name == "lnk":
            run.append(nxt)
            nxt = nxt.find_next_sibling()
        parent = lnk.parent
        existing = {a.get("href") for a in parent.find_all(["a", "btn"], href=True)}
        prev = []
        p = lnk.find_previous_sibling()
        while p is not None and len(prev) < len(run):
            prev.insert(0, p)
            p = p.find_previous_sibling()
        ok = len(prev) == len(run) and all(
            x.name in ("p", "h1", "h2", "h3", "h4") and not x.find("a") and 0 < len(text_of(x)) <= 120
            for x in prev)
        for i, l in enumerate(run):
            href = l.get("href", "")
            if ok and href and href not in existing and not href.endswith("-old") and href != "/":
                wrap_link(prev[i], href)
            l.decompose()

    # 2. Drop the shared hero + sub-navigation on BLV mgn Cube pages (template adds them)
    sections = soup.find_all("section", recursive=False)
    if slug.startswith("blv-mgn-cube"):
        for i, sec in enumerate(sections[:3]):
            hrefs = [b.get("href") for b in sec.find_all("btn")]
            if sum(h in CUBE_SUBPAGES for h in hrefs) >= 5:
                for s in sections[: i + 1]:
                    s.decompose()
                break

    # 2b. "NEXT" links at the bottom of each guide page (the layout adds a pager)
    for h in soup.find_all(["h1", "h2", "h3", "p"]):
        if text_of(h).upper() in ("NEXT", "NEXT >", "NEXT ›") and h.find("a"):
            h.decompose()

    # 3. Single-column strips and empty columns are just wrappers
    for col in soup.find_all("div", class_="col"):
        if not text_of(col) and not col.find(["img", "yt", "btn"]):
            col.decompose()
    for cols in soup.find_all("div", class_="cols"):
        kids = [c for c in elems(cols) if "col" in c.get("class", [])]
        if not kids:
            cols.decompose()
        elif len(kids) == 1:
            kids[0].unwrap()
            cols.unwrap()
        else:
            cols["class"] = ["grid"]
            for k in kids:
                k["class"] = ["grid-col"]

    # 4. Banner sections: only one or two short lines of text and nothing else
    for sec in soup.find_all("section"):
        kids = [e for e in sec.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])]
        if sec.find(["img", "yt", "btn", "ul"]) or not kids or len(kids) > 2:
            continue
        txt = text_of(sec)
        if len(txt) <= 48:
            parts = [text_of(k) for k in kids]
            if len(parts) == 1 and "|" in parts[0]:
                parts = [x.strip() for x in parts[0].split("|", 1)]
            sub = f"<p>{parts[1]}</p>" if len(parts) > 1 else ""
            new = BeautifulSoup(f'<div class="banner"><h2>{parts[0]}</h2>{sub}</div>', "html.parser")
            sec.clear()
            sec.append(new)

    # 5. Groups -> cards, deepest first
    groups = soup.find_all("div", class_="group")
    for g in reversed(groups):
        kids = elems(g)
        if len(kids) >= 2 and is_heading_like(kids[0]) and len(text_of(g)) > len(text_of(kids[0])) + 40:
            title = kids[0]
            body_html = "".join(str(k) for k in kids[1:])
            kind = "opt" if re.search(r"<(ul|btn)\b", body_html) else "q"
            new = BeautifulSoup(
                f'<div class="card {kind}"><div class="card-h">{title.decode_contents()}</div>'
                f'<div class="card-b">{body_html}</div></div>', "html.parser")
            g.replace_with(new)
        else:
            g.unwrap()
    # nested groups that were inside cards were already unwrapped above

    # 6. Runs of option cards side by side
    for parent in soup.find_all(True):
        run = []
        def flush():
            if len(run) >= 2:
                wrap = soup.new_tag("div", attrs={"class": "card-row"})
                run[0].insert_before(wrap)
                for c in run:
                    wrap.append(c.extract())
            run.clear()
        for ch in list(parent.children):
            if isinstance(ch, NavigableString):
                if ch.strip():
                    flush()
                continue
            if ch.name == "div" and "card" in ch.get("class", []) and "opt" in ch.get("class", []):
                run.append(ch)
            else:
                flush()
        flush()

    # 7. Runs of videos and of images
    def group_runs(tagname, wrap_class, min_len):
        for parent in soup.find_all(True):
            run = []
            def flush():
                if len(run) >= min_len:
                    cls = wrap_class
                    if tagname == "img":
                        widths = []
                        for c in run:
                            im = c if c.name == "img" else c.find("img")
                            w = im.get("data-w", "") if im is not None else ""
                            widths.append(int(w) if w.isdigit() else 999)
                        if max(widths) <= 120:
                            cls = "icons"
                    wrap = soup.new_tag("div", attrs={"class": cls})
                    run[0].insert_before(wrap)
                    for c in run:
                        wrap.append(c.extract())
                run.clear()
            for ch in list(parent.children):
                if isinstance(ch, NavigableString):
                    if ch.strip():
                        flush()
                    continue
                target = ch
                if ch.name == "a" and len(elems(ch)) == 1 and elems(ch)[0].name == "img" and not text_of(ch):
                    target = elems(ch)[0]
                if target.name == tagname and parent.get("class", [""])[0] != wrap_class:
                    run.append(ch)
                else:
                    flush()
            flush()
    group_runs("yt", "videos", 2)
    group_runs("img", "gallery", 3)

    # 8. Long "headings" are really paragraphs (Wix used heading styles for body text)
    for h in soup.find_all(["h1", "h2", "h3"]):
        if len(text_of(h)) > 90 and not h.find_parent(class_="banner"):
            h.name = "p"
        elif not text_of(h) and not h.find("img"):
            h.decompose()

    # 9. Lists that Wix split into one <ul> per item
    for ul in soup.find_all(["ul", "ol"]):
        nxt = ul.find_next_sibling()
        while nxt is not None and nxt.name == ul.name and ul.parent is nxt.parent:
            between = ul.next_sibling
            # only merge when nothing but whitespace separates them
            if any(not isinstance(x, NavigableString) or x.strip() for x in _between(ul, nxt)):
                break
            for li in list(nxt.children):
                ul.append(li.extract())
            nxt.decompose()
            nxt = ul.find_next_sibling()

    # 10. Sections: drop data ids and empty ones
    for sec in soup.find_all("section"):
        sec.attrs = {}
        if not text_of(sec) and not sec.find(["img", "yt", "btn"]):
            sec.decompose()

    out = str(soup)
    out = re.sub(r"\n\s*\n+", "\n", out)
    return out.strip() + "\n"


def main():
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    for f in sorted(src.glob("*.html")):
        result = normalize(f.read_text(encoding="utf-8"), f.stem)
        (dst / f.name).write_text(result, encoding="utf-8")
        print(f"{f.stem}: {len(result)} chars")


if __name__ == "__main__":
    main()
