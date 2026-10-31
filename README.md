# BLV Projects website

Static website for [BLV Projects](https://www.blvprojects.com) – open-source 3D printers by Ben Levi
(BLV mgn Cube, BLV Ender 3 Pro, BLV mgn12 mod). Hosted on GitHub Pages.

## Folder layout

| Path | What it is |
|------|------------|
| `src/content/` | The text of every page (one HTML file per page). **Edit these.** |
| `src/assets/` | Images (`img/`), styles (`css/site.css`) and script (`js/site.js`). |
| `site.json` | Site settings: menu, social links, donate link, GitHub user/repo, download files. |
| `pages.json` | Page list: URL path, title and Google description of every page. |
| `build.py` | Builds the finished site into `docs/`. |
| `docs/` | The finished website that GitHub Pages publishes. **Do not edit by hand** – it is overwritten by `build.py`. |
| `tools/` | One-time scripts used to move the site off Wix (kept for reference). |

## Editing the site

1. Edit a page in `src/content/` (or an image in `src/assets/img/`).
2. Run the build (Python 3.8+, no extra packages needed):
   ```
   python build.py
   ```
3. Open `docs/index.html` in a browser to check, then commit and push. GitHub Pages updates within a minute or two.

### Special tags in `src/content/*.html`

```html
<btn href="/blv-mgn-cube-bom">BOM</btn>                 <!-- button-style link -->
<btn href="download:BLV-mgn-Cube-V1.15.zip">Download</btn>  <!-- file from the GitHub release -->
<yt id="FC9tIDhOgD4" title="Video title"></yt>          <!-- YouTube video, loads on click -->
```

Links and images that start with `/` (for example `/about` or `/assets/img/photo.jpg`) are site paths;
`build.py` rewrites them so the site works both on `username.github.io/blvprojects/` and on the custom domain.

Section headings (`<h2>`, `<h3>`) automatically get an id made of their letters and digits
(`Main Electronics` → `#mainelectronics`), so in-page links keep working.

## Downloads

The large project ZIP files are **not** stored in the repository. They are attached to a GitHub
Release with the tag set in `site.json` (`release_tag`, default `files`). The file names must match
the names in the `downloads` section of `site.json`:

- `BLV-mgn-Cube-V1.15.zip`
- `BLV-mgn-Cube-V1.15-Metal-Kit.zip`
- `BLV-Ender-3-Pro-Upgrade.zip`
- `BLV-mgn12-3D-Printer-mod.zip`

## Adding a page

1. Create `src/content/<slug>.html`.
2. Add an entry to `pages.json` (`path`, `title`, `description`).
3. To show it in the menu, add it to `projects` (or `cube_tabs`) in `site.json`.
4. Run `python build.py`.

## Custom domain

When `blvprojects.com` points to GitHub Pages, set it under **Settings → Pages → Custom domain**
(`www.blvprojects.com`). `site.json` → `domain` is used for canonical links, the sitemap and the 404 page.

## License

Project files and content © Ben Levi – free for non-commercial use
(Creative Commons Attribution-NonCommercial-ShareAlike).
