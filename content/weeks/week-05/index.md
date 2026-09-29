---
title: Class 5 — Your own product
date: 2026-09-29
type: theory
---

# Class 5 — Your own product

Block 2 · Theory · 2026-09-29

Last week you gave an agent instructions, tests, and a stop condition. Today you choose a product and turn its business requirements into a first task you can build and verify.

## Start here

- [Class slides](class-5.html)
- [Compare the three products](00-project-overview.html)
- [Plot Twist — business requirements](01-plot-twist-brd.html)
- [Campus Tycoon — business requirements](02-campus-tycoon-brd.html)
- [Festival Architect — business requirements](03-festival-architect-brd.html)
- [Your first feature — planning sheet](first-feature.html)
- [Solo project exam question template](exam-question-template.html)

## What you need

Your laptop, the tools from Block 1, and your existing app as a reference. No new accounts or services today. Keep the Block 1 project intact: your solo product belongs in its own folder and repository.

## What we are learning

**State** is the information that describes the app right now: a player's room and inventory, a business's cash and stock, or the performances already booked. An action reads that state, checks a rule, and either rejects the action or changes the state.

**Persistence** means storing the state so it can be loaded after the app stops. A value in a running Python program is not automatically saved. In our first release, accepted changes should survive a restart; rejected changes should leave the saved data unchanged.

**Content and progress are different.** A story says a key exists in a drawer. A saved game says this player already collected it. Starting a new game resets the player's progress, not the story.

**The BRD describes the product. Your task spec describes one change.** Use the four sections from Class 4: Why, What, Out of scope, Done when. The acceptance scenarios in the brief give you concrete examples of correct behaviour.

## Your turn

### 1. Choose and read

Open the overview and select one product. Read its full brief, including the rules and acceptance scenarios. You can change the theme, name, and interface; the required behaviour is the baseline.

### 2. Plan one complete workflow

Use the [planning sheet](first-feature.html). Start with something small enough to click through from beginning to end:

| Product | First workflow |
|---|---|
| Plot Twist | Collect a key, use it to unlock a route, and resume saved progress. |
| Campus Tycoon | Buy stock, trade one day, and inspect the saved cash and stock. |
| Festival Architect | Add a performance, reject an overlap, and reload the saved lineup. |

Write what must be true before the action, what changes after it, and what must survive a restart. Include an allowed action and a rejected one.

### 3. Prepare your project

Create a separate folder named after your solo product. Open it as a project in your coding tool. Use the familiar structure: screens in `app.py`, rules in `logic.py`, storage in `db.py`, and a `tests/` folder. For this first release, use Python, Streamlit, SQLite, and pytest, run with uv as in Block 1.

Save your task spec as `specs/first-feature.md`. Save a copy of the selected BRD in `docs/` and tell the agent where it is. A browser can save the brief as an HTML file; alternatively copy its text into `docs/product-brief.md`.

Ask the agent to propose the file structure and tests before building:

```
Read the product brief in docs/ and specs/first-feature.md.
List the state this workflow needs, what must be saved, and the rule that rejects an invalid action.
Propose tests for the allowed action, the rejected action, and restarting the app.
Do not implement yet. Point out any requirement you cannot determine from these files.
```

Read the proposal against the brief. You are responsible for the expected outcomes, even if AI writes the tests.

### 4. Build and verify one task

Set up your own GitHub repository using the workflow from Block 1. Keep it private, confirm the remote is yours, and make an initial commit before starting the feature branch. Keep local database files and secrets out of git.

Your `AGENTS.md` should describe the run and test commands, the folder structure, and the branch and verification rules. Unlike Block 1, this is a new app: tests need to be created. Ask for the tests first, review them, and then keep those expectations fixed during implementation. Correct an incorrect test explicitly against the BRD; never weaken it just to get green output.

```
Implement specs/first-feature.md on a branch named first-feature.
Use the reviewed tests as the acceptance checks. Do not weaken, skip, or delete them to make the implementation pass.
Work only on this workflow. Run the tests, show the final output, and list the changed files.
Then tell me how to verify the workflow in the running app, including stopping and restarting it.
```

Read the diff, perform the accepted and rejected actions yourself, then stop and restart the app. Refreshing the browser alone is not the full persistence check. When the feature works, commit, push, review, and merge using the workflow from Class 4.

## Before the next practical

Bring your selected brief and completed first-feature spec. If you have started building, be ready to run it, show the checks, and explain what is saved. Push your progress before closing the laptop.

The whole product does not need to be finished today. W6–W7 are for building; the solo project becomes a possible starting point for the team project in W8. Nothing is uploaded to Moodle.
