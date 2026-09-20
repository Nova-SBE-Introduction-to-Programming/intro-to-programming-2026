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
The class opens with git, because the thing you will build today lives on a branch; then it asks
what an agent actually is; then it gives you the three standards every agentic team uses.

### First, git: one change, start to finish

Last week you learned four words: repo, commit, branch, push. Here they are as one story — the
journey a single change makes, from your idea to the version everyone uses. It is the workflow you
already know from anything that gets reviewed before it counts.

1. **`main` is the version everyone trusts.** One file, one history, one truth — not a folder of
   files all called *FINAL*. Everybody's copy starts from here.
2. **You never edit the original.** A **branch** is your own copy to work in, named after the job
   (`feature-2-categories`, not `my-changes`). Everyone else carries on from `main`, undisturbed.
3. **Every save point is a commit.** A **commit** is a checkpoint with a note saying what changed
   — *"Fix group title showing the id"*, not *"update"*. Keep them small: each one a step you could
   explain out loud. You can go back to any of them.
4. **`main` has not moved.** Three commits deep, half of it broken, the agent having a bad day —
   the version everyone else is using is untouched. That is the point of
   working on a branch.
5. **Until you push, it only exists on your laptop.** **Push** puts your draft where the team can
   see it. A **pull request** is you asking someone to read the diff before it counts — and today
   that someone is you, reviewing the agent.
6. **Merge is the sign-off.** Once it is green and reviewed, it comes home: `main` now includes
   your work, and the next person's copy starts from there. Then the cycle begins again.

### Then, from a model to an agent

Four words, and each one is a region of the same picture.

1. **A language model.** ChatGPT in a browser: text in, text out. It has never seen your folder
   and cannot run anything. In Class 2 *you* were the hands — you pasted code in and out, and you
   were the only one who ever found out whether it worked.
2. **Tools.** A tool is a named action the model may *ask for*: read a file, edit a file, run a
   command. Three cover nearly everything. The important arrow is the one coming back: the result
   of the action returns to the **model**, not to you.
3. **An agent.** The same model, plus tools, plus a loop: it acts, sees the result, and chooses
   again, until the job is done or it needs you. **Agent = model + tools + a loop.** Run the tests
   → read the failure → edit → run again: that chain of tool calls *is* the loop.
4. **The harness.** The model can only *write* a tool call. The software around it runs the call,
   asks your permission first, puts the output back into the conversation, keeps the whole
   conversation, and loads `AGENTS.md` at the start. That software is the harness. Codex is one;
   Claude Code, Cursor and Copilot's agent are others. They differ in tools, permissions and how
   they manage the conversation; the loop is the same everywhere, so learn it once.

**One tool call, in full.** You saw one in Class 2: you asked what was in your expenses file, and
the model — which has never seen that file — emitted a small structured request to *read
expenses.csv*; Codex checked with you, read it, pasted the line back into the conversation, and only
then could the model tell you it was €30 for dinner. A request instead of prose, executed after
your approval, with the result going back in as ordinary text. Say no, and it has nothing to answer
with.

**Reasoning** is the other half: newer models work a problem out in steps before answering instead
of replying with the first plausible thing. Ask for *"make it so Ana doesn't owe anything"* and a
guess picks one of three readings at random; a model that reasons first notices that two of them
move everyone else's money, picks the safe one, and tells you the assumption so you can overrule
it. It matters because an agent takes many steps, and a guess at step one is still wrong at step
ten.

**The loop has a name: ReAct** ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)) — *reason*
(a short thought: "I still do not know what is in that file"), *act* (one tool call), *observe* (the
result comes back), repeat until done. It is the architecture underneath every agent you will use,
and the three standards below are you configuring it: what it reads before the first thought, what
it observes, and when the loop is allowed to stop.

