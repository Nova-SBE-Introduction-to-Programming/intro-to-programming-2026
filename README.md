# Introduction to Programming — course site

Static course site for Nova SBE, 2026/27. One Python script, one template, one stylesheet.
Students read it; only I edit it. Everything students see lives in `content/`.

## Add a week

```
mkdir content/weeks/week-05
```

Write `content/weeks/week-05/index.md` with a front-matter block and the class notes:

```markdown
---
title: Class 5 — Your own thing
date: 2026-09-29
type: theory
---

# Class 5 — Your own thing

What happened, homework, links.
```

`type` is `theory` or `practical` (it becomes the badge on the home page).
Then drop the deck (`class-5.html`) and any files (PDFs, CSVs, zips, extra `.md` pages) into the same folder and push.
The home page lists the week, and the week page lists every file in the folder with its size — nothing else to write.

## Preview locally

```
python -m venv .venv && source .venv/bin/activate   # once
pip install -r requirements.txt                       # once
python build.py && python -m http.server -d _site
```

Open <http://localhost:8000>.

## How the build works

1. `build.py` wipes `_site/`, copies `style.css` into it.
2. Every `.md` under `content/` is rendered with the `markdown` library and poured into `template.html` at the same relative path (`content/setup.md` → `_site/setup.html`).
3. Every other file is copied byte-for-byte — decks (`.html`) included, they are self-contained.
4. `content/index.md` gets a weeks index appended; each `weeks/week-NN/index.md` gets a materials list appended.
5. Front matter is the `---` block at the top of a `.md` file: `key: value` lines, parsed with plain string splitting. Keys used: `title`, `date`, `type`.

Links are relative, so the site works at `https://<user>.github.io/<repo>/` as well as at the root.

## Deploy (one-time setup)

Push to GitHub, then in the repository: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
From then on, every push to `main` runs `.github/workflows/deploy.yml`, which builds `_site/` and publishes it.
