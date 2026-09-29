# Class 5 — Your own product

29 September 2026 · Ricardo · 90 minutes · Block 2 launch.

## Outcome

Every student leaves with a chosen project, a first-feature spec, and a way to check state and persistence. A first working workflow is a stretch outcome, not a requirement for leaving the room.

## Run of show

| Minutes | Slides | Activity |
|---|---|---|
| 0–10 | 1–3 | Connect to Class 4; introduce the three products; students choose provisionally. |
| 10–25 | 4–7 | Walk the room/key example on the board; identify state, a rejection, and persistence. |
| 25–40 | 8–10 | Read a BRD requirement and acceptance scenario; write one task spec; students sketch their equivalent. |
| 40–60 | 11–12 | Live-build one small workflow with the reviewed spec. Inspect the rule, test it, stop and restart. |
| 60–80 | 13–14 | Students complete the planning sheet and begin one workflow. Circulate and ask for the rejection rule. |
| 80–90 | 15–16 | Two students explain their state and a check; show the exam template; close with the next-class expectation. |

## Prepare before teaching

Open the Week 5 page, overview, Plot Twist BRD, and exam template. Use a separate demo folder so the Block 1 repos remain intact. Keep the worked first-feature spec open. Use Python, Streamlit, SQLite, and pytest as the first-release stack. No API keys or deploy in this lesson.

The live demo is built in class; this pack does not include a finished demo app. If model access or setup blocks the build, trace the workflow using the worked example and spend the remaining demo time reviewing the proposed state and tests. Protect the 20-minute student exercise.

## Board exercise

Start: room = office, inventory = empty, ending = none. The story contains a key in a drawer and a locked route to the corridor.

1. Try the route. Ask for the expected result before revealing it: rejected, still in the office, inventory unchanged.
2. Open the drawer and take the key. State now includes the key.
3. Try to collect again. Still one key.
4. Use the route. Current room becomes corridor; the key remains.
5. Stop the app. Ask what must be saved to resume correctly. A Python variable alone disappears; saved data can be loaded into the next process.

Differentiate fixed story content, player state, and storage. A database does not replace validation. Git stores code history; it is not the mechanism that saves each player's latest action.

## Live demo sequence

Use the worked spec on the planning sheet. Ask the agent for a state model and the three checks before implementation. Read expected results yourself. Ask it to create those tests, observe the first failure or missing implementation, then implement only the slice.

The student page contains the handoff prompts. Show the rule in `logic.py`, the save/load functions in `db.py`, and the UI call in `app.py`. Run the tests and click the same allowed and rejected paths. Close the running process, restart it, and resume. If it fails, use the symptom to locate the storage path; do not claim refresh alone proved persistence.

## While students work

- Can they name one user action and its before/after state?
- Does a rejected action leave both memory and stored data unchanged?
- Is their test checking a concrete outcome from the BRD?
- Can their first task fit inside the full product without building everything now?
- Are they keeping the new app in its own repository?

Students who are ready can build. Students whose setup is blocked can complete and peer-review the spec. Stronger students add a duplicate-action check or improve a restart test; they do not need a new stack.

## Exam discussion

Show the six public question forms. Ask two students: “What does your app need to remember?” and “What input should it refuse?” Tie answers to their chosen project. No assessment weights or submission policies change.

## Publishing and source locations

The site source lives in `content/weeks/week-05/`. `build.py` renders the Markdown pages and copies HTML unchanged. GitHub Actions deploys `_site/` after a push to `main`. This guide is in `teaching/` and is not included in the published site.
