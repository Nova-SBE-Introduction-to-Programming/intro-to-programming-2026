# Class 4 — Rules, judge, loop · TA plan and answer key

90 min · practical · 2026-09-22 · deck `content/weeks/week-04/class-4.pdf` (39 slides in four acts; LaTeX source in
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
- **Git comes first.** It is what they just looked at on their own GitHub page, it is what last week
  was about, and every later slide (branch, judge, push, merge) leans on its vocabulary. Putting it
  before the agent material also means the class opens on something concrete and already familiar
  rather than on an abstraction.
- **One tool call is shown in full, as a transcript.** The stack gives the choreography; the slide
  after it gives the payloads — the structured request the model emits, the approval prompt, the
  file's own line pasted back, the answer. It is the slide that turns "the AI reads your files" from
  magic into mechanism, and it sets up standard 2: a thing that can only ask, and can only see what
  is handed back, is a thing you can verify.
- **The model-to-agent stack is one picture built in four moves.** *A language model*: you and the
  model, text both ways, and a dashed empty circle where the rest will go. *Tools*: a laptop with
  read · edit · run, and the result arrow pointing back at the **model**, not at you — that arrow
  is the whole slide. *An agent*: one more arrow, "again, until done", and the equation. *The
  harness*: the box that was always there gets drawn and named, with the "may I?" gate on its edge
  and its three jobs along the bottom. Same canvas every time, so the LLM / tools / agent / harness
  distinction is spatial: each word is a region of the same picture.
- **History comes before the stack, and is two slides.** Students arrive assuming all of this
  appeared in 2022. The run-up (1958–2017) puts the ideas where they belong — the perceptron, the
  XOR critique and the winter, backpropagation, LSTM, the Transformer — and its caption names what
  was actually missing: cheap parallel arithmetic (CUDA 2007, AlexNet 2012) and a scraped web
  (Common Crawl). The second slide is 2018 onwards, with a parameter row under the stops (117M → 1.5B → 175B, then "not published": the size story ends, the job story continues), and its last line hands off: "the next four
  slides are that second change." Two minutes buys a model that is engineering rather than magic —
  and therefore something you can set rules for. It also corrects an attribution students meet the
  wrong way round: Minsky and Papert wrote the critique that *motivated* multi-layer networks; they
  did not invent them.
- **Git is one continuous story, not three rules.** One TikZ macro draws the same commit graph five times, each
  slide one move further on. Because it is literally the same picture at five stages, nothing shifts or rescales
  between slides: it reads as a build, not as five diagrams. A branch is a spatial idea; a sentence about it is not.
- **`local` and `remote` get their own picture, with three machines in it.** Slide 9 is the one place
  the story leaves the graph: GitHub as a cloud across the top, your laptop and a teammate's laptop
  under it, each screen showing the history it holds. Your branch is on your screen and in the
  cloud; on the teammate's screen it is a dashed ghost labelled "not until they pull". That
  asymmetry is what *remote* means — one shared copy, and every laptop has to push to it and pull
  from it — and it is visible rather than asserted. Staging is deliberately absent: GitHub Desktop
  collapses it into the file checkboxes, and naming a fourth place buys nothing today. If someone
  asks, that is what the checkbox column is.
- **It is framed the way this audience already thinks.** `main` is the approved version, a branch is your draft,
  commits are checkpoints, a pull request is sending it for review, a merge is the sign-off. Nothing about git is
  new to someone who has ever had a model reviewed before it went out — only the vocabulary is. The two habits that
  usually get announced as rules (name the branch after the job; keep commits small) fall out of slides 2 and 3
  instead.
- **Reasoning gets shown, not described.** Slide 19 is a chat mock-up where it earns its keep. The
  ask — *"make it so Ana doesn't owe anything"* — is genuinely ambiguous, and every reading of it
  moves somebody's money. Read it aloud and stop: the room will give you at least two readings,
  which is the point. Without the thinking block you get one of them at random and no way to tell
  which; with it you get the safe one plus a stated assumption you can overrule. The thinking block
  is styled as the odd one out — no fill, dashed rule, italic — because it is not a message anyone
  sent. The definition ("worked out first, then answered") is in the kicker; the lineage is in the
  notes.
- **ReAct is drawn once and reused, so it reads as the architecture rather than a diagram.** The ring
  — reason, act, observe, the "not yet" return underneath and the "done" exit to the right — is
  slide 20 in Act 2 and slide 27 in Act 3 with the tests written into it: *read the failure* ·
  *edit, then run the tests* · *red, or green?* · *green: read the diff, click the app*. The bridge
  at the `3` divider is that the ring has three places where you get a say: what it reads before
  the first thought (the rulebook), what it observes (the judge), and when the return arrow stops
  (the loop). The standards are the ring, configured.
- **Context is a bar; context rot is two measurements, shown as measurements.** The context slide
  draws the window as a fixed-width bar filling up — the rulebook a thin sliver at the left, the
  files and command output most of it — so "the oldest part goes first" is visible. Context rot
  then shows the evidence rather than a metaphor: Liu et al.'s Figure 1 as published (TACL 2024,
  CC BY) — twenty documents, the answer moved through them, accuracy sagging in the middle to
  *below* the closed-book line, i.e. worse than no documents at all — and Chroma's 2025 result on
  four current models copying a list of words, redrawn from their figure because the PNG's fonts
  vanish at slide size: every line falls from a few hundred tokens on. The kicker carries the
  consequence ("so: new thread, or compact"). It explains why "start a new thread after twice
  round" is standard 3, and why compaction is not the tool being lazy: it discards the part the
  model was using worst and keeps the two parts it uses best. If you have the screen, run
  `/context` then `/compact` and let them watch the bar drop.
