"""MkDocs hooks for BLV Projects.

Shortcuts available in the Markdown pages:

    !yt VIDEO_ID | Video title
        A YouTube video that only loads when clicked. Consecutive lines become a grid.

    [Download](download:FILE.zip)
        A link to a file attached to the GitHub release (see RELEASE_URL below).
"""
import html
import re

RELEASE_URL = "https://github.com/BenBlv/blvprojects/releases/download/files/"

YT_LINE = re.compile(r"^!yt\s+([\w-]{11})\s*(?:\|\s*(.*))?$")


def _video(vid, title):
    cap = html.escape(title or "", quote=True)
    label = cap or "YouTube video"
    return (
        f'<figure class="yt"><button class="yt-play" data-id="{vid}" aria-label="Play: {label}">'
        f'<img class="no-lightbox" loading="lazy" src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt=""></button>'
        + (f"<figcaption>{cap}</figcaption>" if cap else "") + "</figure>"
    )


def on_page_markdown(markdown, **kwargs):
    out, run = [], []
    indent = [""]

    def flush():
        if not run:
            return
        cls = "videos" if len(run) > 1 else "videos single"
        out.append(indent[0] + f'<div class="{cls}" markdown="0">' + "".join(run) + "</div>")
        out.append("")
        run.clear()

    for line in markdown.split("\n"):
        m = YT_LINE.match(line.strip())
        if m:
            if not run:
                indent[0] = line[: len(line) - len(line.lstrip())]
            run.append(_video(m.group(1), m.group(2)))
            continue
        if run and not line.strip():
            continue
        flush()
        out.append(line)
    flush()
    text = "\n".join(out)
    return re.sub(r"\(download:([^)\s]+)\)", lambda m: f"({RELEASE_URL}{m.group(1)})", text)
