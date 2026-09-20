# Class 2 — Meet the code · segment-by-segment script

Companion to `class-2-plan.md` (which has the triage table and the answer key). One section per row of the run of show. Times are cumulative minutes. Demo app: **SplitIt**; CRM groups follow in their own folder.

Legend: **Say** = talking points, not a script to read · **Do** = on the demo machine · **Ask Codex** = the exact prompt to type · **Watch** = what goes wrong here.

---

## 0–1 · Open (slides 1–2)

**Goal.** Frame the class in one sentence and show the four things on the menu.

**On screen.** Slide 1 → slide 2.

**Say.**
- "Last week you drew a workflow on paper. Today you open the app that was built from it."
- Four things today: the product tour, getting the repo running, six words to read code, and the question sheet — one question live, nine in your group.
- "Groups of 3–4, one screen per group. Sit with your group now."

**Do.** Nothing. Let them shuffle chairs while you talk.

**Watch.** Don't take questions yet — the install block absorbs them.

**Transition.** "One thing changed since last week."

---

## 1–2 · One change: Codex, not Cursor (slide 3)

**Goal.** Thirty seconds. Announce the tool, give the reason, remove the anxiety, move on.

**On screen.** Slide 3.

**Say.**
- "We use Codex. It's the coding side of ChatGPT — it lives inside the ChatGPT desktop app, on the free plan."
- Why: free, no student verification, identical on Mac and Windows. Install, sign in, done.
- What it does: reads your project, answers questions, edits files, runs commands — *after asking you first*.
- "Installed Cursor last week? Keep it today. Everything on the sheet works in either."

**Watch.** Don't apologise, don't explain the history, don't migrate Cursor users. Anyone who asks "which is better?" → "Today: whichever one is open on your laptop."

**Transition.** "Let's get it running. Twenty-five minutes; most of you are installing, that's expected."

---

## 2–27 · Get it running (slide 4)

**Goal.** Every group has (a) the app in a browser and (b) Codex open on the project folder. Not every *laptop* — every *group*. Stragglers pair up and fix during group time.

**On screen.** Slide 4, left up the whole time. Course site → Setup on your second screen or in a tab you can switch to.

**Say.** Walk the five steps once, slowly, pointing at the slide:
0. "Not installed? Course site → Setup. One line installs **uv** — it takes care of Python for you. Then the ChatGPT app, sign in, top-left menu → **Codex**."
1. "Course site → Week 2."
2. "Download your app's ZIP — SplitIt or Tiny CRM — and unzip it into a folder you'll find again. `Documents/nova` is a good address."
3. "Open the folder in Codex: *Open folder*, pick the one that contains `app.py`. Codex calls it a *project*."
4. "A terminal *in the folder*, then `uv run streamlit run app.py`. The first time it downloads for a minute. Or ask Codex *'Run the app'* and approve the command."

**Do.**
- Open Setup on screen and show the two things that trip people: *close the terminal and open a new one* after installing uv; *the folder that contains `app.py`*, not the one above it.
- Then **walk the room**. Don't stay at the front. Triage table is in `class-2-plan.md`; the top three by frequency: `uv` not recognised → new terminal · nested `splitit/splitit` → open the inner folder · first `uv run` slow → wait, it's downloading Python.

**Ask Codex** (for anyone who prefers it): *"Run the app."* → Codex proposes `uv run streamlit run app.py` → **read it with them**, approve. If uv is missing, Codex proposes the uv installer → same: read, approve.

**Watch.**
- Someone typing `python` or `pip` — they skipped uv. "There is no Python on this machine, on purpose. uv brings its own."
- Codex missing from the ChatGPT app menu → app out of date; update, restart, sign in again. If that fails, pair them; fix after class.
- "Usage limit" message → 5-hour window; pair up.
- Approving without reading. Each time you see it: "What did it just ask to run?" — that's the habit we're building.

**Checkpoint at minute ~20.** Count screens with a browser on `localhost:8501`. If all groups: move on early and give the time to the groups later. If not: pair the stuck laptop with a running one and move on at 27 regardless.

**Transition.** "Everyone can see the app? Good. Last week you drew this."

---

## 27–32 · Product tour (slides 5–6)

