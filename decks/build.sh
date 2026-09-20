#!/usr/bin/env bash
# Build the Class 4 deck.
#   ./build.sh                 diagrams + both PDFs, installed into the repo
#   ./build.sh --no-diagrams   skip the Mermaid step (diagrams unchanged)
#
# Mermaid sources live in diagrams/, render to figures/*.pdf (committed).
# LaTeX output goes to out/ (gitignored); the two PDFs are then installed:
#   out/class-4.pdf        -> content/weeks/week-04/class-4.pdf   (published deck)
#   out/class-4-notes.pdf  -> teaching/class-4-notes.pdf          (speaker notes, not published)
set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" != "--no-diagrams" ]]; then
  echo "→ rendering Mermaid diagrams"
  uv run --quiet --with playwright python render-diagrams.py
fi

mkdir -p out
for src in class-4 class-4-notes; do
  echo "→ compiling $src.tex"
  tectonic -X compile "$src.tex" --outdir out 2>&1 \
    | grep -viE "absolute path|^note:|already defined|color stack" || true
done

cp out/class-4.pdf       ../content/weeks/week-04/class-4.pdf
cp out/class-4-notes.pdf ../teaching/class-4-notes.pdf
echo "→ installed:"
ls -la ../content/weeks/week-04/class-4.pdf ../teaching/class-4-notes.pdf
