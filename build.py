"""Build the course site: content/ (markdown + files) -> _site/ (static HTML).

Run:  python build.py
Then: python -m http.server -d _site
"""
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
SITE = ROOT / "_site"
TEMPLATE = (ROOT / "template.html").read_text(encoding="utf-8")

NAV = [("Home", "index.html"), ("Setup", "setup.html"), ("Evaluation", "evaluation.html")]


def parse_front_matter(text):
    """Split an optional '---' block of 'key: value' lines from the markdown body."""
    meta = {}
    if text.startswith("---"):
        head, sep, body = text[3:].partition("\n---")
        if sep:
            for line in head.strip().splitlines():
                key, _, value = line.partition(":")
                meta[key.strip()] = value.strip()
            return meta, body.lstrip("\n")
    return meta, text


def render_markdown(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])


def human_size(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def read_page(md_path):
    """Return (meta, body_markdown) for a content .md file, with a default title."""
    meta, body = parse_front_matter(md_path.read_text(encoding="utf-8"))
    if "title" not in meta:
        first = next((l for l in body.splitlines() if l.startswith("#")), md_path.stem)
        meta["title"] = first.lstrip("#").strip()
    return meta, body


def materials_list(week_dir):
    """HTML listing every file in a week folder except index.md."""
    order = {".html": 0, ".md": 1}                    # decks first, then pages, then downloads
    files = [f for f in week_dir.iterdir() if f.name != "index.md" and not f.name.startswith(".")]
    items = []
    for f in sorted(files, key=lambda f: (order.get(f.suffix, 2), f.name)):
        if f.suffix == ".html":
            items.append(f'<li class="deck"><span>{f.stem}</span>'
                         f'<a href="{f.name}">Open presentation →</a></li>')
        elif f.suffix == ".md":
            title = read_page(f)[0]["title"]
            items.append(f'<li class="page"><a href="{f.stem}.html">{title}</a></li>')
        else:
            size = human_size(f.stat().st_size)
            items.append(f'<li class="file"><a href="{f.name}" download>{f.name}</a>'
                         f'<span class="size">{size}</span></li>')
    if not items:
        return ""
    return '<section class="materials"><h2>Materials</h2><ul>' + "".join(items) + "</ul></section>"


def weeks_index():
    """HTML list of every weeks/week-NN/index.md, in folder order."""
    weeks_dir = CONTENT / "weeks"
    items = []
    for index_md in sorted(weeks_dir.glob("week-*/index.md")) if weeks_dir.exists() else []:
        meta = read_page(index_md)[0]
        kind = meta.get("type", "").lower()
        badge = f'<span class="badge {kind}">{kind}</span>' if kind else ""
        date = f'<span class="date">{meta["date"]}</span>' if meta.get("date") else ""
        items.append(f'<li><a href="weeks/{index_md.parent.name}/index.html">{meta["title"]}</a>'
                     f'<span class="meta">{date}{badge}</span></li>')
    if not items:
        return ""
    return '<section class="weeks"><h2>Classes</h2><ul>' + "".join(items) + "</ul></section>"


def write_page(out_path, title, content_html):
    depth = len(out_path.relative_to(SITE).parts) - 1
    prefix = "../" * depth
    nav = "".join(f'<a href="{prefix}{href}">{label}</a>' for label, href in NAV)
    html = (TEMPLATE.replace("{{title}}", title)
                    .replace("{{content}}", content_html)
                    .replace("{{nav}}", nav)
                    .replace("{{root}}", prefix))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


def build():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    shutil.copy(ROOT / "style.css", SITE / "style.css")

    for src in sorted(CONTENT.rglob("*")):
        if src.is_dir() or src.name.startswith("."):
            continue
        rel = src.relative_to(CONTENT)
        if src.suffix != ".md":
            (SITE / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, SITE / rel)          # decks and downloads: byte-for-byte
            continue
        meta, body = read_page(src)
        content_html = render_markdown(body)
        if rel == Path("index.md"):
            content_html += weeks_index()
        elif rel.parts[0] == "weeks" and src.name == "index.md":
            content_html += materials_list(src.parent)
        write_page(SITE / rel.with_suffix(".html"), meta["title"], content_html)

    pages = len(list(SITE.rglob("*.html")))
    print(f"Built {pages} pages into {SITE.relative_to(ROOT)}/")


if __name__ == "__main__":
    build()
