# Class 2 — Meet the code · run sheet

90 min · practical · groups of 3–4, one screen per group · all local (no git, no GitHub). Tool: **Codex** (ChatGPT desktop app) + **uv**. Deck: 17 slides, **N** for notes. Demo on **SplitIt**; CRM groups follow in their own folder.

**Before class:** Moodle post ("install uv + the ChatGPT app — Setup, 15 min; on Cursor? keep it"). Demo laptop: fresh `splitit` unzipped, app running, Codex open on the folder, `uv run python seed.py` done.

## 0–2 · Open + the one change (slides 1–3)

- "Last week you drew it on paper. Today you open the app built from it." Four items today; sit with your group.
- **Codex, not Cursor.** Free, no verification, same on Mac/Windows. Reads the project, edits files, runs commands — *after asking you*. On Cursor already? Keep it today.
- Don't apologise, don't explain, don't migrate anyone.

## 2–27 · Get it running (slide 4)

Goal: every **group** has the app in a browser and Codex on the folder. Stragglers pair up.

Steps, said once: **0** not installed → Setup: uv one-liner, ChatGPT app, sign in, top-left → Codex · **1** course site → Week 2 · **2** ZIP → unzip into `Documents/nova` · **3** Codex → *Open folder* → the one with `app.py` · **4** terminal in the folder → `uv run streamlit run app.py` (first time downloads a minute) — or ask Codex *"Run the app"* and approve.

Then walk the room. Top fixes:

| Symptom | Fix |
|---|---|
| `uv` not recognised | Close terminal, open a new one |
| Nested `splitit/splitit` | Open the inner folder |
| First `uv run` slow | Downloading Python — wait, start the tour |
| Typed `python` / `pip` | Skipped uv. No Python on the machine, on purpose |
| No Codex in the app menu | Update app, restart, sign in. Else pair up |
| "Usage limit" | 5-hour window — pair up |
| Approves without reading | "What did it just ask to run?" — every time |
| Data is a mess | `uv run python seed.py` |

Checkpoint ~20: count browsers on `localhost:8501`. Move on at 27 regardless.

## 27–34 · Tour + three words (slides 5–7)

- Open **Casa da Lapa**, add an expense (Rita, €12, Pizza). Ask Codex: *"Show me the last line of data/expenses.csv."* → the new line. "That folder is the database."
- Nouns → `data/` · steps → `app.py` · decisions → `logic.py`.
- Point at what's broken — title says "Group 1", raw balances — **don't fix**.
- CRM, 2 min: pipeline → open a lead → *Move to next stage* → *"show me the last line of data/leads.csv."*
- **Three words:** folder (your computer) · project (Codex: folder + your threads) · repository (git: folder + history — next week). Same thing. Don't rename, move or nest it.

## 34–45 · The folder · six words · "where does X happen?" (slides 8–10)

- Ask Codex: *"List this folder, one sentence per item."* Read down slide 8. Then *"Show me COLUMNS in db.py"* — "these are the tables". No pytest today.
- Six words, one real line each via Codex: file (*first line of each .py*) · function (*def add_expense*) · call (*where app.py calls logic.add_expense*) · table (*first two lines of data/members.csv*) · entry point (*what runs first?*) · validation (*is_valid_name* — "remember this for Q6").
- Three ways: **follow the click** (button text in `app.py` → what it calls → stop at `db.py`) · **search** (*"Find the text 'Add expense' — file and line only"* — a match, not an opinion) · **ask, then verify** (make it show the line it names). Only the third can be wrong.

## 45–56 · The sheet + live Q4 (slides 11–12)

- *"Show me ONBOARDING.md."* Scroll once. Then *"Under question 1, write: 'SplitIt works out who owes whom… Verified: README.md.'"* → read the diff → accept. If Codex rewrites your sentence: "I didn't ask for that. No."
- **Q4 live, in this order:**
  1. *"Find the text 'Add expense' — file and line only."* → `app.py:79`. *"Show me lines 62–82 of app.py."* → inside `show_expenses` (62); line 81 calls `logic.add_expense`.
  2. *"Show me add_expense in logic.py."* → 54; calls `db.append_row` (64).
  3. *"Show me append_row in db.py."* → 42; writes one line to `data/expenses.csv`. Stop.
  4. New thread, cold: *"When I click Add expense, which function runs and which does it call to save it?"* Same three? Lines right?
  5. *"Under question 4, write: show_expenses (app.py 62, button 79) → logic.add_expense (logic.py 54) → db.append_row (db.py 42). Verified by reading the three lines."* Diff → accept.
