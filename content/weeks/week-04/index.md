---
title: Class 4 — Rules, judge, loop
date: 2026-09-22
type: practical
---

# Class 4 — Rules, judge, loop

Block 1 · Practical · 2026-09-22

## What you need

- Your repo, with feature 1 merged and pushed. Missing files, or no repo at all? Start at *A clean start* under Your turn.
- GitHub Desktop signed in (that is what lets Codex push), Codex open on the repo folder, uv working. Nothing new to install.
- Read before class: `specs/feature-2` in your repo, and the bug for your app — SplitIt `issues/002`, Tiny CRM `issues/003`.

## What the slides said

Nothing in this section is a step. It is the lecture half of the class, here so you can read it
back. The steps are under [Your turn](#your-turn).

### Git: one change, start to finish

Last week you learned four words: repo, commit, branch, push. As one story, it is the journey a
single change makes from your idea to the version everyone uses, and it is the workflow you already
know from anything that gets reviewed before it counts.

**`main` is the version everyone trusts.** One file, one history, one truth, not a folder of files
all called *FINAL*. Everybody's copy starts from here. **You never edit the original:** a **branch**
is your own copy to work in, named after the job (`feature-2-categories`, not `my-changes`), and
everyone else carries on from `main` undisturbed. **Every save point is a commit,** a checkpoint
with a note saying what changed: *"Fix group title showing the id"*, not *"update"*. Keep them
small, each one a step you could explain out loud; you can go back to any of them. **`main` has not
moved** while you work: three commits deep, half of it broken, the agent having a bad day, and the
version everyone else is using is untouched. That is the point of a branch. **Until you push, it
only exists on your laptop.** Push puts your draft where the team can see it, and a **pull
request** is you asking someone to read the diff before it counts; today that someone is you,
reviewing the agent. **Merge is the sign-off.** Once it is green and reviewed it comes home: `main`
now includes your work, and the next person's copy starts from there.

### From a model to an agent

Four words, and each one is a region of the same picture.

**A language model** is ChatGPT in a browser: text in, text out. It has never seen your folder and
cannot run anything. In Class 2 *you* were the hands; you pasted code in and out, and you were the
only one who ever found out whether it worked. **A tool** is a named action the model may *ask
for*: read a file, edit a file, run a command. Three cover nearly everything. The important arrow
is the one coming back: the result of the action returns to the model, not to you. **An agent** is
the same model, plus tools, plus a loop: it acts, sees the result, and chooses again, until the job
is done or it needs you. Agent = model + tools + a loop. Run the tests, read the failure, edit,
run again: that chain of tool calls *is* the loop. **The harness** is the software around the
model. The model can only *write* a tool call; the harness runs it, asks your permission first,
puts the output back into the conversation, keeps the whole conversation, and loads `AGENTS.md` at
the start. Codex is one; Claude Code, Cursor and Copilot's agent are others. They differ in tools,
permissions and how they manage the conversation; the loop is the same everywhere, so learn it
once.

**One tool call, in full.** You saw one in Class 2: you asked what was in your expenses file, and
the model, which has never seen that file, emitted a small structured request to *read
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

**The loop has a name: ReAct** ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)): *reason*
(a short thought: "I still do not know what is in that file"), *act* (one tool call), *observe* (the
result comes back), repeat until done. It is the architecture underneath every agent you will use,
and the three standards below are you configuring it: what it reads before the first thought, what
it observes, and when the loop is allowed to stop.

