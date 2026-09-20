# Class 2 — Meet the code · run sheet

90 minutes · practical · TA-run · groups of 3–4, one screen per group · everything local (no git, no GitHub, no forms).
Tool: **Codex** (ChatGPT desktop app, free plan) + **uv**. Students arrive having been told "Cursor" last week — expect installs in the room.

Deck: `content/weeks/week-02/class-2.html` (17 slides, press **N** for notes). Sheet: `ONBOARDING.md` inside each app.

---

## Before class (15 min)

- [ ] Post on Moodle: *"Before class: install uv and the ChatGPT desktop app — Setup on the course site, 15 minutes. Already on Cursor? Keep it."*
- [ ] On your own laptop: unzip a fresh `splitit.zip`, `uv run streamlit run app.py` — confirm it boots. Open the folder in Codex, ask one question. This is the demo machine.
- [ ] Have open, in tabs: course site → Week 2; the deck; SplitIt running on `localhost:8501`; Codex with the `splitit` project.
- [ ] Reset your demo data before the room arrives: `uv run python seed.py`.
- [ ] Know the two commands cold: Windows `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"` · macOS `curl -LsSf https://astral.sh/uv/install.sh | sh`.

---

## Run of show

| Min | Slide | What happens | Checkpoint |
|---|---|---|---|
| 0–1 | 1–2 | "Last week you drew it on paper. Today you open it." Today's four items. | — |
| 1–2 | 3 | **One change: Codex, not Cursor.** Say why (free, no verification, same on Mac/Win), move on. Cursor users keep Cursor today. | — |
| 2–27 | 4 | **Get it running.** Everyone: Setup → uv one-liner → ChatGPT app → sign in → Codex. Download ZIP, unzip into `Documents/nova`, *Open folder* in Codex, terminal in the folder, `uv run streamlit run app.py`. Walk the room with the triage table below. | **Every group has the app in a browser and Codex open on the folder.** Stuck laptops pair up; fix during group time. |
| 27–32 | 5–6 | **Product tour** (SplitIt on your screen; CRM groups follow in theirs). Open *Casa da Lapa*, add an expense, then ask Codex *"show me the last line of data/expenses.csv"* — a new line appeared. Point at what's visibly broken (title says "Group 2"; balances are raw numbers) — don't fix. | The "aha": the CSV grew. |
| 32–34 | 7 | **Three words.** Folder (your computer) · project (Codex) · repository (git, next week). One app, one folder — don't rename, move or nest. | — |
| 34–38 | 8 | **The folder.** Ask Codex *"list this folder, one sentence per item"*. Then *"show me COLUMNS in db.py"* — "these are the tables". No pytest today. | — |
| 38–43 | 9 | **Six words.** File · function · call · table · entry point · validation. One real example each, 20 s each, no definitions beyond the slide. | — |
| 43–45 | 10 | **"Where does X happen?"** — follow the click · search the exact words · ask the AI and verify. All three go through Codex chat; the difference is what you ask for. | — |
| 45–47 | 11 | **The sheet.** Ask Codex *"show ONBOARDING.md"*; scroll once. Show how an answer gets in: *"Under question 4, write: …"* → read the diff → accept. | — |
| 47–56 | 12 | **Live Q4** — script below. | Room has seen one complete answer with locations. |
| 56–58 | 13–14 | What a good answer looks like (2 min): claim + where you saw it + what you did. | — |
| 58–85 | 15–16 | **Groups, 27–30 min.** Rotate who types. Guess first, then ask. Write where you checked. Reproduce before you fix. Roam; never answer a sheet question — *"what did the AI say, and did you check?"* | **Each group shows the TA bug #1 before/after** (Q9). |
| 85–90 | 17 | Wrap: keep the folder (it becomes a repo next week), finish the sheet, app running on every laptop, read `specs/feature-1`. | — |

If the room is running by minute 15, give the 10 back to the groups.

---

## Live Q4 — script (SplitIt, 9 min)

*"Click Add expense. Which function runs? Which function does that call to save it?"*

1. **Follow the click.** To Codex: *"Find the text 'Add expense' in this project — file and line only."* → `app.py:79`, inside `show_expenses` (def at 62). *"Show me lines 62–82 of app.py."* The line under the button calls `logic.add_expense(...)` (81).
2. **Follow the call.** *"Show me add_expense in logic.py."* → def at 54; builds a row, calls `db.append_row("expenses", …)` (64).
3. **Stop at the database.** *"Show me append_row in db.py."* → def at 42; opens `data/expenses.csv`, writes one line.
4. **Now ask the AI the same question, cold:** *"When I click Add expense, which function runs and which function does that call to save it?"* Did it name the same three?
5. **Dictate the answer:** *"Under question 4 in ONBOARDING.md, write: show_expenses (app.py 62, button at 79) → logic.add_expense (logic.py 54) → db.append_row (db.py 42). Verified by reading the three lines."* Read the diff. Accept.

CRM equivalent for CRM groups: "Move to next stage" → `show_stage_buttons` (app.py 102, button 111, call 112) → `logic.move_to_next_stage` (logic.py 106) → `save_lead` (76, called at 113) → `db.save_table` (db.py 32).

---

## Triage table (minutes 2–27)