- "A claim, where you saw it, what you did. That's every answer."
- CRM chain (say it): *Move to next stage* → `show_stage_buttons` (app.py 102/111/112) → `logic.move_to_next_stage` (106) → `save_lead` (76) → `db.save_table` (db.py 32).

## 56–58 · Good vs weak (slides 13–14)

Q2 "app.py" vs "app.py — what the run command starts; last line calls `main()`". Q5 "reused" vs "app.py 35, 46, 70; logic.py 87, 105". Q6 "error" vs "0 and −20 both saved, no message; `add_expense` has no check — compare `is_valid_name`". Q7 ask, then **do it**. Q8 comment vs code. Q9 wrong number → line → right number; **show the TA before/after**. Don't reveal the Q7 crash or the Q8 trap.

## 58–85 · Groups (slides 15–16)

Rotate who types · guess first, then ask · write where you checked · reproduce before you fix. Never answer a sheet question: *"What did the AI say — and did you check?"*

| You'll see | Do |
|---|---|
| Q7: page red, `KeyError: '8'` | "What did the AI say would happen?" Then `uv run python seed.py` |
| Q8: they paste the AI's explanation | "Read the comment on line 94. Now line 95. Is the comment true?" (No — the payer ate too. That comment *is* bug #1.) |
| Q9: Codex fixes four bugs at once | "Which one did you ask for? Say no. Ask for just that one." |
| Q9 done | Before/after: Jantar de Curso 30/−15/−15 → 20/−10/−10. CRM: "acme" 0 → 1 |
| "How do we save this for good?" | "Next week. That's git. Don't delete the folder." |
| Fast group | `issues/000` (SplitIt `group_title` logic.py 37 · CRM `count_by_stage` logic.py 45): reproduce + locate only. Or the TODO function: `settle_up` / `move_to_stage` — write what it should do |
| Stuck on an error (slide 16) | Read the last line, then the one above. Paste to the AI: *explain before you fix*. Neighbour. TA, error on screen |

## 85–90 · Wrap (slide 17)

Keep the folder (next week it becomes a repo). Finish the sheet, with locations. Every laptop runs the app — else forum + screenshot tonight. Read `specs/feature-1`. **Check-in: bug #1 before/after, per group, before they leave.**

### Answer key — SplitIt
Q1 who owes whom · Q2 `app.py`, last line 118 `main()` · Q3 `data/` groups/members/expenses.csv · Q4 `app.py` 62/79/81 → `logic.py` 54/64 → `db.py` 42 · Q5 `get_group_members` app 35, 46, 70; logic 87, 105 · Q6 no check in `add_expense` 54–64; cf. `is_valid_name` 42 · Q7 `remove_member` → KeyError · Q8 comment 94 vs line 95 · Q9 `logic.py` 95 `len(members) - 1` → `len(members)`, and debit **every** member (drop the `if` at 96–97); 30/−15/−15 → 20/−10/−10.

### Answer key — Tiny CRM
Q1 leads through new → contacted → proposal → won/lost · Q2 `app.py`, no `main()`: the block after "*this part runs on every click*" reads the sidebar and calls `show_*` · Q3 `data/` leads/notes/activities.csv · Q4 `app.py` 102/111/112 → `logic.py` 106 → `save_lead` 76 → `db.py` 32 · Q5 `get_lead` app 13, 71; logic 108, 124 · Q6 no validation anywhere — `add_lead` 59–73 and the form (150) both save empty/past · Q7 `delete_lead` (85) leaves notes in `notes.csv` (2 before, 2 after) · Q8 `overdue_followups` 179: skips won/lost and empty dates; date check is a *text* comparison · Q9 `search_leads` 50: case-sensitive; lower-case both sides; "acme" 0 → 1.
