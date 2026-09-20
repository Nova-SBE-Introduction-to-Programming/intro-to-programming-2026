#!/usr/bin/env python3
r"""Render every diagrams/*.mmd to figures/<name>.pdf for \includegraphics.

Mermaid runs in headless Chromium (vendor/mermaid.min.js — no network), and Chromium
prints the SVG straight to a vector PDF. That keeps mermaid's HTML labels
(<foreignObject>, which rsvg-convert cannot draw) and uses the same system fonts as
the rest of the deck. Chromium always prints white paper, so the deck background is
baked into the page: the slide uses the same flat colour, so the seam is invisible.

    uv run --with playwright --with pypdf --with pillow python render-diagrams.py
"""
import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
SRC, OUT = HERE / "diagrams", HERE / "figures"
BG, FG, MUTED, LINE, CARD = "#FFFCF7", "#2E3A41", "#6E7D85", "#E6DCCC", "#F4EDE0"
SOFT = "#EDE4D5"   # node outlines: present, but not a drawn box
ORANGE, TEAL, YELLOW, PURPLE = "#D2552C", "#12897A", "#A9750B", "#6B5CA5"
PAD = 6  # pt of breathing room around the artwork
MERMAID_VERSION = "11.17.2"

CONFIG = {
    "startOnLoad": False, "securityLevel": "loose", "theme": "base",
    "fontFamily": "Inter, sans-serif",
    "flowchart": {"useMaxWidth": False, "curve": "basis", "padding": 16,
                  "nodeSpacing": 50, "rankSpacing": 58, "diagramPadding": 4},
    "sequence": {"useMaxWidth": False, "mirrorActors": False, "actorMargin": 110,
                 "boxMargin": 12, "diagramMarginX": 8, "diagramMarginY": 8,
                 "noteFontFamily": "Inter", "messageFontFamily": "Inter", "actorFontFamily": "Inter"},
    "gitGraph": {"useMaxWidth": False, "showBranches": True, "showCommitLabel": True,
                 "rotateCommitLabel": False, "mainBranchName": "main"},
    "themeVariables": {
        "background": "transparent", "fontFamily": "Inter, sans-serif", "fontSize": "18px",
        "primaryColor": CARD, "primaryTextColor": FG, "primaryBorderColor": SOFT,
        "secondaryColor": CARD, "secondaryTextColor": FG, "secondaryBorderColor": SOFT,
        "tertiaryColor": CARD, "tertiaryTextColor": FG, "tertiaryBorderColor": SOFT,
        "lineColor": MUTED, "textColor": FG, "mainBkg": CARD, "nodeBorder": SOFT,
        "clusterBkg": "transparent", "clusterBorder": LINE,
        "edgeLabelBackground": BG, "labelBoxBkgColor": CARD,
        "actorBkg": CARD, "actorBorder": TEAL, "actorTextColor": FG, "actorLineColor": LINE,
        "signalColor": FG, "signalTextColor": FG, "labelTextColor": FG,
        "noteBkgColor": "#F2EADD", "noteTextColor": MUTED, "noteBorderColor": LINE,
        "activationBkgColor": TEAL, "activationBorderColor": TEAL,
        "git0": TEAL, "git1": ORANGE, "git2": PURPLE, "git3": YELLOW,
        "gitBranchLabel0": BG, "gitBranchLabel1": BG, "gitBranchLabel2": BG, "gitBranchLabel3": BG,
        "commitLabelColor": FG, "commitLabelBackground": "transparent", "commitLabelFontSize": "15px",
        "tagLabelColor": BG, "tagLabelBackground": ORANGE, "tagLabelBorder": ORANGE, "tagLabelFontSize": "14px",
    },
}

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
  html,body{margin:0;padding:0;background:%s}
  #wrap{display:inline-block;padding:%dpx}
  #wrap svg{display:block;max-width:none!important;height:auto}
  /* mermaid's HTML labels inherit the page font; force ours and the deck's colours */
  #wrap, #wrap *{font-family:Inter,sans-serif!important}
  #wrap .nodeLabel,#wrap .edgeLabel,#wrap .label{color:%s!important}
  #wrap .edgeLabel p,#wrap .edgeLabel{background:transparent!important}
