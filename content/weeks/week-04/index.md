---
title: Class 4 — Rules, judge, loop
date: 2026-09-22
type: practical
---

# Class 4 — Rules, judge, loop

Block 1 · Practical · 2026-09-22

## What you need

- Your repo, with feature 1 merged and pushed. The TA checks your GitHub page in the first five minutes.
- GitHub Desktop signed in, Codex open on the repo folder, uv working. Nothing new to install.
- Read before class: `specs/feature-2` in your repo, and the bug for your app — SplitIt `issues/002`, Tiny CRM `issues/003`.

## In class

Last week you watched a feature get built. Today you build one alone, the way agentic teams do it.

**First, what an agent is.** ChatGPT in a browser is a plain language model: text in, text out. It has never seen your folder and cannot run anything — you paste code in, you paste it out, you find out whether it works. Codex on your repo is the same kind of model **plus tools, in a loop**: it can *read* a file, *edit* a file and *run* a command, and it sees the result of each action before choosing the next. Each of those actions is a **tool call** — the model writes a request like `run: uv run pytest tests/test_feature_2.py` instead of prose, Codex executes it (after asking you), and the output goes back into the conversation for the model to read. Run → read the failure → edit → run again: that chain of tool calls *is* the loop, and the approval prompt is where you sit inside it. Without tools it could only ever give you advice, and you would be the hands — and the only one who ever found out whether it worked.

The other half is **reasoning**: newer models work a problem out in steps before answering instead of replying with the first plausible thing. Ask why SplitIt's balances were wrong and a guess names a likely-looking line; reasoning writes out the arithmetic — 30 paid, two people charged 15, the payer never charged — and lands on the real one. It matters because an agent takes many steps, and a guess at step one is still wrong at step ten.

The loop has a name: **ReAct** ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)) — *reason* (a short thought: "two tests still fail on CATEGORIES"), *act* (one tool call), *observe* (the result comes back), repeat until done. The model can only *write* a tool call; the software that runs it, asks your permission, feeds the output back, keeps the history, loads `AGENTS.md` and stops the loop is the **harness**. Codex is a harness; Claude Code, Cursor and Copilot's agent are others. They all run the same loop and differ only in tools, permissions and how they manage the conversation — which is why the three standards below apply to every one of them.

**How we got here, in one line per year.** 2018 GPT-1 continues text · 2019 GPT-2 writes coherent paragraphs · 2020–21 GPT-3 learns from examples in the prompt, Codex/Copilot autocomplete code · 2022 ChatGPT follows instructions and converses, ReAct is published · 2023 GPT-4 and tool calling: the model can request an action and read the result · 2024 reasoning models (OpenAI o1, DeepSeek-R1, Claude's extended thinking) work through a problem step by step before answering — asked *why do the balances sum to +10?* they trace the arithmetic to line 95 instead of guessing a fix — and computer use lets a model look at a screen and click · 2025 coding harnesses (Claude Code, Codex CLI, Cursor's agent) build features in your repo, `AGENTS.md` becomes a convention · 2026 long-running agents work for hours with a judge. The model got better every year; the two jumps that changed the job were *instructions* (2022) and *tools + a loop* (2023–25). The standards exist because a model that can act for hours needs rules and a judge.

Then three standards, and you will use all three before you leave:

1. **The rulebook — `AGENTS.md`.** The file Codex reads before it reads anything else. What goes in, what stays out, and why it lives in git like any other code. In class you add three rules to yours and commit them: a boundary, an evidence rule, and one thing that is off-limits (written out below).
2. **The judge.** Define *done* before you build. The spec's *Done when* and the tests in `tests/test_feature_2.py` are the judge: four red tests are your to-do list, and you never edit them to make them pass. After green, the human check: read the diff, click the app.
3. **The loop.** Red → build → run the tests → read the failure → fix → run again → green → stop. One task per loop. When it goes wrong twice, stop the thread and start a new one with a better prompt.

Live on SplitIt: the three lines go into `AGENTS.md`, feature 2 starts on a branch, the loop prompt goes in, we watch it loop, then we read the diff before we trust it.

## Git standards

Last week you learned the four words: repo, commit, branch, push. These are the habits on top —
the ones that make a codebase survivable once more than one person touches it. From Block 3 that
person is your team; for now it is you and the agent.

1. **`main` always works.** Risky work happens on a branch; `main` only ever receives finished,
   green work. If `main` is broken, everyone who clones it is blocked.
2. **One job, one branch, named after the job.** `feature-2-categories`, not `my-changes`. The name
   should say what is inside without opening it. Keep commits small — each one a step you could
   explain out loud, with a message that says what changed (*"Fix group title showing the id"*, not
   *"update"*).
3. **Push before you close the laptop. Pull before you start the next thing.** Your laptop and
   GitHub are two copies; the round trip is commit → push → pull request → merge → pull. The pull
   request is where a human reads the diff — today, that human is you, reviewing the agent.

### The three rules you add to `AGENTS.md`

Copy these under **How to answer** in your own `AGENTS.md`, read the diff, then commit and push.

```
- Build each spec on a branch named after it, e.g. feature-2-categories. Never commit to main directly.
- After every change, run the tests for the task and paste the final output. The output is the proof, not a sentence.
- Never edit, delete or skip anything in tests/. If a test looks wrong, say so and stop.
```

Codex only reads `AGENTS.md` at the *start* of a thread, so open a new thread after you commit them.

## Your turn · 30 min

Same order as last week: one bug, then the feature, on a branch. Tests first, every time.

- **SplitIt:** `issues/002-delete-member-crash.md` (its test is `test_bug_002` in `tests/test_bugs.py`), then `specs/feature-2-categories.md` on a branch called `feature-2-categories`.
- **Tiny CRM:** `issues/003-won-date-missing.md` (`test_003` in `tests/test_bugs.py`), then `specs/feature-2-conversion.md` on a branch called `feature-2-conversion`.

### The loop prompt

Paste this into a **new thread** in Codex, with the spec file open, and change the file names for your app:

> Build `specs/feature-2-categories.md`. Work only on the branch `feature-2-categories`. After every change, run `uv run pytest tests/test_feature_2.py` and keep going until all four tests pass. Do not edit anything in `tests/`. When they pass, paste the final test output and list every file you changed.

The judge is the test output, not the sentence "done". Then *you* check: the diff in GitHub Desktop, and the app in the browser.

### Done when

- Bug test green, committed on `main`, pushed.
- Feature 2 tests green **without touching `tests/`**, the feature visible in the app, on its branch, pushed, pull request merged.
- `AGENTS.md` has the three lines from class, plus one rule of your own from something the agent got wrong today.

Copies of the specs, the bug reports and the standards sheet are in the materials below; the files that count are the ones in your repo.

## When the loop goes wrong

| What you see | What to do |
|---|---|
| It edited a test | *Discard changes* on that file in GitHub Desktop. Say: "never edit tests/". Run again. |
| It says "done" but the tests are red | "Paste the test output." The output is the judge, not the sentence. |
| Same failure three times in a row | Stop. Read the failure yourself: the last line says what, the line above says where. New thread, better prompt. |
| It fixed three other things too | Discard them. One task per loop. Ask again for the one thing. |
| Tests green, app wrong | The judge missed something. Write down what — that is a test that should exist. Fix by hand or re-prompt with the symptom. |

## Homework — before Class 5

1. **Finish feature 2**: green, merged, pushed.
2. **One rule in `AGENTS.md`** that would have prevented the worst thing the agent did today. Commit it with a message that says why.
3. Block 2 starts next week: a spec you build alone. Keep the repo pushed; it is what you build on.
