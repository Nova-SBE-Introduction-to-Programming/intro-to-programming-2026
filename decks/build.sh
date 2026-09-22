#!/usr/bin/env bash
# Build the Class 4 deck.
#   ./build.sh
#
# Every figure is TikZ, drawn from macros in theme/; imported artwork: the Ralph photo and the NVIDIA logo.
# Needs tectonic, the Inter/Inter Display/JetBrains Mono fonts, and pygmentize (Pygments) for the
# diff cards on the git slides.
# LaTeX output goes to out/ (gitignored); the two PDFs are then installed:
#   out/class-4.pdf        -> content/weeks/week-04/class-4.pdf   (published deck)
#   out/class-4-notes.pdf  -> teaching/class-4-notes.pdf          (speaker notes, not published)
set -euo pipefail
cd "$(dirname "$0")"

mkdir -p out
for src in class-4 class-4-notes; do
  echo "→ compiling $src.tex"
  # keep the filter narrow: a broad grep once hid a fatal "LaTeX Error" and shipped a stale PDF
  # a halted run leaves the previous PDF in out/, so remove it first and fail on any error line
  rm -f "out/$src.pdf"
  # -Z shell-escape: the git slides run Pygments (minted) for the diff cards. Needs pygmentize
  # on PATH; without the flag minted aborts the run rather than shipping an unhighlighted PDF.
  tectonic -X compile -Z shell-escape "$src.tex" --outdir out 2>&1 \
    | grep -viE "absolute path|^note:|color stack|Object @(Navigation|page)" | tee out/$src.build.log || true
  if grep -qE "^error:|LaTeX Error|^!" "out/$src.build.log"; then echo "!! $src.tex: compile errors above"; exit 1; fi
  [[ -f "out/$src.pdf" ]] || { echo "!! $src.tex did not produce a PDF"; exit 1; }
done

cp out/class-4.pdf       ../content/weeks/week-04/class-4.pdf
cp out/class-4-notes.pdf ../teaching/class-4-notes.pdf
echo "→ installed:"
ls -la ../content/weeks/week-04/class-4.pdf ../teaching/class-4-notes.pdf
