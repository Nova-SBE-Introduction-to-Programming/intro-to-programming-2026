# Class 4 — Rules, judge, loop · TA plan and answer key

90 min · practical · 2026-09-22 · deck `content/weeks/week-04/class-4.pdf` (31 slides in four acts; LaTeX source in
`decks/`, rebuild with `decks/build.sh`) · speaker notes `teaching/class-4-notes.pdf` (slide left, notes right —
open it on the second screen in any PDF presenter) · page `weeks/week-04` · handout `agentic-standards-1.md`.

## Why the class is shaped this way

- **The slides carry concepts; the page carries commands.** Nothing on a slide is meant to be typed: a
  projected command is unreadable from the back row, and copying it is not the skill. Every literal — the
  loop prompt, the three `AGENTS.md` rules, file and test names, the `uv` invocations — lives on the Week 4
  page and in the handout, which students have open. The speaker notes carry them for you.

- **Worked example → faded scaffolding.** Class 3 was the fully worked example (feature 1 built live, every decision narrated). Class 4 removes the narration and leaves a scaffold: a prompt template with four named parts, a checklist, a failure table. Students do the whole loop themselves; the TA only asks questions.
- **Tests as the feedback channel.** The "Prompt Problems" line of CS-education research (Denny, Leinonen, Prather et al.; 726-student study, arXiv 2410.03063) shows novices — especially those who find syntax hard — learn well when the task is *write the prompt, let the tests judge, iterate*, averaging 3–4 attempts. That is exactly the loop, so the class makes the loop explicit instead of leaving it implicit.
- **PRIMM mapped onto agentic work.** Predict (read the spec + tests: which files change?) → Run (the red tests) → Investigate (read the diff) → Modify (fix what the judge reports) → Make (the feature). The deck's live kick-off follows that order.
- **Industry standards, not tool features.** The three things every agentic team has — a rulebook (`AGENTS.md`, agents.md convention; Anthropic's CLAUDE.md guidance says the same: short, only what can't be inferred, in git), a judge (Anthropic: *"give the agent a way to verify its work… the loop closes on its own"*; Huntley: *check against something that can't lie*), and a loop (Ralph: one task per loop, a stop condition, "no placeholder implementations"). Tool-specific forms (Claude Code `/goal`, Stop hooks, `ralph-loop`) are mentioned once as "the same idea one level up" and left for Part II.
- **Name the thing before the rules.** Two slides define *agent* by contrast (a chat model writes; an agent = the same model + tools + a loop, acts) and *tool call* concretely (request → executed after approval → output back in the conversation → next call), anchored in what students already saw Codex do. Without this, "the loop" is a metaphor; with it, it's a description of the tool-call chain they watch on stage.
- **One tool call is shown in full, as a transcript.** The sequence diagram gives the choreography; the slide after
  it gives the payloads — the structured request the model emits, the approval prompt, the file's own line pasted
  back, the answer. It is the slide that turns "the AI reads your files" from magic into mechanism, and it sets up
  standard 2: a thing that can only ask, and can only see what is handed back, is a thing you can verify.
- **Tools and reasoning get a slide each, before the loop that combines them.** "Agent = model + tools + a loop"
  is a slogan until they see what a tool buys: the top lane of the diagram is exactly what they did in Class 2 with
  a browser chat — the model advised, they were the hands, and they were the only one who found out it was wrong.
  Reasoning is shown on their own SplitIt balances bug: answer at once and you get a plausible guess; work it out
  and you get line 95. ReAct then lands in one breath, because it is just those two in a loop.
- **The pre-history earns its place because it takes the magic out.** Students arrive assuming all of this
  appeared in 2022. Three slides put it where it belongs: the perceptron (1958), the proof that one layer cannot
  learn XOR and the winter that followed (1969), backpropagation (1986), LSTM (1997), the Transformer (2017) —
  and then the thing that actually changed, which is not an idea at all. Cheap parallel arithmetic (CUDA 2007,
  AlexNet 2012) and a scraped web (Common Crawl) arrived at the same time, and the ideas had been waiting. Two
  minutes buys a model that is engineering rather than magic — and therefore something you can set rules for, which
  is the whole of Act 2. It also corrects an attribution students usually meet the wrong way round: Minsky and
  Papert wrote the critique that *motivated* multi-layer networks; they did not invent them.
- **Git is one continuous story, not three rules.** The same `gitGraph` is drawn five times, each slide one move
  further on, and the frames are aligned on the `main` badge so the graph holds still and only grows — it reads as a
  build, not as five diagrams. A branch is a spatial idea; a sentence about it is not.
- **It is framed the way this audience already thinks.** `main` is the approved version, a branch is your draft,
  commits are checkpoints, a pull request is sending it for review, a merge is the sign-off. Nothing about git is
  new to someone who has ever had a model reviewed before it went out — only the vocabulary is. The two habits that
  usually get announced as rules (name the branch after the job; keep commits small) fall out of slides 2 and 3
  instead.
- **Rules come from failures.** The retro converts today's worst agent behaviour into one `AGENTS.md` line with the reason in the commit message. That's the meta-skill: the rulebook grows from observation, not from longer prompts.

## Run of show

Four acts, each opened by its kicker colour: **teal** logistics · **violet** what an agent is ·
**amber/coral** the three standards · **blue** git. Two divider slides (`3` and `git`) mark the turns.

| Min | Slides | What | Checkpoint |
|---|---|---|---|
| 0–5 | 1–3 | Open, agenda, check-in: GitHub page shows the feature-1 branch and a merged PR. | TA has the list of who is behind |
| 5–22 | 4–12 | **Act 1 — what an agent is.** Chat model vs agent · what a tool is · the tool-call choreography · **one exchange in full** (go slowly — it demystifies everything) · what reasoning is · ReAct and the harness · the long run-up, 1958–2017 · what actually changed: compute and text · eight years in one picture. | — |
| 22–23 | 13 | Divider: **three standards**. | — |
| 23–36 | 14–19 | **Act 2 — the standards.** Rulebook (+ live: add three rules, commit) · judge (run the red tests on stage) · loop · the four parts of an ask · Ralph, 30 s. | Every laptop: an `AGENTS.md` commit pushed |
| 36–37 | 20 | Divider: **git**. | — |
| 37–42 | 21–26 | **Act 3 — git, as one story.** The graph grows by one move per slide: `main` → branch → commit → second commit (`main` has not moved) → push and pull request → merge, approved. About forty seconds each — it is a build, so do not narrate it twice. | — |
| 42–52 | 27 | **Live kick-off.** Branch → red → new thread → paste the ask → watch it loop → read the diff → click the app → merge. Let it get something wrong. | Room has seen one full loop and one "green but wrong" |
| 52–82 | 28–29 | **Your turn.** Bug on `main`, then feature 2 on a branch. | Bug test green and pushed; feature 2 green on its branch |
| 82–88 | 30 | **Retro.** Worst agent behaviour → one rule → commit with the reason. Three read out. | Every laptop: a second `AGENTS.md` commit |
| 88–90 | 31 | Wrap. | — |

Act 1 and Act 3 are the flex, and they trade: the three history slides cost two minutes, and git gives them up —
six slides of one growing graph run fast. The 30 minutes of hands-on at the end do not move. If the room is quick,
the minutes belong to *your turn*, not to you.

## Exact prompts for the live part

- Proof of the rulebook: *"What does AGENTS.md tell you to do?"*
- Adding the rules: *"Under 'How to answer' in AGENTS.md, add these three lines: …"* — the verbatim wording is on the Week 4 page and in the handout (slide 15 shows only the three concepts: boundary, evidence, off-limits). Read the diff. Accept.
- The loop prompt (new thread): *"Build `specs/feature-2-categories.md`. Work only on the branch `feature-2-categories`. After every change, run `uv run pytest tests/test_feature_2.py` and keep going until all four tests pass. Do not edit anything in `tests/`. When they pass, paste the final test output and list every file you changed."*
- After green: *"Show me the diff of every file you changed."* Then, in the browser: Add expense → category box? Group page → totals?

## Answer key

### SplitIt

**Bug 002 — removing a member crashes** (`test_bug_002_removing_a_member_removes_their_expenses`). The test demands a helper `remove_member_expenses` (read the assertion message) and that `remove_member` calls it. Fix in `logic.py`: new function that keeps every expense whose `payer_id` differs and saves the table; `remove_member` calls it first, then removes the member. `expense_rows(JANTAR)` returns `[]` afterwards. One function + one line.

**Feature 2 — categories** (4 tests). Verified green with this minimal change:
- `logic.py`: `CATEGORIES = ["rent", "groceries", "fun", "transport", "other"]`; `add_expense(..., category="other")` writes `"category"` into the row; `category_totals(group_id)` sums `float(amount)` per category from `get_group_expenses`, skipping empty ones (`{"fun": 38.5, "transport": 12.0}` in the test).
- `db.py`: `COLUMNS["expenses"]` gets `"category"` at the end.
- `seed/expenses.csv`: new column on every line; Zé dos Cornos = `fun`. Then **`uv run python seed.py`** — otherwise `data/` has no column and the app crashes on load *while the tests stay green* (tests copy from `seed/`). That is the planned "green is not the end" moment.
- `app.py` (untested): a `st.selectbox("Category", logic.CATEGORIES)` in the Add expense form, passed to `add_expense`; a short list of `category: total` on the group page. Only clicking catches a missing one.

### Tiny CRM

**Bug 003 — "Won this month" always 0** (`test_003_mark_won_stamps_closed_on_and_counts`). Two changes, and the second is the twist:
1. `mark_won` (logic.py 122): set `lead["closed_on"] = today_text()` before `save_lead`.
2. `won_this_month` (196): the branch `if lead["closed_on"] == "": return 0` gives up on the whole count when *any* won lead has no date — and the seed has **five** won leads with empty `closed_on`. Change `return 0` to `continue` (the comment above it is wrong on purpose). Verified: test green only with both.

**Feature 2 — conversion by source** (4 tests). Verified green: `conversion_by_source()` loops `SOURCES` (`["referral", "website", "linkedin", "event"]`), counts `total` and `won` from `all_leads()`, `rate = round(won / total * 100, 1) if total else 0`, returns dicts in `SOURCES` order. Untested: the **Sources** section on the Pipeline page with a `%` sign — click to check.

## What the agent typically gets wrong (feed the retro)

- Forgets `uv run python seed.py` after editing `seed/` → app crashes, tests green.
- Edits `data/*.csv` directly instead of `seed/` + seed.py.
- No selectbox / no page section — nothing tests `app.py`.
- Fixes bug 003 with the stamp only, then "fixes" the test's expectation — catch it: *never edit tests/*.
- Fixes issues 003 (SplitIt shares) or other red tests while at it → "one task per loop", discard.
- Claims green without output → ask for the output.
Good retro rules: *"Run seed.py after changing seed/."* · *"Never write to data/ by hand."* · *"Show the diff before committing."* · *"Paste the test output, don't summarise it."*

## Rules for the room

Never answer a red test — *"what does the last line say?"* Never relay an error to the agent for them — they paste it. Bug on `main`, feature on its branch, PR before merge. Feature 1 not merged → that first; feature 2 becomes homework.