**Goal.** The reveal: the paper workflow is the software. Nouns → `data/`, steps → `app.py`, decisions → `logic.py`. And the "aha": adding an expense adds a line to a CSV file.

**On screen.** Your SplitIt in the browser, Codex beside it. Slide 5 up between.

**Do (SplitIt, 3 min).**
1. Open **Casa da Lapa**. "Four flatmates. Rent, groceries, internet, gas."
2. **Add an expense** — e.g. Rita paid €12 for "Pizza". Submit.
3. **Ask Codex:** *"Show me the last line of data/expenses.csv."* → a new line, with what you just typed. "That folder is the database. No server, no cloud. Three text files."
4. Point at slide 5: "Your nouns — group, member, expense — became `data/`. Your steps — add an expense, see who owes whom — became `app.py`. Your decisions — who's in the split, how much each — became `logic.py`."
5. Point at what's visibly broken, **without fixing anything**: the page title says "Group 1", not "Casa da Lapa"; the balances box shows raw numbers next to ids. "This company shipped with bugs. Users reported them. They're in `issues/`. You fix the first one today."

**Do (Tiny CRM, 2 min).** Slide 6. Open the pipeline, open a lead, **Move to next stage**, ask Codex *"show me the last line of data/leads.csv"* — same trick, the stage changed in the file. "Same skeleton, same three folders, different nouns."

**Say (slide 6).** "Two apps, one skeleton. Both have user-reported bugs in `issues/` and the same question sheet, `ONBOARDING.md`. I demo on SplitIt; CRM groups follow along in their own folder."

**Watch.** Resist fixing the title bug live — it's the fast-group extension.

**Transition.** "Three words you'll hear for the same thing."

---

## 32–34 · Three words (slide 7)

**Goal.** Defuse the folder / project / repository confusion before it happens. One minute.

**On screen.** Slide 7.

**Say.**
- "Your computer says **folder** — files in a directory, what you unzipped. Finder and Explorer only know this word."
- "Codex says **project** — a folder Codex has opened. Same files, plus the memory of your threads about them."
- "Git and GitHub say **repository** — a folder whose *history* is tracked: every change recorded, undoable, copyable to GitHub. Yours becomes one next week."
- "It's the same folder, seen by three tools. One app, one folder, one project, one repository. Don't rename it, don't move it, don't put it inside another one."

**Watch.** Someone asks about ZIP vs clone: "ZIP is a copy with no history. Clone is a copy that stays connected. Next week."

**Transition.** "What's in the folder?"

---

## 34–38 · The folder (slide 8)

**Goal.** Eight things, one sentence each, no syntax. Show that Codex is how you look at files today.

**On screen.** Slide 8, then Codex.

**Ask Codex:** *"List this folder, one sentence per item."* Read down the slide while it answers:
- `app.py` — the screens; what `uv run streamlit run app.py` starts
- `logic.py` — the rules
- `db.py` — reads and writes the CSV files; nothing else touches them
- `data/` — the live database; `seed/` is the pristine copy; `uv run python seed.py` restores it
- `tests/` — small programs that check the app. Next week.
- `issues/` — four bug reports from users. You fix #1 today.
- `specs/` — feature requests from the product manager. Next week.
- `ONBOARDING.md` — your question sheet. Answer inside the file.

**Ask Codex:** *"Show me COLUMNS in db.py."* → "These are the tables. Three of them. That's the whole schema."

**Watch.** No `pytest` today, even if Codex mentions it. If it offers to run tests: "Not today."

**Transition.** "Six words you need to read this."

---

## 38–43 · Six words (slide 9)

**Goal.** The minimum vocabulary to read the code. One real example each, 20 seconds each, no definitions beyond the slide.

**On screen.** Slide 9; flip to Codex for each example.

**Do.** For each word, ask Codex to show one real line, then name it:
| Word | Ask Codex | Say |
|---|---|---|
| File | *"Show me the first line of app.py, logic.py and db.py."* | "One file, one job." |
| Function | *"Show me `def add_expense` in logic.py."* | "A named block that does one thing. Read the name and the docstring first." |
| Call | *"Show me where app.py calls logic.add_expense."* | "One function using another. That's how the screen talks to the rules." |
| Table | *"Show me the first two lines of data/members.csv."* | "First line is the columns; each other line is a row." |
| Entry point | *"What runs first when I start the app?"* | "`app.py` — it's what the run command names." |
| Validation | *"Show me is_valid_name in logic.py."* | "A check before saving. Without it, bad data gets in. Remember this one for question 6." |

