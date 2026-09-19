# Decks

LaTeX (beamer) slides for the course, with diagrams authored in Mermaid.

```
decks/
  class-4.tex                 the deck
  class-4-notes.tex           same deck, notes on a second screen
  theme/beamerthemenovasbe.sty  warm light theme: course palette, Inter + JetBrains Mono
  diagrams/*.mmd              Mermaid sources
  figures/*.pdf               rendered diagrams (committed; regenerate with the script)
  render-diagrams.py          Mermaid → PDF, via headless Chromium
  build.sh                    everything, and installs the results
  out/                        LaTeX output (gitignored)
  vendor/                     mermaid.min.js, fetched on demand (gitignored)
```

## Build

```
./build.sh                 # diagrams + both PDFs, installed into the repo
./build.sh --no-diagrams   # skip Mermaid (nothing in diagrams/ changed)
```

It installs `content/weeks/week-04/class-4.pdf` (the published deck, linked from the Week 4
page) and `teaching/class-4-notes.pdf` (speaker notes, not published).

## What you need

- **Tectonic** — a self-contained LaTeX engine; it downloads the packages it needs on first
  run and caches them. `pacman -S tectonic`, `brew install tectonic`.
- **uv** — runs `render-diagrams.py` with Playwright, and Playwright's Chromium
  (`uv run --with playwright python -m playwright install chromium`; the render script also uses
  `pypdf` and `pillow`, which `uv` fetches for you) for the Mermaid step.
  Not needed if you build with `--no-diagrams`.
- Fonts **Inter** and **JetBrains Mono** installed system-wide.

## Why it is built this way

- **Mermaid renders in Chromium, not rsvg.** Mermaid puts node labels in `<foreignObject>`,
  which `rsvg-convert` silently drops — boxes come out empty. Chromium prints the SVG straight
  to a vector PDF with the labels intact, and uses the same fonts as the slides.
- **The diagram background is the deck background.** Chromium always prints white paper, so the
  page is painted `#FFFCF7`. The slides use the same flat colour, so the seam is invisible.
- **Diagram PDFs are committed.** The deck then rebuilds anywhere Tectonic runs, with no
  Node/Chromium. Only re-run the Mermaid step when a `.mmd` changes.
- **Rebuilt PDFs differ byte-for-byte** even when nothing changed, because Chromium and
  Tectonic stamp a creation date. The rendering is identical; `git checkout` the artifacts
  if a rebuild leaves noise in `git status`.

## The optional Ralph image

The "Meet Ralph" slide draws an image from `figures/ralph.png` if one is there, and lays itself out
without it if not — so the deck builds either way. Drop a still in at roughly 4:3 and rebuild.

Two things to know. A PDF cannot animate a GIF, so use a single frame (`magick ralph.gif[0]
figures/ralph.png` picks the first one). And the obvious source is copyrighted, so choose an image
you are comfortable using in a lecture — that call is not the build script's to make.

## Writing slides

`\hue{NovaTeal}` before a frame sets the kicker colour; `\framesubtitle` is the kicker.

```latex
\hue{NovaAccent}
\begin{frame}{The title.}
\framesubtitle{Standard 2 · The judge}
\begin{tcbitemize}[cardsS, raster columns=2]
  \carditem{eyebrow}{Heading}{Body text.}
  \carditemplain{eyebrow}{Body with no heading.}
\end{tcbitemize}
\end{frame}
\tanote{Speaker note — appears only in the notes build.}
```

Also available: `steps` (numbered chips), `callout`, `\code{}`, `\pill{}`, `\lead{}`,
`\muted{}`, `\diagram`/`\diagramtight` (the tight one has no `\vfill`; use it when the frame
carries other content), and `\sectionslide{W4}{kicker}{Title}{subtitle}`.

Beamer will not reflow to fit: if a frame overruns, the build says
`Overfull \vbox ... too high` and you trim it. Keep the build warning-free.
