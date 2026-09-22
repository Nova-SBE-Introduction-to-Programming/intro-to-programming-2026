---
title: Agentic coding standards · Part I — rules, judge, loop
---

# Agentic coding standards · Part I

Three things every team that ships with AI agents does. They fit on one page and you will use all three today. First, one paragraph on what an agent is — because the standards are about controlling one.

## 0 · What an agent is

Four words, in order, and each one adds one thing to the picture:

| | What it is | What it adds |
|---|---|---|
| **Language model** | Text in, text out. Has never seen your folder; cannot run anything. | — |
| **Tools** | Named actions it may *ask for*: read a file, edit a file, run a command. | The result comes back to the **model**, not to you |
| **Agent** | Model + tools + a loop. Acts, sees the result, chooses again. | The loop |
| **Harness** | The software around the model: runs the call, asks you first, keeps the conversation, loads `AGENTS.md`. Codex, Claude Code, Cursor. | The box all of it runs in |

**A plain LLM writes.** ChatGPT in a browser predicts the next words of an answer. It has never seen your folder; it cannot open a file, run a test or check anything. You copy code in, you paste it out, you find out whether it works. When it says "the tests pass", that is a sentence that sounds right — nothing more.

**An agent acts.** Codex on your repo is the same kind of model **plus tools, in a loop**. The tools are few: *read* a file, *edit* a file, *run* a command. The loop is: act, see the result, decide the next action, until the job is done or it needs you.

**A tool call** is how it acts. Ask *what was the last expense?* and the model — which has never
seen your files — cannot answer. Here is the whole exchange:

| | |
|---|---|
| you type | what was the last expense? |
| the model emits | `{"tool": "read_file", "path": "data/expenses.csv"}` |
| Codex asks | *Codex wants to read `data/expenses.csv`. Allow?* |
| Codex pastes back | `29,3,8,Jantar no Zé dos Cornos,30.00,2026-08-25` |
| the model answers | €30 — dinner at Zé dos Cornos, on 25 August. |

Three things are worth noticing. The model's output is **not prose** — it is a small structured
request naming a tool and what to use it on; it cannot open anything, it can only ask. **Codex** is
what touches your disk, and it stops to ask you first. That is the approval prompt you
click through all lesson. And the file's real line is **pasted into the conversation** as ordinary
text, which the model then reads like any other message. Say no, and it has nothing to answer with.

Every edit and every command is the same three steps: a request, your approval, a result coming
back. (The exact wire format differs between tools; you never type it yourself.)

**The loop has a name: ReAct.** *Reason* — the model writes a short thought ("two tests still fail on CATEGORIES"). *Act* — it emits one tool call. *Observe* — the result comes back into the conversation. Repeat until the task is done or it needs you. The original paper showed models do far better alternating thought and action than answering in one go; every agentic coding tool since is that loop with better plumbing.¹

**The harness.** The model can only *write* a tool call. The software around it runs the call, shows you the approval prompt, puts the output back, keeps the history, loads `AGENTS.md` at the start, and stops the loop. That software is the harness. Codex is one; Claude Code, Cursor, Copilot's agent are others. Same loop everywhere — they differ in the tools offered, what needs permission, and how the conversation is managed. Learn the loop once; the tools are interchangeable. The three standards below are you configuring the harness: the rulebook it loads, the judge it runs, the stop condition of its loop.

**How we got here.** Same direction for eight years, four kinds of capability added in order:

