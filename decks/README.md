# Decks

LaTeX (beamer) slides for the course. Every figure is drawn in TikZ from macros in the theme, except one published chart and one photo.

```
decks/
  class-4.tex                   the deck
  class-4-notes.tex             same deck, notes on a second screen
  theme/beamerthemenovasbe.sty  warm light theme: course palette, Inter + JetBrains Mono,
                                and the figure macros (\gitgraph, \agentstack, \reactring, …)
  figures/                      ralph.jpg and Liu et al. (2024) fig. 1, the only imported artwork
  build.sh                      both PDFs, installed into the repo
  out/                          LaTeX output (gitignored)
```

## Build

```
./build.sh
```

It installs `content/weeks/week-04/class-4.pdf` (the published deck, linked from the Week 4
page) and `teaching/class-4-notes.pdf` (speaker notes, not published).

## What you need

- **Tectonic** — a self-contained LaTeX engine; it downloads the packages it needs on first
  run and caches them. `pacman -S tectonic`, `brew install tectonic`.
- Fonts **Inter** and **JetBrains Mono** installed system-wide.

## Why it is built this way

- **Figures are macros, not files.** Three of them are "builds": the same canvas shown at
  successive stages (`\gitgraph{1..5}`, `\agentstack{1..4}`) or the same ring with different
  words (`\reactring`). Because nothing moves between slides, the eye only registers what was
  added. Mermaid was tried first and dropped: it sized every diagram to its own content, so a
  five-stage story jumped and rescaled, and its fonts and line weights never matched the cards.
- **Icons are drawn** (`\icmodel`, `\icperson`, `\iclaptop`, `\icgear`): no icon font is
  guaranteed on the presenting machine.
- **Rebuilt PDFs differ byte-for-byte** even when nothing changed, because Tectonic stamps a
  creation date. The rendering is identical; `git checkout` the artifacts if a rebuild leaves
  noise in `git status`.

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

Also available: `steps` (numbered chips), `callout`, `\code{}`, `\codeline{}` (a chip big enough
to carry a slide), `\pill{}`, `\muted{}`, `\roundedpic`, the `chatsaid`/`chatthinks` transcript
environments, `\contextbar`, and `\sectionslide{W4}{kicker}{Title}{subtitle}`.

Beamer will not reflow to fit: if a frame overruns, the build says
`Overfull \vbox ... too high` and you trim it. Keep the build warning-free, and look at the
rendered pages — a clean log says nothing about whether a label collides.