- **Ralph gets four slides because the picture is the argument.** The crowd photo first and alone:
  not one agent getting better, a queue of identical beginners. Then one canvas grown three
  times, like the git graph. *One run*: prompt → fresh agent → repo → tests, every part something
  they already have from this act. *Nobody is watching*: the one-liner on top (the deck's one
  deliberate command on a slide — `while :; do cat PROMPT.md | claude-code ; done` is the
  punchline and does not survive paraphrase), and the red verdict routed back to the prompt, not
  the agent, with a queue of ghost agents behind the live one and three tags: the prompt never
  changes, the agent remembers nothing, the repo keeps everything. Ask the room what that implies
  and let someone say it: the files are the only memory. *The signs*: Huntley's own word for
  tuning the loop, four of them under the four parts of the picture — the prompt (one task, full
  code, what done looks like), when it fails (a sign in the prompt, not an argument in the
  thread), the memory (spec, plan, rulebook), the stop (tests and a commit every run, a cap on
  runs, then a human reads). Seeing that the famous technique is four words of shell is what makes
  the three standards feel load-bearing rather than fussy. Provenance sits on the last of the
  three: Huntley 2025, an official Claude Code plugin since December 2025, and the person who
  built Claude Code has said he uses it. One footnote, verified in the plugin's source: the plugin
  is a Stop hook that feeds the prompt back into the *same* conversation, so only the shell loop
  gets the fresh agent the slide describes. The citation line says so.
- **`/goal` closes the act, and it is the reason the act matters.** A year after Huntley's bash
  loop, both Claude Code and Codex ship it as a command: a finish line in plain words, and turns
  keep running until a separate evaluator model agrees it holds. Underneath it is a Stop hook —
  which is exactly what the ralph-wiggum plugin was. The slide deliberately rhymes with the one
  before it: same chip, same place on the page, one year apart. Two beats to land. The evaluator
  cannot run anything, it only reads the transcript, which is *why* "paste the final test output"
  is in their loop prompt — evidence is not politeness, it is the only thing the judge can see.
  And everything the tool automated was the easy half: nothing in it writes the rulebook or decides
  what done means. Students on Codex can enable it today (`codex features enable goals`); tell them
  not to, until they have a test that fails first.
