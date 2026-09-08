---
title: Class 2 — Meet the code
date: 2026-09-08
type: practical
---

# Class 2 — Meet the code

Block 1 · Practical · 2026-09-08

## Get it running

Everything today is local — no git, no GitHub. That comes in Class 3.

1. Download the ZIP for your group's app from the materials below: **splitit.zip** or **tiny-crm.zip**.
2. Unzip it somewhere you'll find again — a `nova` folder in Documents.
3. Open that folder in Codex: **Open folder** → pick the folder that contains `app.py`. Codex now calls it a *project*.
4. Open a terminal *in that folder* (Windows: right-click in the folder → *Open in Terminal*; macOS: type `cd `, drag the folder into Terminal, Enter), then `pip install -r requirements.txt` and `streamlit run app.py`. Your browser opens on the app. (macOS: `pip3` and `python3`.) Or ask Codex to do it and approve the two commands.

Cloned the repo last week instead? That works too.

**Folder, project, repository.** Three words, one thing on your disk. A *folder* is what you unzipped. A *project* is that folder opened in Codex, plus the memory of what you asked about it. A *repository* is a folder whose history git tracks — yours becomes one in Class 3. One app, one folder, one project; don't rename or move it. The long version is in [Setup](../../setup.html#4-folder-project-repository-three-words-for-one-thing).

## In class

The product tour: the workflow you drew last week, running. Your nouns became `data/`, your steps became `app.py`, your decisions became `logic.py`. Then the folder behind the screens, the six words you need to read it (file, function, call, table, entry point, validation), and the three ways every new engineer answers "where does X happen?": follow the click, search the project for the exact words, ask the AI and verify. In Codex all three go through the chat — the difference is what you ask for: *show me*, *find the text*, *explain*.

Then the question sheet, `ONBOARDING.md`, inside your folder. Ten questions: six about the code, four about checking the AI. The TA answers one live; your group answers the rest, in the file, with a location for every answer. Question 9 is **bug #1** (`issues/001.md`): reproduce it, find the line, fix it, show the TA before and after.

## Homework — before Class 3

1. **Finish the sheet** in `ONBOARDING.md`. Every answer with a location: file and line, or what you clicked. To write in the file, tell Codex what to write under which question, then read the change before accepting it.
2. **Keep the folder.** Don't delete or rename it. In Class 3 it becomes a git repository, and your sheet and your bug fix become your first commit.
3. **Every laptop runs the app.** Still stuck? Post the error on the Moodle forum with a screenshot.
4. **Read `specs/feature-1`** in your folder. That's what gets built live in Class 3, with tests and a branch.

The question sheets are below for reference; the one that counts is the `ONBOARDING.md` inside your own folder.