| When | What arrived | What it meant for your code |
|---|---|---|
| 2018–19 | GPT-1, GPT-2: continue text, then write coherent paragraphs | Plausible snippets, often wrong |
| 2020–21 | GPT-3: learns from examples in the prompt; Codex → Copilot | Autocomplete: finishes the line you started |
| 2022 | ChatGPT: follows instructions, holds a conversation; ReAct published | Answers you paste in and out |
| 2023 | GPT-4; tool calling: the model emits a request and reads the result | It can run your tests, if a harness runs them |
| 2024 | Reasoning models (OpenAI o1, then DeepSeek-R1, Claude's extended thinking): the model works through the problem step by step before answering. Computer use (Claude, OpenAI Operator): it looks at a screen, clicks and types | Multi-step tasks stop falling apart. Asked *why do the balances sum to +10?*, it traces the arithmetic — payer credited 30, two members debited 15, payer never debited — to line 95, instead of guessing a plausible edit. It plans across files before editing and stops earlier when stuck |
| 2025 | Coding harnesses (Claude Code, Codex CLI, Cursor agent); `AGENTS.md` | Builds the feature in your repo while you watch |
| 2026 | Long-running agents: desktop apps, loops with a judge | Works for hours while you're away — if you wrote the rules and the judge |

The two jumps that changed the job: *instructions* (2022) and *tools + a loop* (2023–25). Everything since is plumbing and stamina — and the reason the standards exist.

**Context, and context rot.** Everything the model can see at once — your messages, every file it
read, every command's output — is its *context window*, and it has a fixed size. Windows have grown
fast (8k tokens, then 32k, then 128k, now a million) but the useful part has not grown with them.
Models use the **start** and the **end** of a long context well and the middle badly: that is the
"lost in the middle" result, measured across models and tasks and still holding.² A 2025 re-run
across eighteen current models found every one of them got worse as the input grew — well short of
the limit.³ And it holds for coding, not just reading: given real GitHub bugs with more and more of
the repository in the window, Claude 3.5 Sonnet fixed 29% of them at 32k tokens and 3% at 256k — the
same bugs, only more text around them.⁴ So a long thread does not get wiser, it gets vaguer. Two habits follow, and both are
already rules below: start a new thread instead of arguing in an old one, and let the tool
*compact* — it throws away the soft middle and keeps a summary plus what just happened. That is not
the tool being lazy; it is dropping the part the model was using worst.

**Why it matters here.** An agent can *run* the tests — but it can still *say* they passed without showing you. Tools give it hands; they don't make it honest. Hence the standards: a rulebook it reads before it acts, a judge whose output it cannot argue with, and a loop that knows when to stop.

## 1 · The rulebook — `AGENTS.md`

**What it is.** A README for agents. Codex reads it at the start of every session, before it reads anything else — so do Claude Code, Copilot, Cursor and twenty-odd other tools. It is the one place to say how *this* project is run and what the agent must never do. Your repo has had one since Class 2; open it.

**What goes in.** Only what the agent cannot work out by reading the code:

- commands it can't guess — `uv run streamlit run app.py`, `uv run pytest`, `uv run python seed.py`
- boundaries — *never edit `tests/`*, *don't touch `data/` by hand*, *one issue or spec per task*
- repo etiquette — *branch named after the spec*, *commit message says what changed*
- how to report — *paste the test output*, *list every file you changed*

**What stays out.** Anything it can read in the code. Long explanations. "Write clean code." Every extra line makes the important lines easier to miss — if the agent keeps ignoring a rule, the file is probably too long.

**Three rules every rulebook in this course carries.** A *branch* rule (each task on its own
branch, never straight to `main`), an *evidence* rule (after every change, run the tests and paste
the output; the output is the proof, not a sentence), and an *off-limits* rule (never edit, delete
or skip a test; if one looks wrong, say so and stop). Each one closes a way the agent goes wrong
that you will meet today. The exact lines, and the ask that puts them in, are in the Week 4 steps.

**It is code.** It lives in git, it gets reviewed, it gets pruned. When the agent does something wrong, the fix is often a line here, not a longer prompt. *Would removing this line cause a mistake? If not, cut it.*

### The spec — the instructions for one task

The rulebook is the instructions for every task; the spec, the instructions for this one. You read one in
Class 3 (`specs/feature-1`) and you build from one today (`specs/feature-2`). From Block 2 you write
them, and the shape does not change: four headings, each doing one job for the agent.

| Section | What it is for the agent | Feature 2, for example |
|---|---|---|
| **Why** | The intent. When a line can be read two ways, this is how it picks the safe reading. | *As a flatmate, I want each expense tagged, so I can see where the money went.* |
| **What** | A checklist: one `- [ ]` line per thing that must be true. **One line, one test** — this is the judge, in prose. | `CATEGORIES` is exactly the five names · `expenses.csv` gets a `category` column · `add_expense` takes one · `category_totals(group_id)` |
| **Out of scope** | The fence for this task (the rulebook is the fence for all of them). | Editing a category later · custom categories · charts |
| **Done when** | The finish line in plain words. It goes in your ask today, and it is the sentence `/goal` takes. | Tests green · a category box on the form and totals on the page · `seed.py` runs · on the branch, pushed |

**Writing one.** Start from *Done when*: if you cannot say how you would know it is done, you are not
ready to delegate it. Then the *What* lines, each one checkable by a test you could describe. Keep
*Why* to two sentences. Put in *Out of scope* the thing the agent will be tempted to do (it will
refactor the neighbouring function; say no). One spec, one branch, one loop.

**Tests first, from the checklist.** The *What* lines become tests before any code is written:
one line, one test. This week they are written for you; from Block 2 you ask the agent for them
first, with no implementation, run them, and read them: do they check what the line says? Only
then the ask. A *Done when* line that no test covers is the line you check by clicking.

## 2 · The judge — define done before you build

**First, what a test actually is.** You have been running them since Class 3 without opening one.
Open `tests/test_feature_2.py` now: a test is a small function whose name is the *What* line, with a
sentence saying what it claims, and one word — `assert` — that does the work.

```python
def test_the_category_list_is_fixed():
    """The five categories, in this order, live in logic.CATEGORIES."""
    assert logic.CATEGORIES == ["rent", "groceries", "fun", "transport", "other"]
```

`assert` means *this must be true*. If it is, the test passes silently; if it is not, it stops and
prints what it expected against what it got — that is the red you will be reading all afternoon.
Nobody's opinion is involved, and it gives the same answer every time. The honest limit: a test only
checks what someone thought to write down, which is why green is not the end and why one *Done when*
line has no test at all.

**Something that can't lie.** The agent stops when the work *looks* done. Without a check it can run, you are the check, and every mistake waits for you to notice it. Give it something that answers pass or fail: today, the spec's *Done when* and the tests. Four red tests are the to-do list; green is *done*.

**Never move the goalposts.** The tests are the contract. An agent that edits a test to make it pass has cheated, not finished. The rule is in `AGENTS.md`; you enforce it.

**Evidence, not claims.** "All tests pass" is a sentence. The test output is evidence. Ask for the output, every time.

**Green is not the end.** The judge checks what it was told to check. After green, the human check: read the diff — did it change only what the task needed? — and click the app. If the app is wrong and the tests are green, the judge missed something. Write down what: that is a test that should exist.

## 3 · The loop

```
red  →  build  →  run the tests  →  read the failure  →  fix  →  run again  →  …  →  green  →  stop
```

This is the ReAct loop from section 0 with the tests written into it: *reason* — read the failure,
what does the last line say? · *act* — edit, then run the tests · *observe* — red, or green? · green
means stop, read the diff, click the app.

**One task per loop.** One bug, or one spec. Not "fix everything you see".

**Let it loop.** Tell the agent to run the tests after every change and keep going until green. It reads the failure and fixes it itself. Your job is to read the result, not to relay error messages.

**A stop condition.** Green, or a cap. Two corrections on the same failure and the thread is full of failed attempts: stop, read the failure yourself, start a **new thread** with a better prompt that says what you learned. A clean thread with a better prompt beats a long thread with corrections.

**The ask** is the same four parts every time: the task (one thing, named), the fence (the branch,
and what not to touch), the finish line (run the tests until every one passes) and the proof (paste
the output, list the files). Only the task and the branch change between tasks. The copy-ready
version is in the Week 4 steps.

**Where the loop lives.** Today it runs inside one Codex turn and you watch it. One level up, a
*script* runs it — you go and do something else.

**The Ralph loop.** Geoffrey Huntley published it in 2025, and the whole technique is one line:

```
while :; do cat PROMPT.md | claude-code ; done
```

Any agent goes in that pipe — the name in the original was just the one he happened to be using.
Anthropic later shipped it as an official Claude Code plugin (`ralph-loop`, December 2025), so
this is a practice you will meet at work, not a stunt. The plugin takes three inputs:

```
/ralph-loop "<the loop prompt above>" --max-iterations 20 --completion-promise "GREEN"
```

The prompt is the four-part ask. The cap stops it after that many runs. The phrase is how the
agent ends the loop early: it may only say it when it is true, and nothing checks, so the prompt
must say *the phrase only after every test passes*, and the cap is there because the plugin's own
advice is never to trust the phrase alone.
One difference is worth knowing: the plugin is a *Stop hook* that feeds the same prompt back into
the same conversation, so it does not get the fresh start described next. Only the shell loop does.

The same prompt, fed to a **fresh** agent, over and over. Each run starts with no memory of the last
one, so the agent cannot talk itself into a story about what it already did. The only state is
`PROMPT.md`, your `AGENTS.md`, and the repo as it now stands. Each run it picks the most important
undone thing, does it, and the tests say whether it worked. It keeps going until they pass.

It is named after a cartoon character who is cheerfully, relentlessly wrong and gets there anyway.
That is the honest description, and Huntley's own defence of it is that the technique is
"deterministically bad in an undeterministic world": it fails a lot, but in bounded, repeatable
ways, and something that cannot lie catches each one.

**Running it well.** Huntley's word for tuning the loop is *signs*: when a run does something
dumb you do not argue with it, you add a line to the prompt file and the next run reads it. The
standards that come with the technique are short. One task per run. A full implementation (his
prompt literally says *no placeholders*). A description of what *done* looks like, because that is
the only stop condition. Everything the agent needs to remember goes in a file — a spec folder, a
plan file, the rulebook — and a run may update them, since nothing else survives. The tests run
every iteration and every green is committed, so a bad run can be thrown away. A cap on runs,
because the official plugin's own advice is never to rely on the finish phrase alone. And then a
human reads all of it.

**The loop is a button now.** In 2026 both Claude Code and Codex ship the same idea as a command.
You give it a finish line in plain words and it keeps taking turns until that finish line holds:

```
/goal every test in tests/ passes, and nothing in tests/ changed
```

The sentence is the spec's *Done when*, with the fence in it. Who decides it holds differs by tool,
and the difference is standard 2 again. In **Codex**, the agent itself: its page says a goal should
name *what to achieve, what not to change, how to validate, and when to stop* — your four-part ask —
and that it stops "when it's confident it has reached the stopping condition". *Confident* is its own
word, so the goal has to say how it proves it. In **Claude Code**, a *second, smaller* model reads
the conversation after each turn and rules *not yet*, *met* or *impossible*. Neither one **can run
your tests** — they only read what the agent put on screen, which is exactly why "shown by the final
test output" belongs in the sentence. And everything that got automated here was the easy half:
nothing in it writes your rulebook, writes your spec, or decides what *done* means.

Using it is three habits, not a procedure: a red test first, never a goal without one; the
sentence names the proof and the fence and a cap; and when it stops, the human check as always.
The Codex desktop app has it built in; the sentence to paste is in the Week 4 steps.

**Why it needs the first two standards.** Nobody is watching. The rulebook is what keeps it inside the lines, and the judge is what tells it to stop. Get either wrong and
it will spend an hour going confidently in the wrong direction. That is why the rulebook and the
judge come first in this course: they are what makes walking away possible. Part II, in Block 3.

Sources: OpenAI, *Follow a goal* (Codex), learn.chatgpt.com/use-cases/follow-goals · ² Liu, N. F. et al. (2024). *Lost in the Middle: How Language Models Use Long Contexts.*
TACL 12, arxiv.org/abs/2307.03172 · ³ Chroma (2025), *Context Rot: How Increasing Input Tokens
Impacts LLM Performance*, trychroma.com/research/context-rot · ⁴ Rando, S. et al. (2025). *LongCodeBench:
Evaluating Coding LLMs at 1M Context Windows.* arxiv.org/abs/2505.07897 · Geoffrey Huntley,
*Ralph Wiggum as a "software engineer"*, ghuntley.com/ralph (2025) · Claude Code,
*Keep Claude working toward a goal*, code.claude.com/docs/en/goal.

---

¹ Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models.* ICLR 2023. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