- **Rules come from failures.** The retro converts today's worst agent behaviour into one `AGENTS.md` line with the reason in the commit message. That's the meta-skill: the rulebook grows from observation, not from longer prompts.

## Run of show

Four acts, each opened by its kicker colour: **teal** logistics · **blue** git · **violet** from a
model to an agent · **amber/coral** the three standards. Three divider slides (`git`, `agent`, `3`)
mark the turns. Three pictures carry the first half and each is *built* rather than shown: the git
graph grows over six slides, the model-to-agent stack over four, and the ReAct ring appears once in
Act 2 and again in Act 3 with the tests in it. Say so on the agenda slide.

| Min | Slides | What | Checkpoint |
|---|---|---|---|
| 0–5 | 1–3 | Open, agenda, check-in: GitHub page shows the feature-1 branch and a merged PR. | TA has the list of who is behind |
| 5–6 | 4 | Divider: **git**. | — |
| 6–12 | 5–10 | **Act 1 — git, as one story.** The graph grows by one move per slide: `main` → branch → commit → second commit (`main` has not moved) → local and remote → merge, approved. About a minute each — it is a build, so do not narrate it twice. | — |
| 12–13 | 11 | Divider: **agent**. "The thing that will make those commits today is not you. So what is it?" | — |
| 13–30 | 12–23 | **Act 2 — from a model to an agent.** Two history slides (1958–2017, then 2018 onwards) and one exhibit (GPT-2's unicorns, read aloud) · the stack in four moves: a language model · tools · an agent · the harness · **one exchange in full** (slowest slide in the act) · reasoning, watched · the ReAct ring · context · context rot. | — |
| 30–31 | 24 | Divider: **three standards**. Bridge: the ring has three places you get a say. | — |
| 31–45 | 25–34 | **Act 3 — the standards.** Rulebook (+ live: add three rules, commit) · judge (run the red tests on stage) · the loop (same ring, tests in it) · the four parts of an ask · Ralph, four slides (who he is · one run · the loop · the signs) · `/goal`. | Every laptop: an `AGENTS.md` commit pushed |
| 45–55 | 35 | **Live kick-off.** Branch → red → new thread → paste the ask → watch it loop → read the diff → click the app → merge. Let it get something wrong. | Room has seen one full loop and one "green but wrong" |
| 55–85 | 36–37 | **Your turn.** Bug on `main`, then feature 2 on a branch. | Bug test green and pushed; feature 2 green on its branch |
| 85–89 | 38 | **Retro.** Worst agent behaviour → one rule → commit with the reason. Three read out. | Every laptop: a second `AGENTS.md` commit |
| 89–90 | 39 | Wrap. | — |

**The lecture half is tight but no longer overfull.** Act 2 is twelve slides in seventeen minutes and
Act 3 is ten in fourteen. Rehearse to these weights: one exchange in full 2½ min · the stack 1 min
a slide (four) · reasoning, ReAct, context rot 1½ each · context 1 · the two history slides 1½ and 1 · the unicorn 1.
In Act 3: rulebook 2½ and three rules 2 (both live) · judge 2½ · loop and the shape of an ask 1½
each · Ralph 20 s, 40 s, 50 s, 60 s (who he is · one run · nobody is watching · the signs) · `/goal` 1 min. Git runs at a minute a stage. **The 30
minutes of hands-on do not move.** If you are behind at the `agent` divider, cut the two history
  slides and the unicorn on the spot; they are the only slides nothing later depends on. If the room is quick, the
minutes belong to *your turn*, not to you.

## Exact prompts for the live part

- Proof of the rulebook: *"What does AGENTS.md tell you to do?"*
- Adding the rules: *"Under 'How to answer' in AGENTS.md, add these three lines: …"* — the verbatim wording is on the Week 4 page and in the handout (slide 25 shows only the three concepts: boundary, evidence, off-limits). Read the diff. Accept.
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