| Symptom | Fix |
|---|---|
| `uv` "not recognised" / "command not found" right after installing | Close the terminal, open a new one. Still nothing → run the one-liner again and read its last lines. |
| Windows: no *Open in Terminal* on right-click | Open Terminal from Start, type `cd `, paste the folder path from Explorer's address bar. |
| macOS: `cd` + drag didn't work | The path has spaces — the drag quotes it; if they typed it, wrap in quotes. |
| First `uv run` takes minutes | Normal on campus wifi (downloads Python + Streamlit ≈ 60 MB). Wait; start the tour. |
| Browser didn't open | Open `http://localhost:8501` by hand. Port taken → Streamlit says which port it used. |
| Unzipped into a nested `splitit/splitit` | Open the inner folder — the one with `app.py`. |
| Codex not in the ChatGPT app's top-left menu | App out of date → update, restart, sign in again. Still nothing → pair with a neighbour; sort it after class. |
| Codex asks to approve a command | Read it aloud with them, then approve. That's the habit. |
| "You've hit your usage limit" | 5-hour window. Pair up — one screen per group anyway. |
| Someone typed `python` / `pip` | They skipped uv. There is no Python on the machine on purpose. |
| Cursor from last week | Keep it. Everything on the sheet works there too. |
| Data is a mess | `uv run python seed.py` in the folder. |

---

## Answer key

### SplitIt

| Q | Answer | Where |
|---|---|---|
| 1 | Works out who owes whom in a group after people pay for things. | `README.md`, `app.py` |
| 2 | `app.py` — it's what `uv run streamlit run app.py` starts; last line (118) calls `main()`, which picks the screen. | `app.py:110–118` |
| 3 | `data/` — `groups.csv`, `members.csv`, `expenses.csv`. | `db.py` `COLUMNS` |
| 4 | `show_expenses` → `logic.add_expense` → `db.append_row`. | `app.py:62/79/81`, `logic.py:54/64`, `db.py:42` |
| 5 | `get_group_members` called at `app.py` 35, 46, 70 and `logic.py` 87, 105. One function, fixed once. | `logic.py:19` |
| 6 | `0` and `-20` both save, no message. `add_expense` (54–64) has no check. Compare `is_valid_name` (42), which members do have. | `logic.py:54`, `:42` |
| 7 | Removing João from *Jantar de Curso*: page goes red, `KeyError: '8'`. The AI usually says balances are recalculated without him. | `logic.py` `remove_member`; `issues/002` |
| 8 | The comment at 94 — *"the payer already paid, so the bill is split between everybody else"* — is exactly what the AI repeats. That comment **is** the bug: the payer ate too. | `logic.py:94–95` |
| 9 | **Bug #1.** *Jantar de Curso*, €30 dinner, 3 people: shows 30 / −15 / −15, should be 20 / −10 / −10. Line 95 divides by `len(members) - 1` and lines 96–97 skip the payer. Fix: `share = amount / len(members)` and debit **every** member (drop the `if`), then credit the payer the full amount. | `logic.py:95–98` |
| 10 | Open. Good ones: why is the payer excluded? why no amount check? what is `settle_up` supposed to do? | — |

Fast groups: `issues/000` — heading says "Group 2": `group_title` (`logic.py:37`) returns `"Group " + id`. `issues/002` — reproduce and locate only. Half-built: `settle_up` (`logic.py:130`, TODO).

### Tiny CRM

| Q | Answer | Where |
|---|---|---|
| 1 | Tracks sales leads through `new → contacted → proposal → won / lost`, with notes, activities and follow-up dates. | `README.md` |
| 2 | `app.py`. There is no `main()`: the block after `# this part runs on every click` reads the sidebar radio and calls `show_pipeline` / `show_lead` / `show_add_lead`. | `app.py:163–172` |
| 3 | `data/` — `leads.csv`, `notes.csv`, `activities.csv`. | `db.py` `COLUMNS` |
| 4 | `show_stage_buttons` → `logic.move_to_next_stage` → `save_lead` → `db.save_table`. | `app.py:102/111/112`, `logic.py:106/113/76`, `db.py:32` |
| 5 | `get_lead` called at `app.py` 13, 71 and `logic.py` 108, 124. | `logic.py:23` |
| 6 | Empty name and past follow-up date both save. `add_lead` (59–73) has no check, and neither does the form (`show_add_lead`, 150). There is no validation anywhere — the line that should stop you doesn't exist yet. | `logic.py:59`, `app.py:150` |
| 7 | Deleting a lead leaves its notes in `notes.csv` (2 before, 2 after). The AI usually says the notes go too. | `logic.py:85` `delete_lead`, `:132` `notes_for` |
| 8 | `overdue_followups` (179): the AI paraphrases the docstring. Glossed: won/lost are skipped, empty follow-up is skipped, the date check is a **text** comparison that only works because dates are stored `YYYY-MM-DD`. | `logic.py:179–194` |
| 9 | **Bug #1.** Search "acme" → 0, "Acme" → 1. `search_leads` (`logic.py:50`) compares text case-sensitively; fix by lower-casing both the query and the fields. | `logic.py:50–57` |
| 10 | Open. | — |

Fast groups: `issues/000` — pipeline counts one too many: `count_by_stage` (`logic.py:40`), `range(len(matching) + 1)` at 45. `issues/002` — reproduce and locate only. Half-built: `move_to_stage` (`logic.py:117`, TODO).

---

## Rules for the room

- **Never** answer a sheet question. Reply: *"What did the AI say — and did you check?"*
- Groups fix **bug #1 only**. If Codex offers to fix the rest ("I also noticed…"), that's a teaching moment: *say no*. (`AGENTS.md` tells it not to, but it will try.)
- No `pytest`, no git, no `.venv` explanations. Next week.
- Reproduce before fixing: see the wrong number, then the line, then the right number. Before/after is the check-in.
- Anyone asks "how do we save this for good?" → *"Next week. That's what git is for. Don't delete the folder."*

## Exit checklist per group

- [ ] App runs on every laptop in the group (or a named plan to fix it: Moodle forum + screenshot)
- [ ] `ONBOARDING.md` has answers with locations
- [ ] Bug #1 shown to the TA: before and after
- [ ] They know: keep the folder, read `specs/feature-1`
