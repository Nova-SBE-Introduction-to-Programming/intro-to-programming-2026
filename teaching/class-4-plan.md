# Class 4 — Rules, judge, loop · TA plan and answer key

90 min · practical · 2026-09-22 · deck `content/weeks/week-04/class-4.html` (15 slides, N for notes) · page `weeks/week-04` · handout `agentic-standards-1.md`.

## Why the class is shaped this way

- **Worked example → faded scaffolding.** Class 3 was the fully worked example (feature 1 built live, every decision narrated). Class 4 removes the narration and leaves a scaffold: a prompt template with four named parts, a checklist, a failure table. Students do the whole loop themselves; the TA only asks questions.
- **Tests as the feedback channel.** The "Prompt Problems" line of CS-education research (Denny, Leinonen, Prather et al.; 726-student study, arXiv 2410.03063) shows novices — especially those who find syntax hard — learn well when the task is *write the prompt, let the tests judge, iterate*, averaging 3–4 attempts. That is exactly the loop, so the class makes the loop explicit instead of leaving it implicit.
- **PRIMM mapped onto agentic work.** Predict (read the spec + tests: which files change?) → Run (the red tests) → Investigate (read the diff) → Modify (fix what the judge reports) → Make (the feature). The deck's live kick-off follows that order.
- **Industry standards, not tool features.** The three things every agentic team has — a rulebook (`AGENTS.md`, agents.md convention; Anthropic's CLAUDE.md guidance says the same: short, only what can't be inferred, in git), a judge (Anthropic: *"give the agent a way to verify its work… the loop closes on its own"*; Huntley: *check against something that can't lie*), and a loop (Ralph: one task per loop, a stop condition, "no placeholder implementations"). Tool-specific forms (Claude Code `/goal`, Stop hooks, `ralph-loop`) are mentioned once as "the same idea one level up" and left for Part II.
- **Name the thing before the rules.** Two slides define *agent* by contrast (a chat model writes; an agent = the same model + tools + a loop, acts) and *tool call* concretely (request → executed after approval → output back in the conversation → next call), anchored in what students already saw Codex do. Without this, "the loop" is a metaphor; with it, it's a description of the tool-call chain they watch on stage.
- **Rules come from failures.** The retro converts today's worst agent behaviour into one `AGENTS.md` line with the reason in the commit message. That's the meta-skill: the rulebook grows from observation, not from longer prompts.

## Run of show

| Min | Slide | What | Checkpoint |
|---|---|---|---|
| 0–5 | 3 | Check-in: GitHub page shows feature-1 branch + merged PR. Pull main, run feature-1 tests. | TA has the list of who isn't done |
| 5–11 | 4–5 | What an agent is (chat model vs agent: same model + tools + loop) and what a tool call is (request → executed after approval → output back into the conversation → next call). Tie to Class 2 ("show me the last line of expenses.csv") and to what they'll see in the kick-off. | — |
| 11–21 | 6–7 | Standard 1, the rulebook. Live: ask Codex *"What does AGENTS.md tell you to do?"* (proof it reads it). Add the three lines via Codex, read the diff, commit, push. Everyone does the same. | Every laptop: `AGENTS.md` commit pushed |
| 21–26 | 8 | Standard 2, the judge. Run `uv run pytest tests/test_feature_2.py` → 4 red; match tests to the spec checklist. | — |
| 26–31 | 9–10 | Standard 3, the loop + the loop prompt (task · boundary · judge · evidence). | — |
| 31–44 | 11 | Feature 2 kick-off live on SplitIt: branch → red → **new thread** → paste prompt → watch it loop → green → read the diff → click the app → commit/push/PR/merge. Let it get something wrong. | Room has seen one full loop and one "green but wrong" |
| 44–80 | 12–13 | Your turn: bug (on main) then feature 2 (on branch). Roam: "did you ask for the output?", "did you read the diff?". | Bug test green + pushed; feature 2 green on branch |
| 80–87 | 14 | Retro: worst thing the agent did → one rule → commit to `AGENTS.md` with the reason. Three read out. | Every laptop: second `AGENTS.md` commit |
| 87–90 | 15 | Wrap: finish feature 2, rule committed, push. Block 2 next. | — |

## Exact prompts for the live part

- Proof of the rulebook: *"What does AGENTS.md tell you to do?"*
- Adding the lines: *"Under 'How to answer' in AGENTS.md, add these three lines: …"* (from slide 5). Read the diff. Accept.
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
