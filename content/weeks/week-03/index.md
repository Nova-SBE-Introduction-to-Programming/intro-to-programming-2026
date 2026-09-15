---
title: Class 3 — Save points
date: 2026-09-15
type: theory
---

# Class 3 — Save points

Block 1 · Theory · 2026-09-15

## What you need

- Last week's folder, with your bug #1 fix and your `ONBOARDING.md` answers.
- A GitHub account (university email). No account yet? Create one at [github.com](https://github.com/) now.
- [GitHub Desktop](https://desktop.github.com/), installed and signed in. Windows: it installs git for you, nothing else needed.
- uv from last week. Tests run with `uv run pytest tests/test_bugs.py`; no install step, pytest is in the project.

## In class

Git in four words: **repo**, **commit**, **branch**, **push**. Save points for code, all through GitHub Desktop buttons, no terminal.

1. **Your folder becomes a repo.** GitHub Desktop → *Add local repository* → *Create a repository here* → *Publish repository*, name it `splitit` or `tiny-crm`, keep it **private**. Last week's fix is your first commit. One repo per person.
2. **Bug #0, one line, one commit.** Read the report, run the red test, follow the click, fix, green, commit, push. Live on SplitIt first, then on your repo.
3. **A spec from the PM.** What `specs/feature-1` asks for, and the tests in `tests/test_feature_1.py` that say when it is done. Run them before you build: four red tests is your to-do list.
4. **Feature 1, live.** Branch → red tests → prompt Codex with the spec → read the diff → green → check it in the app → commit, push, pull request, merge.

## Your turn

- **SplitIt:** bug `issues/000-group-title.md`, then `specs/feature-1-balances.md` on a branch called `feature-1-balances`.
- **Tiny CRM:** bug `issues/000-lead-count.md`, then fix `issues/002-overdue-order.md` (the spec says so at the top), then `specs/feature-1-overdue.md` on a branch called `feature-1-overdue`.

Copies of the bug reports and specs are in the materials below; the ones that count are the files inside your own repo.

## When git is confusing

- Wrong branch? *Current branch* → switch. GitHub Desktop offers to bring your changes along; say yes.
- Broke a file? Right-click it in GitHub Desktop → *Discard changes*.
- Broke the data? `uv run python seed.py`, same as last week.
- An error you don't understand? Screenshot it, ask Codex to explain it, then ask us.

## Homework — before Class 4

1. **Finish feature 1** on its branch: tests green, merged, pushed.
2. **Your repo is the one that counts now.** Not the ZIP, not the folder. Push before you close the laptop, every time.
3. **Read `specs/feature-2` and `issues/002`** in your repo. That is Class 4.

Nothing to hand in. In Class 4 the TA will ask to see your GitHub page: the feature-1 branch and a merged commit.
