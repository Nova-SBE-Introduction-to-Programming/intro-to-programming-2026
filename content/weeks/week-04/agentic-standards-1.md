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

**The three rules you add today.** A boundary, an evidence rule, and one thing that is off-limits:

```
- Build each spec on a branch named after it, e.g. feature-2-categories. Never commit a feature to main directly.
- After every change, run the tests for the task and paste the final output. The output is the proof, not a sentence.
- Never edit, delete or skip anything in tests/. If a test looks wrong, say so and stop.
```

**It is code.** It lives in git, it gets reviewed, it gets pruned. When the agent does something wrong, the fix is often a line here, not a longer prompt. *Would removing this line cause a mistake? If not, cut it.*

## 2 · The judge — define done before you build

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

**The loop prompt** — paste, change the file names:

> Build `specs/<spec>.md`. Work only on the branch `<branch>`. After every change, run `uv run pytest tests/<test file>` and keep going until all tests pass. Do not edit anything in `tests/`. When they pass, paste the final test output and list every file you changed.

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

After each turn a *second, smaller* model reads the conversation and rules: not yet, done, or
impossible. Two things about it are worth more than the command itself. The evaluator **cannot run
your tests** — it only reads what the agent put on screen, which is exactly why "paste the final
test output" belongs in your ask. And everything that got automated here was the easy half: nothing
in it writes your rulebook or decides what *done* means. On Codex it is off by default; turn it on
with `codex features enable goals`. Don't reach for it until you have a test that fails first.

**Why it needs the first two standards.** Nobody is watching. The rulebook is what keeps it inside the lines, and the judge is what tells it to stop. Get either wrong and
it will spend an hour going confidently in the wrong direction. That is why the rulebook and the
judge come first in this course: they are what makes walking away possible. Part II, in Block 3.

Sources: ² Liu, N. F. et al. (2024). *Lost in the Middle: How Language Models Use Long Contexts.*
TACL 12, arxiv.org/abs/2307.03172 · ³ Chroma (2025), *Context Rot: How Increasing Input Tokens
Impacts LLM Performance*, trychroma.com/research/context-rot · ⁴ Rando, S. et al. (2025). *LongCodeBench:
Evaluating Coding LLMs at 1M Context Windows.* arxiv.org/abs/2505.07897 · Geoffrey Huntley,
*Ralph Wiggum as a "software engineer"*, ghuntley.com/ralph (2025) · Claude Code,
*Keep Claude working toward a goal*, code.claude.com/docs/en/goal.

---

¹ Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models.* ICLR 2023. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
