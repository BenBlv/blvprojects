# BLV Projects - archive website

Archive of the BLV open-source 3D printer projects by Ben Levi: **BLV mgn Cube**, **BLV Ender 3 Pro** and **BLV mgn12 mod**.
Live site: <https://www.blvprojects.com> (GitHub Pages, served from the `docs/` folder of `main`).

The projects are no longer updated. Every guide, BOM, image, video, download and blog post from the original Wix site is kept here. The site opens in dark mode by default, with a light mode toggle in the header.

## Layout

| Path | What it is |
|------|------------|
| `content/` | The pages, written in Markdown. **Edit these.** |
| `content/assets/img/` | All images (`posts/` holds the images of the project update posts) |
| `content/*/updates/`, `content/news/` | Project update posts migrated from the old Wix blog |
| `content/files/` | Small files attached to the posts (STL/STEP ZIPs, a video) |
| `content/CNAME` | The custom domain for GitHub Pages |
| `content/stylesheets/extra.css`, `content/javascripts/extra.js` | Theme colors and the click-to-load YouTube player |
| `mkdocs.yml` | Site settings and the menu (`nav:`), plus redirects from the old Wix URLs |
| `hooks.py` | Small build hooks: `!yt` video lines and `download:` links |
| `overrides/main.html` | The "this is an archive" banner |
| `docs/` | The built website that GitHub Pages publishes. Generated - don't edit by hand. |

## Building

Requires Python 3.9+.

```
pip install -r requirements.txt
mkdocs serve      # preview at http://127.0.0.1:8000
mkdocs build      # writes the site into docs/
```

Commit both `content/` and the rebuilt `docs/`.

## Writing shortcuts

```markdown
!yt FC9tIDhOgD4 | Video title           <- YouTube video (loads on click); consecutive lines form a grid
[Download](download:BLV-mgn-Cube-V1.15.zip)   <- file from the GitHub release tagged "files"
```

## Downloads

The project ZIP files are attached to the GitHub Release tagged `files` (not stored in the repository):

- `BLV-mgn-Cube-V1.15.zip`
- `BLV-mgn-Cube-V1.15-Metal-Kit.zip`
- `BLV-Ender-3-Pro-Upgrade.zip`
- `BLV-mgn12-3D-Printer-mod.zip`

## Old URLs

The old Wix page and post addresses (for example `/blv-mgn-cube-bom` or `/post/let-there-be-cob-led-light`) redirect to the new pages, so links on
Thingiverse, Printables, YouTube and forums keep working. The mapping is in `mkdocs.yml` under `redirects`.

## License

Content and project files © Ben Levi - [Creative Commons BY-NC-SA](http://creativecommons.org/licenses/by-nc-sa/3.0/), free for non-commercial use.
