---
title: Agentic coding standards · Part I — rules, judge, loop
---

# Agentic coding standards · Part I

Three things every team that ships with AI agents does. They fit on one page and you will use all three today. First, one paragraph on what an agent is — because the standards are about controlling one.

## 0 · What an agent is

**A plain LLM writes.** ChatGPT in a browser predicts the next words of an answer. It has never seen your folder; it cannot open a file, run a test or check anything. You copy code in, you paste it out, you find out whether it works. When it says "the tests pass", that is a sentence that sounds right — nothing more.

**An agent acts.** Codex on your repo is the same kind of model **plus tools, in a loop**. The tools are few: *read* a file, *edit* a file, *run* a command. The loop is: act, see the result, decide the next action, until the job is done or it needs you.

**A tool call** is how it acts. Instead of prose, the model emits a request — `run: uv run pytest tests/test_feature_2.py`. The software around the model (Codex) executes it on your machine, after the approval prompt, and puts the output back into the conversation: `2 failed, 2 passed… AttributeError: no attribute CATEGORIES`. The model reads that like any other message and chooses the next call: `edit: logic.py`, then `run` again. When you watched Codex "run the tests, read the failure, edit again", you were watching tool calls, one after another.

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

**Why it matters here.** An agent can *run* the tests — but it can still *say* they passed without showing you. Tools give it hands; they don't make it honest. Hence the standards: a rulebook it reads before it acts, a judge whose output it cannot argue with, and a loop that knows when to stop.

## 1 · The rulebook — `AGENTS.md`

**What it is.** A README for agents. Codex reads it at the start of every session, before it reads anything else — so do Claude Code, Copilot, Cursor and twenty-odd other tools. It is the one place to say how *this* project is run and what the agent must never do. Your repo has had one since Class 2; open it.

**What goes in.** Only what the agent cannot work out by reading the code:

- commands it can't guess — `uv run streamlit run app.py`, `uv run pytest`, `uv run python seed.py`
- boundaries — *never edit `tests/`*, *don't touch `data/` by hand*, *one issue or spec per task*
- repo etiquette — *branch named after the spec*, *commit message says what changed*
- how to report — *paste the test output*, *list every file you changed*

**What stays out.** Anything it can read in the code. Long explanations. "Write clean code." Every extra line makes the important lines easier to miss — if the agent keeps ignoring a rule, the file is probably too long.

**It is code.** It lives in git, it gets reviewed, it gets pruned. When the agent does something wrong, the fix is often a line here, not a longer prompt. *Would removing this line cause a mistake? If not, cut it.*

## 2 · The judge — define done before you build

**Something that can't lie.** The agent stops when the work *looks* done. Without a check it can run, you are the check — and every mistake waits for you to notice it. Give it something that answers pass or fail: today, the spec's *Done when* and the tests. Four red tests are the to-do list; green is *done*.

**Never move the goalposts.** The tests are the contract. An agent that edits a test to make it pass has cheated, not finished. The rule is in `AGENTS.md`; you enforce it.

**Evidence, not claims.** "All tests pass" is a sentence. The test output is evidence. Ask for the output, every time.

**Green is not the end.** The judge checks what it was told to check. After green, the human check: read the diff — did it change only what the task needed? — and click the app. If the app is wrong and the tests are green, the judge missed something. Write down what: that is a test that should exist.

## 3 · The loop

```
red  →  build  →  run the tests  →  read the failure  →  fix  →  run again  →  …  →  green  →  stop
```

**One task per loop.** One bug, or one spec. Not "fix everything you see".

**Let it loop.** Tell the agent to run the tests after every change and keep going until green. It reads the failure and fixes it itself. Your job is to read the result, not to relay error messages.

**A stop condition.** Green, or a cap. Two corrections on the same failure and the thread is full of failed attempts: stop, read the failure yourself, start a **new thread** with a better prompt that says what you learned. A clean thread with a better prompt beats a long thread with corrections.

**The loop prompt** — paste, change the file names:

> Build `specs/<spec>.md`. Work only on the branch `<branch>`. After every change, run `uv run pytest tests/<test file>` and keep going until all tests pass. Do not edit anything in `tests/`. When they pass, paste the final test output and list every file you changed.

**Where the loop lives.** Today, inside one Codex turn — you watch it. The same idea, one level up, is a script that feeds the same prompt to the agent again and again until the judge says pass (the "Ralph loop": `while true; run agent with PROMPT.md; done`), or a tool feature that keeps the agent working until a goal you wrote is met. Same three parts every time: a rulebook, a judge, a loop. Part II, later in the course, is when you walk away from the laptop.

---

¹ Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. & Cao, Y. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models.* ICLR 2023. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
