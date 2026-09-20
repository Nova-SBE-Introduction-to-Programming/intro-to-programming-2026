#!/usr/bin/env bash
# Build the Class 4 deck.
#   ./build.sh
#
# Every figure is TikZ, drawn from macros in theme/; the only imported artwork is Liu et al. (2024) fig. 1.
# LaTeX output goes to out/ (gitignored); the two PDFs are then installed:
#   out/class-4.pdf        -> content/weeks/week-04/class-4.pdf   (published deck)
#   out/class-4-notes.pdf  -> teaching/class-4-notes.pdf          (speaker notes, not published)
set -euo pipefail
cd "$(dirname "$0")"

mkdir -p out
for src in class-4 class-4-notes; do
  echo "→ compiling $src.tex"
  # keep the filter narrow: a broad grep once hid a fatal "LaTeX Error" and shipped a stale PDF
  tectonic -X compile "$src.tex" --outdir out 2>&1 \
    | grep -viE "absolute path|^note:|color stack|Object @(Navigation|page)" || true
  [[ -f "out/$src.pdf" ]] || { echo "!! $src.tex did not produce a PDF"; exit 1; }
done

cp out/class-4.pdf       ../content/weeks/week-04/class-4.pdf
cp out/class-4-notes.pdf ../teaching/class-4-notes.pdf
echo "→ installed:"
ls -la ../content/weeks/week-04/class-4.pdf ../teaching/class-4-notes.pdf