**How we got here: the ideas came first, by decades.** 1958: Frank Rosenblatt's **perceptron** — a machine that learns from examples instead of being programmed rule by rule, which is still the idea. 1969: Marvin Minsky and Seymour Papert's book *Perceptrons* proved that a single layer cannot learn even XOR, and the funding went away — the first "AI winter". (Careful with the attribution: they wrote the critique that made multi-layer networks the open problem; they did not invent them.) 1986: Rumelhart, Hinton and Williams published **backpropagation** in *Nature* — an error signal that flows back through every layer, so networks many layers deep finally become trainable. That is the answer to 1969, seventeen years late. 1997: Hochreiter and Schmidhuber's **LSTM** carries memory across a sequence, so word 200 can depend on word 3. 2017: ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) introduces the **Transformer** — attention instead of recurrence, and it trains in parallel. Every model in the list below is one of these. (Hinton shared the [2024 Nobel Prize in Physics](https://www.nobelprize.org/prizes/physics/2024/summary/) with John Hopfield for this line of work.)

**What was missing was not the idea. It was compute and text.** NVIDIA's CUDA (2007) let ordinary programmers run their own maths on a graphics card, which is thousands of tiny arithmetic units built for game pixels, which turned out to be what a neural network needs; in 2012 AlexNet (Krizhevsky, Sutskever and Hinton) trained on two consumer graphics cards and won the ImageNet image-recognition competition with roughly half the error of the runner-up, and that is the moment it became obvious to everyone. Common Crawl — a non-profit founded in 2007 that has published full-scale crawls of the public web since 2011 — made the web itself available as a training corpus. Neither one is an idea about intelligence: neural networks are not new, cheap parallel arithmetic and a scraped web are. That is why this happened now and not in 1990.

**Then, one line per year.** 2018 GPT-1 continues text · 2019 GPT-2 writes coherent paragraphs · 2020–21 GPT-3 learns from examples in the prompt, Codex/Copilot autocomplete code · 2022 ChatGPT follows instructions and converses, ReAct is published · 2023 GPT-4 and tool calling: the model can request an action and read the result · 2024 reasoning models (OpenAI o1, DeepSeek-R1, Claude's extended thinking) work through a problem step by step before answering — asked *why do the balances sum to +10?* they trace the arithmetic to line 95 instead of guessing a fix — and computer use lets a model look at a screen and click · 2025 coding harnesses (Claude Code, Codex CLI, Cursor's agent) build features in your repo, `AGENTS.md` becomes a convention · 2026 long-running agents work for hours with a judge. Size, for scale: GPT-1 had 117 million parameters, GPT-2 1.5 billion, GPT-3 175 billion, a thousandfold in two years; GPT-4's was never published (a 2023 report put it near 1.8 trillion, unconfirmed) and no lab has published a count since. The model got better every year; the two jumps that changed the job were *instructions* (2022) and *tools + a loop* (2023–25). The standards exist because a model that can act for hours needs rules and a judge.

### Then, three standards

You will use all three before you leave:

1. **The rulebook — `AGENTS.md`.** The file Codex reads before it reads anything else. What goes in, what stays out, and why it lives in git like any other code. In class you add three rules to yours and commit them: a boundary, an evidence rule, and one thing that is off-limits (written out below).
2. **The judge.** Define *done* before you build. The spec's *Done when* and the tests in `tests/test_feature_2.py` are the judge: four red tests are your to-do list, and you never edit them to make them pass. After green, the human check: read the diff, click the app.
3. **The loop.** Red → build → run the tests → read the failure → fix → run again → green → stop. One task per loop. When it goes wrong twice, stop the thread and start a new one with a better prompt.

Live on SplitIt: the three lines go into `AGENTS.md`, feature 2 starts on a branch, the loop prompt goes in, we watch it loop, then we read the diff before we trust it.

### The three rules you add to `AGENTS.md`

Copy these under **How to answer** in your own `AGENTS.md`, read the diff, then commit and push.

```
- Build each spec on a branch named after it, e.g. feature-2-categories. Never commit a feature to main directly.
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
| Same failure twice in a row | Stop. Read the failure yourself: the last line says what, the line above says where. New thread, better prompt. |
| It fixed three other things too | Discard them. One task per loop. Ask again for the one thing. |
| Tests green, app wrong | The judge missed something. Write down what — that is a test that should exist. Fix by hand or re-prompt with the symptom. |

## Homework — before Class 5

1. **Finish feature 2**: green, merged, pushed.
2. **One rule in `AGENTS.md`** that would have prevented the worst thing the agent did today. Commit it with a message that says why.
3. Block 2 starts next week: a spec you build alone. Keep the repo pushed; it is what you build on.
