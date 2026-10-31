"""One-time migration step: copy the images each page uses into the repo with
readable names, and point the content at them.

Usage: python prepare_assets.py <export_dir> <content_dir> <repo_dir>

  img:<wix media id>  ->  /assets/img/<readable-name>
  file:<wix file id>  ->  download:<release file name>   (names from site.json)
"""
import json
import re
import shutil
import sys
from pathlib import Path


def readable(alt, mid):
    base = re.sub(r"\.(png|jpe?g|gif|webp|svg)$", "", alt or "", flags=re.I)
    base = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:40]
    short = mid.split("_")[1][:8] if "_" in mid else mid[:8]
    ext = Path(mid).suffix.lower().replace(".jpeg", ".jpg")
    return f"{base + '-' if base else 'img-'}{short}{ext}"


def main():
    export, content, repo = (Path(p) for p in sys.argv[1:4])
    site = json.loads((repo / "site.json").read_text(encoding="utf-8"))
    downloads = site["downloads"]
    src_imgs = export / "assets" / "images_web"
    if not src_imgs.exists():
        src_imgs = export / "assets" / "images"
    dst_imgs = repo / "src" / "assets" / "img"
    dst_imgs.mkdir(parents=True, exist_ok=True)
    out_content = repo / "src" / "content"
    out_content.mkdir(parents=True, exist_ok=True)

    names = {}
    missing = set()

    def img_repl(m):
        tag = m.group(0)
        mid = re.search(r'src="img:([^"]+)"', tag).group(1)
        alt = re.search(r'alt="([^"]*)"', tag)
        if mid not in names:
            name = readable(alt.group(1) if alt else "", mid)
            src = src_imgs / mid
            if src.exists():
                shutil.copyfile(src, dst_imgs / name)
            else:
                missing.add(mid)
            names[mid] = name
        return tag.replace(f'src="img:{mid}"', f'src="/assets/img/{names[mid]}"')

    for f in sorted(content.glob("*.html")):
        html = f.read_text(encoding="utf-8")
        html = re.sub(r'<img\b[^>]*src="img:[^"]+"[^>]*>', img_repl, html)
        html = re.sub(r'file:([0-9a-f]{6}_[0-9a-f]{32}\.\w+)',
                      lambda m: "download:" + downloads[m.group(1)]["name"] if m.group(1) in downloads else m.group(0),
                      html)
        (out_content / f.name).write_text(html, encoding="utf-8")
    print(f"{len(names)} images copied, {len(missing)} missing: {sorted(missing)}")


if __name__ == "__main__":
    main()
