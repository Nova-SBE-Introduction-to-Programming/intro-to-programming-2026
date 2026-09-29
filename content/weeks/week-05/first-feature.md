---
title: Your first feature — planning sheet
---

# Your first feature

Choose one workflow from your product brief. Write your answers in `specs/first-feature.md` in your own project. This is a working document, not a submission.

## Before writing the spec

1. **Product and user:** Which product did you choose, and who performs this action?
2. **Trigger:** What does the user click or enter?
3. **Before:** What information must already exist?
4. **Rule:** When must the app refuse the action?
5. **After:** What changes if the action is accepted?
6. **Restart:** What must still be true after stopping and reopening the app?

## The spec

Copy these four headings. Use concrete values in the checks.

### Why

What can the user accomplish when this workflow works?

### What

List the behaviour that must exist. Reference the relevant requirement or rule IDs from your BRD. Include what happens when an action is rejected.

### Out of scope

Which parts of the full product are deliberately excluded from this task?

### Done when

Describe at least three checks: an accepted action, a rejected action with unchanged data, and a restart that restores the accepted changes. State expected results before asking AI to write tests.

## Worked example — Plot Twist

**Why:** A player should find a key, unlock a route, and continue later without losing progress.

**What:** Show a starting room and a locked route. Collect the key once. Allow the route only after collection; keep the key after use. Save the current room and inventory after accepted actions. Resume the saved game. This implements part of PT02–PT03 and PT R1–R3, with the relevant parts of A1–A4.

**Out of scope:** The remaining scenes, the second item, multiple endings, artwork, and a story editor. These belong to later tasks; this feature is not the full product.

**Done when:**

- Without the key, the locked route cannot be used. The room and inventory stay unchanged.
- Collecting twice results in one key. With it, the route opens and the key remains.
- After stopping and reopening the app, the current room and inventory are restored. The key cannot be collected again.

## Explain it to a neighbour

Ask them to identify the state, point to the rule that blocks an invalid action, and describe one way to break the workflow. Clarify your spec before building.