</style></head><body><div id="wrap"></div></body></html>""" % (BG, PAD, FG)


def main():
    sources = sorted(SRC.glob("*.mmd"))
    if not sources:
        sys.exit("no diagrams in " + str(SRC))
    OUT.mkdir(exist_ok=True)
    lib_path = HERE / "vendor" / "mermaid.min.js"
    if not lib_path.exists():                      # 3.5 MB, so it is fetched, not committed
        import urllib.request
        lib_path.parent.mkdir(exist_ok=True)
        url = f"https://cdn.jsdelivr.net/npm/mermaid@{MERMAID_VERSION}/dist/mermaid.min.js"
        print(f"fetching mermaid {MERMAID_VERSION}")
        urllib.request.urlretrieve(url, lib_path)
    lib = lib_path.read_text(encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 2000, "height": 1400})
        page.set_content(PAGE)
        page.add_script_tag(content=lib)
        page.evaluate("cfg => mermaid.initialize(cfg)", CONFIG)
        for src in sources:
            size = page.evaluate(
                """async ([id, text]) => {
                    const {svg} = await mermaid.render(id, text);
                    const wrap = document.getElementById('wrap');
                    wrap.innerHTML = svg;
                    const el = wrap.querySelector('svg');
                    el.removeAttribute('style');            // drop mermaid's own background
                    // trust mermaid's viewBox: getBBox() would un-crop sequence lifelines
                    const vb = el.viewBox && el.viewBox.baseVal;
                    const box = (vb && vb.width) ? vb : el.getBBox();
                    el.setAttribute('viewBox', `${box.x} ${box.y} ${box.width} ${box.height}`);
                    el.setAttribute('width', box.width); el.setAttribute('height', box.height);
                    await document.fonts.ready;
                    const r = wrap.getBoundingClientRect();
                    return {w: Math.ceil(r.width), h: Math.ceil(r.height)};
                }""",
                [f"d_{src.stem.replace('-', '_')}", src.read_text(encoding="utf-8")],
            )
            pdf = OUT / f"{src.stem}.pdf"
            page.pdf(path=str(pdf), width=f"{size['w']}px", height=f"{size['h']}px",
                     print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
                     prefer_css_page_size=False)
            print(f"{src.name:22} -> {pdf.name:22} {size['w']}x{size['h']} px, {pdf.stat().st_size // 1024} KB")
        browser.close()
    pad_group(OUT, "git-story-")


def pad_group(out, prefix):
    """Give every diagram in a group the same page size, anchored top-left.

    The git story is the same graph drawn four times, one step further each time. Chromium sizes
    each page to its own content, so without this the graph would jump and rescale between slides.
    """
    from pypdf import PdfReader, PdfWriter
    files = sorted(out.glob(f"{prefix}*.pdf"))
    if not files:
        return
    boxes = {f: PdfReader(str(f)).pages[0].mediabox for f in files}
    w = max(float(b.width) for b in boxes.values())
    h = max(float(b.height) for b in boxes.values())
    # The first frame has no branch label, so its graph starts one gutter further left. Align every
    # frame on the main branch badge (TEAL) so the graph holds still and only grows.
    gutter = _main_badge_offsets(files)
    for f in files:
        reader = PdfReader(str(f))
        page = reader.pages[0]
        top, left = float(page.mediabox.top), float(page.mediabox.left)
        shift = gutter.get(f, 0.0)          # window moves left => content sits further right
        page.mediabox.lower_left = (left - shift, top - h)
        page.mediabox.upper_right = (left - shift + w, top)
        writer = PdfWriter()
        writer.add_page(page)
        with open(f, "wb") as fh:
            writer.write(fh)
    print(f"{prefix}*: {len(files)} pages padded to {w:.0f}x{h:.0f} pt, aligned on the main badge")


def _main_badge_offsets(files, dpi=110):
    """How far each page must move right so every main badge lands at the same x, in pt."""
    import subprocess, tempfile
    from PIL import Image
    teal = (18, 137, 122)
    lefts = {}
    with tempfile.TemporaryDirectory() as tmp:
        for f in files:
            stem = f"{tmp}/{f.stem}"
            subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-singlefile", str(f), stem], check=True)
            im = Image.open(stem + ".png").convert("RGB")
            hit = next((x for x in range(im.width)
                        for y in range(0, im.height, 2)
                        if all(abs(a - b) < 18 for a, b in zip(im.getpixel((x, y)), teal))), None)
            if hit is not None:
                lefts[f] = hit
    if not lefts:
        return {}
    target = max(lefts.values())
    return {f: (target - x) * 72.0 / dpi for f, x in lefts.items()}


if __name__ == "__main__":
    main()
