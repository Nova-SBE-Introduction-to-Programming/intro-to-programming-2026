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

**How we got here, in short.** The ideas are decades old: the **perceptron** (1958) learns from
examples instead of being programmed rule by rule; **backpropagation** (1986) makes networks many
layers deep trainable; **LSTM** (1997) carries memory across a sequence; the
[**Transformer**](https://arxiv.org/abs/1706.03762) (2017) lets every word look at every other, in
parallel. What was missing was never an idea — it was compute and text: cheap parallel arithmetic
(NVIDIA's CUDA in 2007; AlexNet winning an image competition on two gaming cards in 2012) and a
scraped web to read. Training itself is one game repeated a few billion times: hide the next word,
guess, get corrected. No grammar and no facts are typed in, which is why a fluent paragraph can
walk into four-horned unicorns and keep going.

**The two jumps that changed the job** were *instructions* (2022: ChatGPT follows them) and *tools
+ a loop* (2023–25: the model can request an action, read the result, and choose again). That is
the whole reason the three standards below exist — a model that can act for hours in your repo
needs rules and a judge. The year-by-year timeline is in the standards sheet.

### Then, three standards

These three are the class. Everything above is background; everything below is you doing them.

1. **The brief, in two files.** The **rulebook — `AGENTS.md`** — is what Codex reads before it
   reads anything else: the rules for *every* task. Commands it cannot guess, boundaries, what is
   off limits — and nothing it could work out by reading the code. It lives in git and gets
   reviewed like code, so when the agent does something wrong the fix is usually a line here, not a
   longer prompt. Today you add three rules to the one already in your repo (below) and commit
   them; Codex reads the file only at the *start* of a thread, so open a new one afterwards.
   The **spec** is the brief for *one* task, in four sections: *Why* (the intent — how it picks
   when a line can be read two ways), *What* (a checklist, one line per thing that must be true),
   *Out of scope* (the fence for this task), *Done when* (the finish line in plain words). Today's
   is already in your repo; from Block 2 you write them.

2. **The judge — define done before you build.** An agent stops when the work *looks* done, so
   give it something that answers pass or fail. Today that is `tests/test_feature_2.py`: four
   tests, already red, and that is your to-do list. **A test is a claim you can run** — a small
   function whose name is the spec's *What* line, and one word, `assert`, saying what must be true.
   Open one and read it; you cannot trust a judge you have not read. Two rules follow: never edit a
   test to make it pass (that is cheating, not finishing), and ask for the test *output*, never the
   sentence "all tests pass". And green is still not the end — one *Done when* line has no test at
   all, and you catch that one by clicking.

3. **The loop — one task, and a stop condition.** Red → hand it over → it edits and runs → read the
   failure → again → green. One task per loop, on its own branch. The handover is four things in
   plain words: what to build, what to leave alone, keep going until the tests pass, then paste the
   output. When the same failure comes back twice, stop: read it yourself and start a **new thread**
   with a better ask, because a long thread that is going wrong rarely recovers. With nobody
   watching, the same loop becomes a command — `/goal`, below.

Live on SplitIt: the three lines go into `AGENTS.md`, feature 2 starts on a branch, the ask goes
in, we watch it loop, then we read the diff before we trust it.

### Delegating coding agents

The whole of the above as the things you do, in order — the same six steps that are on the slide.
Three of the four things in the first group are already in your repo; what changes in Block 2 is
that you write the spec and ask for the tests yourself.

**First, set it up** — all of this happens before the agent is told anything.

1. **The rules.** Open `AGENTS.md`; under *How to answer*, replace the *No git* line with the three
   lines below. Read the diff, commit, push. Then open a **new thread** — Codex reads the file only
   at the start of one.
2. **The task.** Read the spec: *Why* · *What* (one `- [ ]` line per thing that must be true) ·
   *Out of scope* · *Done when*. Already in your repo as `specs/feature-2-*.md`. From Block 2 you
   write it: same four headings.
3. **The tests.** Run them before anything is built. Already in your repo as
   `tests/test_feature_2.py` — four red, and that is your to-do list. From Block 2, ask for them
   first: *"Write one test per line of the What checklist in `specs/<spec>.md`, in
   `tests/test_<name>.py`. No implementation yet."* Run them; they must fail.
4. **A branch,** named after the task (`feature-2-categories`, `feature-2-conversion`).

**Then hand it over** — one task, one chat.

5. **The ask,** in a new thread: what to build, what to leave alone, and keep going until the tests
   pass, then paste the test output. The exact wording is [below](#the-loop-prompt); or set it as a
   goal and leave it.

**Then check it yourself** — the part no test can do.

6. **Read the diff, click the app.** Then commit, push, pull request, merge.

Two things that are not steps, because they are what you do when it goes wrong: if the same failure
comes back twice, stop, read it yourself and start a new thread with a better ask; and when the
agent does something you did not want, that is one new line in `AGENTS.md`, with the reason in the
commit message.

### `/goal` in Codex

The loop as a command: you give Codex a finish line and it keeps taking turns until it holds. Two things to know before you use it. Codex decides for itself when it is "confident" it is there — that is its own word, so the goal must say how to prove it (run the tests, show the output). And nothing in it writes the rulebook or the spec; it automates the easy half.

1. Once, in a terminal: `codex features enable goals`. Restart Codex.
2. Red test first. Never set a goal without one.
3. In a new thread on the branch: `/goal` followed by the spec's *Done when* with the fence in it — for SplitIt:
   > `/goal every test in tests/test_feature_2.py passes, shown by the final pytest output, and nothing in tests/ changed. Stop after 20 turns.`
4. `/goal` on its own shows the goal and how it is going. `/goal pause`, `/goal resume`, `/goal clear` do what they say.
5. When it stops: the same human check. Read the diff, click the app.

Not on Codex? Claude Code has the same command with the same name; there a second, smaller model reads the thread after each turn and rules *not yet*, *met* or *impossible*. It cannot run your tests either.

### The three rules you add to `AGENTS.md`

Your `AGENTS.md` has been in the repo since Class 2 (it came in the ZIP). Open it. Under **How to answer**, the last line says *No git in this project unless the student asks for it explicitly*: that was true until last week. Delete that line and put these three in its place, read the diff, then commit and push.

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