**Watch.** "Variable" and "loop" will come up when they read `compute_balances` — name them then, not now.

**Transition.** "The question every new engineer asks on day one."

---

## 43–45 · "Where does X happen?" (slide 10)

**Goal.** Three ways to find out — and the fact that with Codex, all three are things you *ask for*, and only one of them is an opinion.

**On screen.** Slide 10.

**Say.**
1. "**Follow the click.** Find the button's text in `app.py`. Read what it calls. Read what *that* calls. Stop when you reach `db.py`."
2. "**Search.** The exact words you see on screen. Ask Codex: *'Find the text "Add expense" in this project — file and line only.'* That's a match, not an opinion."
3. "**Ask the AI.** *'Explain…'* — then **verify**: make it show the line it names, and read it."
- "All three go through the chat today. The difference is what you ask for: *show me*, *find the text*, *explain*. Only the third one can be wrong."

**Transition.** "Here's the sheet you'll fill in."

---

## 45–47 · The sheet (slide 11)

**Goal.** Show the sheet once and, crucially, show how an answer gets *into the file* through Codex.

**On screen.** Slide 11, then Codex.

**Ask Codex:** *"Show me ONBOARDING.md."* Scroll through once: "Six about the code, four about checking the AI. Every answer says **where you checked** — a file and line, or what you clicked."

**Ask Codex:** *"Under question 1 in ONBOARDING.md, write: 'SplitIt works out who owes whom in a group after people pay for things. Verified: README.md, first paragraph.'"* → Codex shows the change → **read the diff aloud** → accept. "That's how you answer. Tell it what to write and where. Read what it changed. Then accept."

**Watch.** Codex may "improve" the wording. Point that out: "It changed my sentence. I didn't ask for that. Say no and repeat the instruction." (Good rehearsal for group time.)

**Transition.** "Let's do question 4 together, properly."

---

## 47–56 · Live Q4 (slide 12)

**Goal.** One complete answer, with locations, built in front of them — then the AI's version compared against it.

**On screen.** Slide 12 at first; then Codex full-screen.

*"Click Add expense. Which function runs? Which function does that call to save it?"*

**Do, in this exact order:**
1. **Follow the click.** Ask Codex: *"Find the text 'Add expense' in this project — file and line only."* → `app.py:79`. Ask: *"Show me lines 62–82 of app.py."* → we're inside `show_expenses` (def at 62); the line under the button calls `logic.add_expense(...)` (81). "Step one done. Screen → rule."
2. **Follow the call.** Ask: *"Show me add_expense in logic.py."* → def at 54. It builds a row and calls `db.append_row("expenses", …)` (64). "Rule → storage."
3. **Stop at the database.** Ask: *"Show me append_row in db.py."* → def at 42; opens `data/expenses.csv`, writes one line. "We've hit the file. Stop."
4. **Now ask the AI cold.** New thread. Ask: *"When I click Add expense, which function runs, and which function does that call to save it?"* Compare with what we just read. Did it name the same three? Did it give line numbers? Are they right?
5. **Dictate the answer.** Ask: *"Under question 4 in ONBOARDING.md, write: show_expenses (app.py 62, button at line 79) → logic.add_expense (logic.py 54) → db.append_row (db.py 42). Verified by reading the three lines."* Read the diff. Accept.

**Say, at the end.** "That's the pattern for every question: a claim, where you saw it, what you did. The AI is allowed everywhere. You can't ship what you can't explain."