**How we got here, in short.** The ideas are decades old: the **perceptron** (1958) learns from
examples instead of being programmed rule by rule; **backpropagation** (1986) makes networks many
layers deep trainable; **LSTM** (1997) carries memory across a sequence; the
[**Transformer**](https://arxiv.org/abs/1706.03762) (2017) lets every word look at every other, in
parallel. What was missing was never an idea; it was compute and text: cheap parallel arithmetic
(NVIDIA's CUDA in 2007; AlexNet winning an image competition on two gaming cards in 2012) and a
scraped web to read. Training itself is one game repeated a few billion times: hide the next word,
guess, get corrected. No grammar and no facts are typed in, which is why a fluent paragraph can
walk into four-horned unicorns and keep going. **The two jumps that changed the job** were
*instructions* (2022: ChatGPT follows them) and *tools + a loop* (2023–25: the model can request an
action, read the result, and choose again). That is the whole reason the three standards exist: a
model that can act for hours in your repo needs rules and a judge. The year-by-year timeline is in
the standards sheet.

### The three standards

Before you hand work to something fast, tireless and always sure it is done, you ask three
questions: how do I brief it, how do I know it is done, and what happens when it is not?

**The instructions, in two files.** The **rulebook, `AGENTS.md`,** is what Codex reads before it
reads anything else: the rules for *every* task. Commands it cannot guess, boundaries, what is off
limits, and nothing it could work out by reading the code. It lives in git and gets reviewed like
code, so when the agent does something wrong the fix is usually a line here, not a longer prompt.
Codex reads it only at the *start* of a chat. The **spec** is the instructions for *one* task, in
four sections: *Why* (the intent, how it picks when a line can be read two ways), *What* (a
checklist, one line per thing that must be true), *Out of scope* (the fence for this task), *Done
when* (the finish line in plain words). Today's is already in your repo; from Block 2 you write
them.

**The judge: define done before you build.** An agent stops when the work *looks* done, so give it
something that answers pass or fail without asking it. Today that is the tests: **a test is a claim
you can run,** a small function whose name is the spec's *What* line and one word, `assert`, saying
what must be true. They were written before the work, by someone who is not the agent, and they
give the same answer every time; that is what makes them a judge and "the tests pass" a sentence.
Open one and read it; you cannot trust a judge you have not read. Two rules follow: never edit a
test to make it pass (that is cheating, not finishing), and ask for the test *output*, never the
sentence. Read red from the bottom: the last line says how far from done, the message above says
why, and that is your to-do. And green is still not the end: one *Done when* line has no test at
all, and you catch that one by clicking.

**The loop: one task, and a stop condition.** Red, hand it over, it edits and runs, reads the
failure, again, green. One task per loop, on its own branch. The handover is four things in plain
words: what to build, what to leave alone, keep going until the tests pass, then paste the output.
When the same failure comes back twice, stop: read it yourself and start a **new chat** with a
better ask, because a long chat that is going wrong rarely recovers. With nobody watching, the same
loop becomes a command, `/goal`, and its stop is the agent's own word, which is why the goal has to
say how to prove it.

## Your turn

Bug first, then the feature. Everything you type is in a box. Copy it as it is. The only words
that change are the file and branch names, and they are given for both apps. Codex does the git,
in the same chat: you ask, it branches, commits and pushes, and you read the result.

### A clean start, if your repo is missing files

Your repo must have these before anything else works: `AGENTS.md`, `pyproject.toml`, `issues/`,
`specs/`, `tests/`. Ask Codex, with your repo open:

```
List the files in this folder. Tell me whether AGENTS.md, pyproject.toml, issues/, specs/ and tests/ are all here.
```

If anything is missing, or you never made a repo, start from the course copy instead of
repairing yours. Three steps:

1. On github.com, open the course repo for your app and press **Fork**. Keep the name.
   SplitIt: `github.com/Nova-SBE-Introduction-to-Programming/splitit` ·
   Tiny CRM: `github.com/Nova-SBE-Introduction-to-Programming/tiny-crm`
2. In Codex, open your `nova` folder (the one from Class 2) and paste, with your GitHub username in the slot:

```
Clone https://github.com/<your-username>/splitit into this folder, then run uv run pytest inside it and paste the output.
```

   (Tiny CRM: the same line with `tiny-crm`.) Some tests fail; that is the course.
3. In Codex, open the new folder as the project. From here on it is your repo: it already has
   `AGENTS.md`, the issues, the specs and the red tests.

### Set up, once

**1. Pick a cheaper model.** In Codex, the model picker is at the bottom of the message box. Choose
**GPT-5.5 with reasoning set to light**, or **5.6 Luna**. The biggest models burn through a free
plan's limit before the feature is done, and this task does not need them. If your plan runs out
for the day, pair with a neighbour: one laptop, two readers of the diff.

**2. The three rules.** Your `AGENTS.md` has had a last line under *How to answer* since Class 2,
*No git in this project unless the student asks for it explicitly*; that stopped being true last
week. Paste this into a chat:

```
In AGENTS.md, under "How to answer", delete the line about no git and put these three lines in its place:
- Build each task on a branch named after it, e.g. feature-2-categories. Never commit to main directly.
- After every change, run the tests for the task and paste the final output. The output is the proof, not a sentence.
- Never edit, delete or skip anything in tests/. If a test looks wrong, say so and stop.
Show me the diff. Then commit with the message "AGENTS.md: three rules from class 4" and push.
```

Read the diff before you accept it: three lines added, one removed, nothing else.

**3. Start a new chat.** Codex reads `AGENTS.md` only at the start of a chat, so every task today
begins with a new one. Check it worked by asking:

```
What does AGENTS.md tell you to do?
```

It should recite the three rules.

### The bug

**4. A branch,** named after the task, from `main`. SplitIt:

```
Create a branch called bug-002-delete-member from main and switch to it.
```

Tiny CRM:

```
Create a branch called bug-003-won-date from main and switch to it.
```

| | SplitIt | Tiny CRM |
|---|---|---|
| The bug | `issues/002-delete-member-crash.md` | `issues/003-won-date-missing.md` |
| The branch | `bug-002-delete-member` | `bug-003-won-date` |

**5. Red first.** Same chat, before anything is built:

```
Run uv run pytest tests/test_bugs.py and paste the full output. Do not change anything.
```

One test fails. Read the last line, then the message above it: that is the to-do.

**6. The ask.** Same chat. SplitIt:

```
Fix issues/002-delete-member-crash.md. Work only on the branch bug-002-delete-member. After every change, run uv run pytest tests/test_bugs.py and keep going until every test passes. Do not edit anything in tests/. When they pass, paste the final test output and list every file you changed.
```

Tiny CRM:

```
Fix issues/003-won-date-missing.md. Work only on the branch bug-003-won-date. After every change, run uv run pytest tests/test_bugs.py and keep going until every test passes. Do not edit anything in tests/. When they pass, paste the final test output and list every file you changed.
```

**7. Watch it loop.** Read, edit, run, red, again. Three things to hold it to: if it says "done"
without the test output, ask for the output; if it touched a test, tell it to put the test back and
say the rule; if the same failure comes back twice, stop, read it yourself, start a new chat, and
ask again with the symptom in your own words.

**8. Green? Check it yourself.** Read every changed line:

```
Show me the full diff of this branch against main.
```

Then start the app and do the thing the bug report describes:

```
Start the app and give me the address to open in the browser.
```

The tests are the finish line, not the proof.

**9. Commit, push, pull request, merge.**

```
Commit everything with a message that says what changed, push the branch, and give me the link to open a pull request.
```

Open the link. On GitHub, read *Files changed* once more, then *Merge pull request*. Back in the
chat, so the feature starts from the fixed version:

```
Switch to main and pull.
```

### The feature

**10. A branch,** from `main`, in a new chat. SplitIt:

```
Create a branch called feature-2-categories from main and switch to it.
```

Tiny CRM:

```
Create a branch called feature-2-conversion from main and switch to it.
```

**11. Red first.** Four tests, all red; that is the to-do list.

```
Run uv run pytest tests/test_feature_2.py and paste the full output. Do not change anything.
```

**12. The ask.** SplitIt:

```
Build specs/feature-2-categories.md. Work only on the branch feature-2-categories. After every change, run uv run pytest tests/test_feature_2.py and keep going until all four tests pass. Do not edit anything in tests/. When they pass, paste the final test output and list every file you changed.
```

Tiny CRM:

```
Build specs/feature-2-conversion.md. Work only on the branch feature-2-conversion. After every change, run uv run pytest tests/test_feature_2.py and keep going until all four tests pass. Do not edit anything in tests/. When they pass, paste the final test output and list every file you changed.
```

**13. Steps 7 to 9 again:** watch, check yourself, merge. One *Done when* line of the spec has no
test; only clicking the app catches it.

### One rule of your own

**14.** Something the agent did today that you did not want is one new line in `AGENTS.md`. Write
the line yourself, then:

```
Add this line to AGENTS.md under "How to answer": <your line>. Commit with a message that says why, and push.
```

This is the retro at the end of class, and it is homework if you did not get to it.

### Instead of watching: `/goal`

Optional, and only after a red test. Codex keeps taking turns until it decides the goal holds. Two
things to know: it decides for itself, so the goal must say how to prove it; and it writes neither
the rulebook nor the spec. In a new chat on the branch, paste:

```
/goal every test in tests/test_feature_2.py passes, shown by the final pytest output, and nothing in tests/ changed. Stop after 20 turns.
```

`/goal` on its own shows how it is going; `/goal pause`, `/goal resume` and `/goal clear` do what
they say. When it stops, step 8: read the diff, click the app.

### Done when

- Bug test green, on its branch, pull request merged.
- Feature 2 tests green **without touching `tests/`**, the feature visible in the app, pull request merged.
- `AGENTS.md` has the three lines from class, plus one rule of your own.

Copies of the specs, the bug reports and the standards sheet are in the materials below; the files that count are the ones in your repo.

## Homework — before Class 5

1. **Finish feature 2**: green, merged, pushed.
2. **One rule in `AGENTS.md`** that would have prevented the worst thing the agent did today. Commit it with a message that says why.
3. Block 2 starts next week: a spec you build alone. Keep the repo pushed; it is what you build on.