**For CRM groups** (say it, don't demo it): "Move to next stage" → `show_stage_buttons` (app.py 102, button 111, call 112) → `logic.move_to_next_stage` (logic.py 106) → `save_lead` (76) → `db.save_table` (db.py 32). Same three hops.

**Watch.** If Codex's cold answer is *better* than yours (it may include lines you skipped) — great, say so: "It's right. I checked. That's the point: not that it's wrong, that you *know* whether it's right."

**Transition.** "Two minutes on what a good answer looks like."

---

## 56–58 · Good vs weak answers (slides 13–14)

**Goal.** Calibrate before they start. Two minutes, no more.

**On screen.** Slide 13, then 14.

**Say (13, "Ask the code").**
- Q2 — weak: "app.py". Good: "app.py — it's what the run command starts, and the last line calls `main()`, which picks the screen."
- Q5 — weak: "get_group_members, it's reused". Good: "called at app.py 35, 46, 70 and logic.py 87, 105. Fix it once, it's right everywhere."
- Q6 — weak: "it gives an error". Good: "I added 0 and −20: both saved, no message. `add_expense` has no check — compare `is_valid_name`, which members do have."
- "The pattern: a claim + where you saw it + what you did."

**Say (14, "Verify the AI").**
- Q7 — ask, paste the AI's answer, **then do it**: remove João from Jantar de Curso. Write what actually happened.
- Q8 — make it explain `compute_balances`. Compare the comment inside the function with what the code does. Where did the AI just repeat the comment?
- Q9 — bug #1: see the wrong number on screen, find the line, fix it, see the right number. **Show the TA before and after.**
- "Broke the data? `uv run python seed.py` puts it back."

**Watch.** Don't reveal the Q7 crash or the Q8 trap. Q7 is the moment of the class: the AI answers confidently, the app goes red. Let them discover it.

**Transition.** "Thirty minutes. Go."

---

## 58–85 · Groups (slides 15–16)

**Goal.** The sheet gets answered *with locations*; bug #1 gets fixed and shown; nobody sits idle behind a broken laptop.

**On screen.** Slide 15; flip to 16 when the first group is stuck on an error.

**Say (15).** "One screen, everyone steers. Rotate who types. Guess first, then ask the AI — compare. Write where you checked. Reproduce the bug before you fix it."

**Do.** Roam. Never answer a sheet question. The only reply is: *"What did the AI say — and did you check?"*

**What you'll see, and what to do:**
- Q7: page goes red, `KeyError: '8'`. Don't rescue immediately. "What did the AI say would happen? … And what happened?" Then `uv run python seed.py`.
- Q8: they paste the AI's explanation. "Read the comment on line 94. Now read line 95. Is the comment true?" (It isn't — the payer ate too. That comment *is* bug #1.)
- Q9: they ask Codex to fix it and it fixes **four bugs**. This will happen. "Which one did you ask for? Say no. Ask again for just that one." `AGENTS.md` tells Codex to change one thing at a time, but it will still try.
- Q9 done: **before/after on the screen** is the check-in. Jantar de Curso: 30 / −15 / −15 → 20 / −10 / −10. CRM: "acme" finds 0 → finds 1.
- Q10: push for real questions. "Why is the payer excluded?" beats "was this hard to write?"
- A group asks "how do we save this for good?" → "Next week. That's what git is for. Don't delete the folder."
- Fast groups: `issues/000` (SplitIt: the "Group 2" title, `group_title` in `logic.py:37`; CRM: pipeline counts one too many, `count_by_stage`, `logic.py:45`) — reproduce and locate, no need to fix. Or find the half-built function (`settle_up` / `move_to_stage`, docstring + TODO) and write what it's meant to do.

**Slide 16, when needed.** "Stuck? In this order: read the error — last line says what, the line above says where. Paste it to the AI and ask it to *explain* before it fixes anything. Ask the group next to you. Ask the TA, with the error on screen."

**Watch.**
- The person typing is always the same person. Rotate them yourself: "Swap."
- Answers without locations. "Where?" Every time.
- Broken laptops: the group works on the running one; the broken one pairs with a neighbour for the last ten minutes.

**Transition (85).** "Two minutes. Save your sheet. Look up."

---

## 85–90 · Wrap (slide 17)

**Goal.** Four instructions, then out.

**On screen.** Slide 17.

**Say.**
1. "**Keep the folder.** Don't delete it, don't rename it, don't move it. Next week it becomes a repository, and your sheet and your bug fix become your first commit."
2. "**Finish the sheet.** Every answer with a location."
3. "**Every laptop runs the app.** Still stuck? Moodle forum, with a screenshot."
4. "**Read `specs/feature-1`.** That's what gets built live in Class 3, with tests and a branch."

**Do.** Before they leave, each group shows you bug #1 before/after if they haven't yet. That's the only check-in there is.

**Watch.** Don't let the room leave with a broken laptop and no plan. "Forum + screenshot tonight" is the plan.
