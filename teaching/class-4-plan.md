# Class 4 — Rules, judge, loop · TA plan and answer key

90 min · practical · 2026-09-22 · deck `content/weeks/week-04/class-4.pdf` (42 slides in four acts; LaTeX source in
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
- **The git act opens on Linus Torvalds, not a divider** (2026-09-22, the user: "why did he invent
  git?"). One photo (Krd, LinuxCon Europe 2014, CC BY-SA 4.0, `decks/figures/linus.jpg`) with the
  "egotistical bastard" line under it, and three plain bullets (cards, then eyebrows, then bold lead-ins were
  tried first and cut the same day, at the user's request): the problem (the kernel's tool withdrawn in a week, April 2005), ten days (he wrote it
  himself and ran the kernel on it by June), and what it had to do — everyone holds the whole
  history, every change named by its contents, fast — which are the three ideas the act then draws.
  The BitKeeper story and dates are in the notes.
- **Git comes first.** It is what they just looked at on their own GitHub page, it is what last week
  was about, and every later slide (branch, judge, push, merge) leans on its vocabulary. Putting it
  before the agent material also means the class opens on something concrete and already familiar
  rather than on an abstraction.
- **One tool call is shown in full, as a transcript.** The stack gives the choreography; the slide
  after it gives the payloads — the structured request the model emits, the approval prompt, the
  file's own line pasted back, the answer. It is the slide that turns "the AI reads your files" from
  magic into mechanism, and it sets up standard 2: a thing that can only ask, and can only see what
  is handed back, is a thing you can verify. Since 2026-09-21 it is drawn on the same turn spine as
  the reasoning slide that follows (it was a two-column table until then, and is titled *End-to-end
  flow* rather than *One exchange, in full*): each turn is labelled down the spine with an icon for who
  is acting — the person and the boxed *f(x)* from the stack slides, plus a window-with-a-prompt for
  the harness, drawn rather than borrowed so the glyph says "harness" and not "Codex" — one colour per
  actor, and the next slide is then visibly this one with thinking added. Labelling by ReAct role was
  tried first and dropped the same day: it put the harness on the slide twice in two colours.
- **The model's icon is *f(x)*, not a sparkle.** Changed 2026-09-21 at the user's request, and it
  carries the act's argument in one glyph: a sparkle is the industry's mark for magic, while the
  history slides spend their whole length saying the opposite — hide a word, guess, get corrected;
  nothing but parallel arithmetic. It is typeset in maths italic rather than in Inter on purpose, so
  it reads as a function and not as a word. It appears on every slide that draws a model: the four
  stack slides, *Guess the next word*, *End-to-end flow*, and the Ralph loop.
- **The model-to-agent stack is one picture built in four moves.** *A language model*: you and the
  model, text both ways, centred on its own canvas (it had a dashed circle holding the empty half
  until 2026-09-21; the user cut it, so stage 1 is centred and the pair slides left when *Tools*
  arrives — the one place in the deck where a build moves rather than only adds). *Tools*: a laptop with
  read · edit · run, and the result arrow pointing back at the **model**, not at you — that arrow
  is the whole slide. *An agent*: one more arrow, "again, until done", and the equation. *The
  harness*: the box that was always there gets drawn and named, with the "may I?" gate on its edge
  and its three jobs along the bottom. Since 2026-09-22 the letterspaced "CODEX · THE HARNESS"
  label above the box is a row of the products instead — Codex, Antigravity, Claude Code, Pi,
  OpenCode — at the user's request, because the slide's claim is that the harness is a category
  and five marks say that faster than a caption can. They are flattened to one ink on purpose:
  five brand palettes at the top of a slide read as a sponsor wall. Marks come from Wikimedia
  (OpenAI's 2025 symbol, public domain), antigravity.google's own site icon, and Simple Icons
  (CC0) for the rest; they live in `decks/figures/logo-*`. Same canvas every time, so the LLM / tools / agent / harness
  distinction is spatial: each word is a region of the same picture.
- **Each stop on the run-up carries a picture.** Added 2026-09-22 at the user's request: the neuron
  model, the four points no straight line can split, an MLP, an RNN, and — the joke the slide has
  been waiting for — a transformer of the other kind. Real images, not drawn glyphs, so they are
  credited on the slide and linked: Chrislb (neuron, LSTM) and Yearofthedragon (XOR) under CC BY-SA,
  HRcommons (MLP) public domain, Kiri Karma's Optimus Prime cosplay under CC BY-SA 2.0, all via
  Wikimedia Commons; files are `decks/figures/tl-*`. Two layout consequences: the LSTM stop lost its
  stagger so the five pictures share one row, and it sits at x=0.66 rather than the 0.635 its year
  gives it, because "Backpropagation" is a 19mm word. The winter is still the widest gap on the
  slide, which is what the scale is there to show.
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
- **Every git slide carries the diff it is talking about.** Added 2026-09-21 at the user's request: a
  card in the bottom-right of each slide in the act, showing the command and its output. Since
  2026-09-22 the diffs are the commits the graph labels, so cards and labels say the same thing
  (until then every card changed one `hello.py` greeting while the graph said "column" and
  "totals", and the user caught it): *feature 1* on `main` adds `balances` to `logic.py`; the
  branch's *column* commit adds `"category"` to `COLUMNS` in `db.py`; *totals* adds
  `category_totals` to `logic.py`; the merge lands both; the conflict is two branches editing the
  same line of `logic.py`. *A branch* is the card that teaches the most by being empty: `git diff
  main feature-2` prints nothing, because branching copies rather than changes. *Merge*
  deliberately repeats the six lines from *Working on a branch*, asked of `main` instead of the
  branch. *Local, and remote* is the one slide in the act without a card — the picture already
  fills the frame, and what changed is not that slide's question. *The record* shows the column
  commit's diff again, in its pane. Technically these are minted + Pygments' diff lexer, so the
  colours come from lexing rather than from hand-marking a listing; the build needs `pygmentize`
  on PATH and tectonic's `-Z shell-escape`, both wired into `build.sh`.
- **Figure captions are NovaBody, not NovaMuted.** Changed 2026-09-22: muted grey measures 4.16:1
  against the paper, under the 4.5:1 floor for body text and thin on a projector in a lit room.
  NovaBody is 6.99:1 and still reads as secondary under the near-black titles.
- **The git act ends on the record** (added 2026-09-22 at the user's request: "we can track, and
  go back to, the full changes — who did it, when"). *The record* is the five commits of the graph
  as a list, newest at the top, the way `git log` prints it and GitHub Desktop's History tab shows
  it: hash, message, who, when, in the graph's own colours. One row is picked out and its diff sits
  beside the list — the `Hello, Nova SBE!` change from *A commit*, so the list visibly indexes the
  slides before it — and an arrow down the left edge says any row can be gone back to. It follows
  *A conflict* as a second aside, and it does a job for later in the day: most rows in their own
  log will be the agent's, and the log is how they audit those after the fact.
- **It is framed the way this audience already thinks.** `main` is the approved version, a branch is your draft,
  commits are checkpoints, a pull request is sending it for review, a merge is the sign-off. Nothing about git is
  new to someone who has ever had a model reviewed before it went out — only the vocabulary is. The two habits that
  usually get announced as rules (name the branch after the job; keep commits small) fall out of slides 2 and 3
  instead.
- **Reasoning gets shown, not described.** Slide 20 is a chat mock-up where it earns its keep. The
  ask — *"make it so Ana doesn't owe anything"* — is genuinely ambiguous, and every reading of it
  moves somebody's money. Read it aloud and stop: the room will give you at least two readings,
  which is the point. Without the thinking block you get one of them at random and no way to tell
  which; with it you get the safe one plus a stated assumption you can overrule. The thinking block
  is styled as the odd one out — no fill, dashed rule, italic — because it is not a message anyone
  sent. The definition ("worked out first, then answered") is in the kicker; the lineage is in the
  notes.
- **Prompt engineering gets one table, after reasoning** (2026-09-22, the user: "prompt
  engineer bloopers … the idea is to convey that reasoning kind of solves this issue"). Five rows,
  when · prompt · effect(s) · source (linked; a real `tabular`, since hyperref links do not
  survive inside a TikZ node, which the user noticed): "let's think step by step" (Kojima 2022,
  18→79% on MultiArith), "take a deep breath" (Yang 2023, 72→80% over "step by step", found by a model searching
  prompts), "important to my career" (Li 2023, +8%; the 2024 replication that found ~1% was in the row and
  moved to the notes at the user's request), the \$200 tip (Bsharat et al. 2023, MBZUAI, +45% judged
  quality on GPT-4 over twenty questions — the row says "judged by hand", and it replaced the
  viral Vogel tweet at the user's request, published source over a thread), and please/thank you
  (Yin 2024: rude prompts score lower; Altman 2025: tens of millions in electricity). Brin's
  kidnapping line (All-In, May 2025) was a sixth row and was cut the same day. Under the table a
  purple callout, "Since 2024: don't", carries what ended it: reasoning models work it out first
  and OpenAI's own guide says "avoid chain-of-thought prompts" (it was a table row first, then a
  caption, and the user asked for it to be obvious). The caption makes the argument: none of it
  was engineering, it was guessing which words sat next to good answers in the training text,
  which is the GPT-2 slides again; what survives is Act 3, structure rather than incantations.

- **ReAct is drawn once and reused, so it reads as the architecture rather than a diagram.** The loop
  — reason, act, observe, the "not yet" return underneath and the "done" exit to the right — is
  slide 23 in Act 2 and slide 29 in Act 3 with the tests written into it: *read the failure* ·
  *edit, then run the tests* · *red, or green?* · *green: read the diff, click the app*. The bridge
  at the `3` divider is that the loop has three places where you get a say: what it reads before
  the first thought (the rulebook), what it observes (the judge), and when the return arrow stops
  (the loop). The standards are the loop, configured.
- **Context is shown concretely first, as one box the model reads.** Since 2026-09-22 the
  context slide draws the window as an open box in oblique 3D, at the user's request ("I was
  really thinking about a 3D box"; it was a flat bordered page with tagged lines until then).
  The things it holds stand inside as cards, like folders in a file box, back to front: the tools
  (a menu of three chips, `read_file` with what it returns) and the rulebook (two of today's
  lines) at the back, "there before the first thought"; then one card per turn — your message, a
  thought, the call, the file that came back — "added as it works", the newest at the front where
  the next one goes. The cards stand against the back wall and the open floor is in front of them, with a dashed
  slot marked "the next turn" (the user's correction, same day: the axis says newest in front,
  so the room to grow has to be in front too, not behind). The two permanent cards, tools and
  rulebook, are tinted pale teal (`NovaFixedCard`, at the user's request; an amber tint was tried first and
  vanished against the cream box) so the two kinds of card
  can be told apart without a heading; the rulebook keeps its tint on the context-rot slide. The front wall hides the bottom of
  every card, so each row shows one line of the row behind it and only the front card, the
  result, shows more: three lines of `logic.py`.
  Every example is bug 002. `read_file` is outlined twice, on the tools card and on the call card,
  and the notes say why: the tool's own line is in the box, and that is how it knows which one
  to call — the answer to the question the reasoning slide raises. The only words beside the
  box are one axis along its depth, "there before the first thought" at the back and "one card
  per turn, the newest in front" at the front (the two letterspaced headings and two side notes
  it had for an hour were cut the same day, at the user's request: one axis says it), and the
  model, which "reads all of it, before every word it writes". Context rot is then
  the same box twice (since 2026-09-22; before that, two mock terminal panels imitating what
  `/context` and `/compact` print, and before those a chart and a four-moment bar that were judged
  illegible and too abstract): left, some way into a bug, eight cards deep at a tighter pitch —
  the rulebook one thin card at the back, then files it read, command output, and three unrelated
  questions (bug 002, a git question, how the CSV is read) in front of it, "87% full"; right,
  after `/compact`, the same box with four cards at the back — the rulebook, the summary the
  model wrote of its own conversation, the last two turns — and the floor in front of them
  empty, "12% full". The two percentages
  are what `/context` prints, and `/compact` on the arrow between the boxes is a deliberate
  exception to "no commands on slides", like the Ralph one-liner: it is the point, and if the
  screen is available the TA types it and the real output replaces the slide. The slide's own
  words stay short ("a full, messy box makes the work worse; compaction clears it") and the
  jargon (soft middle, TACL) lives only in the notes. It cites a coding measurement first — Rando
  et al. 2025, LongCodeBench: Claude 3.5 Sonnet fixed 29% of real GitHub bugs at 32k tokens of
  context and 3% at 256k — and the two reading ones (Liu et al. 2024, worse-than-no-documents in
  the middle; Chroma 2025, every model falling before ten thousand tokens) are told in the notes,
  not charted.
  It explains why "start a new thread after twice
- **The GPT-2 block is the unicorn and one picture.** The picture answers "how did it do that?"
  as a strip of three numbered steps: hide a word on a page from the web, guess (a list with
  probabilities), correct (the page says horn; nudge the numbers), with one loop arrow back to the
  start, "next word, next page, a few billion times". The map of word-positions, the block repeated
  48 times and the sentence growing chip by chip were cut on 2026-09-21: three slides of how the
  machine is built, for a room that only needs the shape of the game. What survives of them is one
  caption line and the hand-off in the notes: writing is the same loop run forwards with nothing to
  check against, which is why the unicorn got four horns, and the agent loop later is this loop one
  level up. The data (WebText, not Common Crawl) and the real numbers live in the notes.
- **Ralph gets three slides because the picture is the argument.** The crowd photo first and alone:
  not one agent getting better, a queue of identical beginners. Then one canvas grown twice,
  like the git graph. *Same message, twenty runs* (titled *Nobody is watching* until 2026-09-22): prompt → fresh agent → repo → eval, every part
  something they already have from this act (a separate *One run* stage restated the ask slide
  and was cut 2026-09-21), the plugin's one line on top (the deck's one
  deliberate command on a slide, since 2026-09-21 the official `ralph-loop` form rather than Huntley's
  shell loop, at the user's request: `/ralph-loop "the message" --max-iterations 20 --completion-promise "GREEN"`,
  drawn in pieces so each input carries a label: the ask, a cap on runs, the phrase it may only say
  when true — and the phrase is standard 2 again, the agent's own word, which is why the message says
  "the phrase only after green" and why the cap exists), and the red verdict routed back to the prompt, not
  the agent, with a queue of ghost agents behind the live one and three tags: the prompt never
  changes, the agent remembers nothing, the repo keeps everything. Ask the room what that implies
  and let someone say it: the files are the only memory. *Don't argue. Add a line* — the sign slide, cut 2026-09-21 at the user's request. It drew what a "sign" is (run 4 edited a test to make it pass; nobody to reply to, so one line goes into the prompt file and run 5, a fresh agent, reads it first). `\ralphloop{3}` still draws it if it comes back. Its Huntley citation moved onto *Nobody is watching*, which is now the slide that shows the plugin's command. The rest of Huntley's advice (one task and what done looks like, commit every green, a cap on runs, then a human reads it all) lives in the notes for when someone asks.
- **One money slide, straight after the unattended loop.** Added 2026-09-21 at the user's request:
  *Tokenmaxxing* — the Business Insider headline, screenshotted, in which Benioff says Salesforce
  will likely spend \$300M on Anthropic tokens this year, mostly on coding (All-In podcast, 16 May
  2026; linked to the syndicated copy because Business Insider blocks the crawler used to check the
  link). The headline is the artefact rather than a number set in the deck's own type, because a
  figure that size is easier to believe from the source. It answers the title before it: nobody is
  watching the loop, somebody is paying for it — and at that spend the rulebook and the judge are
  the only things reading every line. Caveats live in the notes: it is the CEO's own estimate, not a
  disclosure, and Salesforce is also an Anthropic investor.
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
- **Act 3 is drawn in Act 2's two visual languages, not in cards.** Everything the agent reads is a
  page (the rulebook, with the three rules drawn as GitHub Desktop draws added lines, green band and
  a plus, because they read a diff last class and will read this one in a minute; the ask, with its
  four parts tagged), and everything it shows you is a terminal (the judge is what the agent says,
  "done, the tests pass", in a chat bubble next to what the tests say, "1 failed", with numbers 1–3
  on the lines in the order to read them: the count says how far, the message says why — the
  to-do — and the name says what). The judge's first version had the terminal alone with three
  arrows from below, and the user found it unintuitive (2026-09-21): the title promised a concept and
  the picture was a reading lesson, and the arrows' left-to-right order fought the lines' top-to-bottom order.
  That fixed three things at once (2026-09-21): five card grids in a row at the core of the class;
  "show me the output" on three slides and "never touch the tests" on four; and no slide ever
  showing a failing test although the notes ask the TA to say "what does the last line say?" all
  afternoon. The rulebook and the three rules merged into one slide, the live kick-off and the
  your-turn tasks into one slide that stays on screen for forty minutes. 42 slides then; 39 since the GPT-2 cut; 41 since the reorder below; 40 since Ralph lost its one-run stage (2026-09-21, the user: condense); 43 since *A test is a claim you can run* was added, and 42 again once the two loop diagrams collapsed into one (2026-09-22).
- **Act 3 opens with the room's own three questions, and every example is bug 002** (2026-09-21,
  the user's second coherence pass: "the order is wrong, too much on the slide, too abstract, jargon
  before the why; judge not well explained"). The divider is now *Delegating*: handing work to
  something fast, tireless and always sure it is done. The first slide asks what anyone asks before
  delegating: how do I brief it, how do I know it is done, and when it is not? Each column answers in
  one line and ends in the tool word as a chip (the rulebook · the tests · the loop), so the jargon
  arrives after the question it answers. Then one standard per question, in that order, with the
  question as the kicker. The judge is two slides because it was doing two jobs: *Don't take its word*
  is the concept (the sentence next to the verdict, and the three things that make a check a judge:
  written before the work, by someone who is not the agent, the same answer every time), and *Red is
  a to-do list* is the reading lesson. The ask closes the act as *All three, in one message*: the message
  as they will paste it on bug 002, the two slots that change between tasks highlighted, and beside
  each paragraph the part it is and why it is there (the task · the fence · the finish line · the
  proof; the earlier version had the tags inside the page and the reasons in one side note, and the
  user asked 2026-09-21 to "show the structure of a well structured request"). Then Ralph is the
  same message in a file. A map slide that pinned the three standards on
  the ReAct ring lived for one commit between the two passes; it explained the order in the tool's
  terms, not the room's, and went.
- **The class opens on the bridge from Class 3, and the bridge is a picture** (2026-09-22, the user:
  rethink the act so it connects to last class and gives them the means to write a rulebook, write
  specs, run the eval loop, and use `/goal` in Codex). *Last week, this week* (`\handover`) is
  Class 3's live feature-1 procedure as a row of chips — branch, red, prompt with the spec, read the
  diff, green, click the app, merge, "you, every step" — and under it today's row: the same chips,
  the four in the middle tinted purple under a bracket, "the agent, on its own, round and round",
  with the red-again arrow, and one new chip at the front, *the instructions*, in the rulebook's amber.
  Redrawn later the same day (the user: "much more intuitive / visually pleasant"; the chip
  rows read as two sentences): now two lanes with the same seven stations in the same columns,
  a person icon over every station last week; today the three middle stations sit in a purple
  panel under the model with the "red: again" loop beneath them, the first station is amber
  (the instructions, "new, and yours: rulebook + spec") and the last two are labelled "still yours".
  Because the columns line up, the handover reads as a region of the picture.
  It sits before the agenda, at the user's request the same day (it was the first slide of Act 3
  for an hour): the class in one picture, so that the agenda's items read as parts of that row —
  git is the branch and merge chips, the agent act is what the purple middle is made of, the
  standards are the instructions and the checks around it. At the *Delegating* divider the TA points
  back to it. (The three-questions slide that followed the divider was cut later the same day,
  in the pass that retitled the act's slides as *AGENTS.md* / *This task* / *The independent
  judge* / *A failing test* / *The assignment* / *The agent loop* / *A persistent loop* ×3.)
- **The spec gets its own slide, as the second file of the instructions** (2026-09-22). *This task: the
  specification* (titled *Say what done is* for an hour; `\specpage`) draws feature 2's spec as the page the agent reads, in the ask slide's
  language — the page on the left, each section's tag and reason beside it: *Why* is the intent
  (where the reasoning slide's ambiguity gets resolved), *What* is the checklist and one line is
  one test, so it is the judge in prose; *Out of scope* is the fence for this task, as the
  rulebook is for every task; *Done when* is the finish line in plain words, which is the sentence
  `/goal` takes at the end of the act. One *Done when* line is marked in red as having no test
  ("you click"), planting the green-is-not-done moment. The caption is the Block 2 hand-off: last
  week you read one, in Block 2 you write them, same four sections. The judge slide's caption now
  says "one test per line of the checklist" so the two slides chain. Handout and Week 4 page carry
  the how-to-write-one (start from *Done when*; one test per *What* line, asked for before any
  code) and the tests-first prompt.
- **The act closes on a recipe** (2026-09-22, the user, mid-turn: "we need to give very concrete
  practical steps"). *Delegating coding agents* (titled *Delegating, step by step* until 2026-09-22) is the one slide in the act that is a numbered list
  rather than a picture: rulebook (three lines, commit, new thread) · spec (four headings) · judge
  first (one test per What line, run red) · branch · the ask, or `/goal` plus the *Done when* ·
  let it loop, twice on the same failure means a new thread · green: diff, app, merge · went wrong:
  one line in `AGENTS.md`. It is the same eight steps in Block 2 with steps 2 and 3 doing the work
  the PM did, and it sits between `/goal` and *Your turn* so that *Your turn* reads as steps 4–8
  for real. *Your turn* step 3 now says "paste the ask, or `/goal` it".
- **`/goal` is told for Codex first, and the mechanism is corrected** (2026-09-22). The Codex page
  (learn.chatgpt.com/use-cases/follow-goals, fetched that day) says a goal names what to achieve,
  what not to change, how to validate and when to stop — the four-part ask — and that Codex stops
  "when it's confident it has reached the stopping condition": the agent's own word, which is
  standard 2 again and is now the first card. Claude Code's second-model evaluator (Haiku reading
  the transcript, *not yet / met / impossible*) is the second half of that card, and the earlier
  slide had attributed it to both tools. Neither runs the tests, so the sentence says how to prove
  it. The slide carried the Codex steps in one line for a few hours on 2026-09-22 (`codex features
  enable goals` once, then `/goal` and the sentence) as a deliberate exception to
  no-commands-on-slides; the user cut it the same day, which puts the slide back on the rule —
  it now shows only `\goalcmd` over the loop. The setup step moved into the speaker note, and the Week 4
  page has the five-step version with a worked goal sentence for feature 2, bounded with "stop
  after 20 turns" (the Claude Code docs' recommended form; on Codex a plain instruction).
- **Act 3 is one chain of artefacts, and every figure shows who uses it next** (2026-09-22, the
  user's redraw plan: "a chain of artifacts feeding one another, not a sequence of advice slides";
  standing rules → task ticket → tests → assignment → agent loop → /goal). The rulebook sheet is
  unchanged. `\specpage` is now a task ticket with four stacked bands (Why · What · Fence · Done
  when) and, beside each, an arrow to its downstream use: its reasoning, the tests, the
  assignment, the goal. `\testchain` replaced `\claimpanel`: the four What lines on the left, the
  four real test names from `tests/test_feature_2.py` in the middle, one verdict box on the right,
  and the three properties of a judge under it — the causal backbone of the lesson, the judge
  comes from the spec, not from the agent. `\redread` keeps its terminal and gains a final band,
  "next input to the agent: lines 2 and 3, verbatim". `\askpage` is now one handover card with
  four coloured strips down its edge (task · fence · finish line · proof) and the model reading it,
  no rails. `\taskloop` is Act 2's ring with the artefacts in the cards (the assignment · edit, run
  · the verdict; red goes back for another attempt, green goes to human review), and
  `\persistloop{cmd}` draws that same loop inside a dashed "one run" frame with a command on top
  and the eval's arrow bringing the same assignment back: the Ralph slide with `\ralphcmdcore`,
  the Codex slide with `\goalcmdcore` (the ticket's Done when, the fence, a cap, each labelled),
  nothing else changed between the two on purpose. `\ralphloop` and `\claimpanel` are gone.
  Later the same day the user cut two of these: the Ralph ring slide (the photo hands straight
  to the Codex canvas; the plugin's line is in the notes) and *A failing test* (`\redread`
  deleted; the bottom-up reading is done live on the tests slide, in its notes). Then *The agent
  loop* went too (relayed by the other session): the persistent-loop canvas already shows the
  loop, so `\taskloop` is unused and the assignment hands straight to Ralph.
- **The materials were checked against the student ZIPs** (2026-09-22, the user: "verify if the
  class material is compatible with our presentation; should we provide the AGENTS.md, the
  specs?"). Nothing new has to be handed out: both ZIPs from Class 2 already carry `AGENTS.md`
  (with a `## How to answer` section, which is where the Week 4 page says to put the three
  rules), `specs/feature-2-*.md`, `issues/002` (SplitIt) and `issues/003` (Tiny CRM), and the
  tests, and on a pristine copy `tests/test_feature_2.py` is four red in both apps, as the
  slides say. The four SplitIt test names on the judge slide are the real ones. One conflict
  found and fixed on the page, the handout and the speaker note: the ZIP's `AGENTS.md` ends
  with *No git in this project unless the student asks for it explicitly*, which contradicts
  the first new rule, so the instruction is now to replace that line with the three, and the
  live diff is one red line and three green, and the rulebook figure now draws exactly that
  hunk on the real file (real headings, `uv run streamlit run app.py`, the No-git line struck
  through above the three added rules).
- **Rules come from failures.** The retro converts today's worst agent behaviour into one `AGENTS.md` line with the reason in the commit message. That's the meta-skill: the rulebook grows from observation, not from longer prompts.
- **Nothing is handed out today, and the slides now say so** (2026-09-22, the user: *"do we have the
  tests, or do they have to write it? Do we have the AGENTS.md? And the specification, is it
  given?"*). All three artefacts have shipped in the Class 2 ZIP since week 2 and are already in
  every student's repo: `AGENTS.md`, `specs/feature-2-*.md`, `tests/test_feature_2.py`. Verified by
  running both pristine apps: SplitIt and Tiny CRM each give exactly `4 failed` on
  `tests/test_feature_2.py` (so the *4 failed* verdict card and the handout's "all four tests pass"
  are literally true for both), the two bug tests fail, and the published copies of the four specs
  and issues are byte-identical to the ones in the ZIPs. The only thing students *author* today is
  the three `AGENTS.md` rules plus their own retro rule. The gap was that the deck never said
  this — *Delegating, step by step* read as though steps 1–3 were authoring tasks, on the one slide
  the notes tell them to photograph. Fixed: step 1 now says `AGENTS.md` **is already in your repo:
  replace the No git line**; steps 2 and 3 carry a teal **Given today:** tag with the filename. The
  judge slide's caption dropped *"One What line, one test"* — the peer's numbered column heads
  (1 · THE SPEC · WHAT → 2 · THE TESTS → 3 · ONE VERDICT) already say it — and spends the line on
  *"These four are in your repo already, and already red."* Same fix in the handout: the standards
  sheet's *Tests first* paragraph now opens with today's four red tests before the Block-2
  instruction to ask for them, and the *Delegating* preamble names step 1 as today's work too.
- **A test is opened up before it is called a judge** (2026-09-22, the user: *"should we also
  explain what a test is?"*). Nothing in Classes 1–3 or the week-4 handouts ever said what a test
  *is* — students had only run them and watched red turn green — while Act 3 asks them to read the
  tests and check that each one tests its *What* line, which is impossible if a test is a black box.
  So *A test is a claim you can run* now sits between the spec and the judge slides: one real test
  from their own repo (`test_the_category_list_is_fixed`, verbatim), in the dark chip the judge slide
  already uses, with the three parts named beside it — the name is the *What* line, the docstring is
  the claim in English, and `assert` is the only word that does anything. Drawn in TikZ rather than
  minted: only the diff tokens are repainted in the palette, so Pygments' Python style would arrive
  in its own colours. The same explanation opens the handout's judge section, with the honest limit
  stated in both places: a test only checks what someone thought to write down, which is why green is
  not the end and why one *Done when* line has no test at all.
- **The two loop diagrams collapsed into one** (2026-09-22, the user). *A persistent loop* (the
  `/ralph-loop` plugin line over `\ralphloop`) is gone; *A persistent loop in Codex* survives,
  retitled *Persistent agentic loop*, keeping `\goalcmd` over the same diagram and taking the deleted
  slide's caption — *The message stays fixed. The repo keeps the work. The eval decides whether it
  runs again.* The command left on screen is now the one they actually type today rather than a
  Claude Code plugin they will not use. The Huntley citation and the plugin fact moved onto the photo
  slide, and the surviving note absorbed the deleted one's walkthrough and its trap (the loop ends on
  the agent's own word; nothing checks it). `\ralphcmd` is left defined but unused in case it returns.
- **The two instruction slides, decluttered and anchored** (2026-09-22, the user: *"there's an
  instruction set (slide 38 and slide 39). Could we make it less cluttered, more straightforward,
  with less jargon?"*, then *"instructions need to be clear, understandable, and rooted in the
  existing/given material"*). *Delegating coding agents* went from eight flat steps with five inline
  code chips to six plain ones under three headings — **first, set it up** (rules · task · tests ·
  branch) · **then hand it over** (one task, one chat) · **then check it yourself** — with the real
  file set quietly to the right of each step (`\filetag`): `AGENTS.md`, `specs/feature-2-….md`,
  `tests/test_feature_2.py`, `feature-2-…`. Three right-hand notes were tried on the headings and two
  were cut the same day when the user asked whether they earned their place: *the wording is on the
  Week 4 page* was a pointer to a pointer (step 5 already says what to say, and *Your turn* already
  points at the page), and *the part no test can check* went inside step 6 as its reason — "click the
  app — no test covers that" — which is where it teaches rather than labels. The one that stayed,
  *the first three are already in your repo*, is the answer to the question the user had asked
  earlier: do the students write these, or do we give them? The phases are the lesson: everything in the first group
  happens before the agent is told anything, and the last group is the human. Two steps moved off
  the slide because other slides already carry them — *same failure twice* is the whole of *When it
  goes wrong*, and *write a rule* is the retro. The jargon dropped is ours rather than the
  industry's — fence, finish line, proof, judge — which the user had queried once before; the named
  version is still two slides back on *The assignment*. *Your turn* became six one-line steps
  (ragged right: the narrow column was justifying into rivers), and its two app cards now name the
  actual files rather than pointing at the Week 4 page. The handout's *Delegating coding agents*
  section was restructured onto the same three phases and the same six steps, so the slide and the
  page no longer disagree on how many steps there are.
- **The speaker-notes PDF was rendering every numbered step invisible** (2026-09-22, found while
  checking the above). In `class-4-notes.pdf` the body of every `steps` item came out in the page
  background colour — sampled at (243,242,238) against a (255,252,247) background — while the chips,
  eyebrows, captions and `\code` chips on the same slides were perfect, and `class-4.pdf` was
  correct throughout. Cause: the notes build ships each frame through pgfpages (`show notes on
  second screen=right`), whose box re-use leaves pdf's colour stack out of step. Neither the chip's
  TikZ node nor its fill was to blame — replacing the chip with plain text did not help. Fixed by
  stating the colour inside the list itself, `before=\color{NovaFg}` on `\setlist[steps]`. It
  affected *Delegating coding agents*, *Your turn*, *When it goes wrong* and *Write one rule* — the
  four slides the TA most needs to read off the second screen. It was not only `steps`: plain
  `itemize` had it too (*Your GitHub page*, *Why git exists*, *Write one rule*, *Before next week* —
  so the second screen was missing the check-in list, the three git design decisions and both
  homework lists), and a plain `tabular` on *End-to-end flow* had already come out near-white
  earlier in the session and been patched locally as a one-slide quirk. Same `before=\color{NovaFg}`
  on `\setlist[itemize,1]` and `[itemize,2]`. **The general rule: any unboxed content that inherits
  its colour rather than stating it is at risk in the notes build.** Boxed things — chips, eyebrows,
  cards, `\code`, tcolorbox — are fine, which is exactly what hid the problem. State the colour
  inside any new list-like or tabular-like macro. **None of this reaches the log**: no box
  overflowed, the ink was just the wrong colour. Verified fixed deck-wide by rendering all 42 pages
  of both builds and comparing ink coverage page by page; every page now matches exactly.
- **The Week 4 page rebalanced away from history** (2026-09-22, the user: *"it focuses too much on
  history, and less on concepts that we are using for the class"*). Measured before touching it:
  *From a model to an agent* ran to 1233 words, of which roughly 900 were four history paragraphs,
  while *Three standards* — the part the deck's own divider calls the core of the class — had 278.
  History is now two short paragraphs (~230 words): the ideas are old (perceptron · backpropagation
  · LSTM · Transformer), what was missing was compute and text, training is one game repeated, and
  the two jumps that changed the job were instructions (2022) and tools + a loop (2023–25). The
  year-by-year detail was not deleted, it was already in the standards sheet as a table, which the
  paragraph now points at. The standards section grew to 454 words and carries the concepts the
  class actually uses: the rulebook and what belongs in it, the spec's four sections, *a test is a
  claim you can run* with `assert` named, never edit a test, ask for the output not the sentence,
  green is not the end, one task per loop, and why a failing thread gets replaced rather than
  argued with. Net: the section on the core of the class is now longer than the section on how we
  got here, which is the right way round.
- **The judge slide stripped back to the chain** (2026-09-22, the user: *"let's take the
  clutter/eyebrows out of The judge comes from the spec"*). Gone: the three numbered column heads
  (1 · THE SPEC · WHAT → 2 · THE TESTS → 3 · ONE VERDICT) and the hairline row of three chips
  under them (*written before the work* · *not by the agent* · *same answer every time*). What is
  left is the derivation itself — four *What* lines, four tests, one verdict — and the arrows are
  the argument, which is what the slide was always for. Both removals had quietly become
  duplication rather than scaffolding: *A test is a claim you can run*, added earlier the same day
  between the spec and this slide, names `tests/test_feature_2.py` on its card and already says
  "nobody's opinion, the same answer every time, before the agent starts and after it stops" —
  which is the three chips in one line, one slide earlier, where a student meets the idea first.
  The heads were right when they were written, before that slide existed. The speaker note used to
  end a sentence with "which is what the three boxes at the bottom say" and now tells the TA to say
  it aloud instead, pointing back at the test slide.
- **"Brief" renamed to "the instructions"** (2026-09-22, the user disliked the word and asked
  for alternatives). It was agency jargon doing a job plain English does: the collective noun for
  the two files the agent reads before it works — `AGENTS.md` for every task, the spec for this
  one. Changed on the agenda, on the bridge slide's amber card, in both handouts and in the source
  comments. Two things surfaced while grepping for it. The agenda said *"Delegating: the brief, the
  judge, the loop"* while the deck title, the cover and the Act 3 divider all say *Rules, judge,
  loop*, so "brief" was already the outlier. And `\tqcol` in the theme — the three-questions
  figure, whose first column is *"1 · THE BRIEF / How do I brief it?"* — is dead code: nothing in
  the deck references it, so it was left unedited and is a candidate for deletion. On the card,
  "the instructions" needs an explicit line break; left to itself TeX hyphenates it as
  "the in-structions" inside the 15.4mm card.
- **Every citation is live and clickable, checked end to end** (2026-09-22). All 23 distinct URLs in
  the deck and theme resolve; the two non-200s are bot-blocking, not rot (APA returns 200 with a
  browser user agent, Elsevier 403s any `curl`). The built PDF carries 27 link annotations,
  including all six on the prompt-engineering slide and Elman's DOI with the parentheses in it
  (`10.1016/0364-0213(90)90002-E`) — worth re-checking after any hyperref change, since a raw `(`
  in a PDF string is exactly the kind of thing that silently kills an annotation.

## Run of show

Four acts, each opened by its kicker colour: **teal** logistics · **blue** git · **violet** from a
model to an agent · **amber/coral** the three standards. Two divider slides (`agent`, `3`) mark the later turns; the git act opens on Linus Torvalds
instead. Three pictures carry the first half and each is *built* rather than shown: the git
graph grows over six slides, the model-to-agent stack over four, and the ReAct loop appears once in
Act 2 and again in Act 3 with the tests in it. Say so on the agenda slide.

| Min | Slides | What | Checkpoint |
|---|---|---|---|
| 0–6 | 1–4 | Open · **Last week, this week** (Class 3's loop as chips; today the middle four go to the agent and *the instructions* are new — the class in one picture, before the agenda) · agenda · check-in: GitHub page shows the feature-1 branch and a merged PR. | TA has the list of who is behind |
| 6–7 | 5 | **Why git exists**: Linus Torvalds, April 2005 — the problem, ten days, what it had to do. | — |
| 7–14 | 6–13 | **Act 1 — git, as one story.** The graph grows by one move per slide: `main` → branch → commit → second commit (`main` has not moved) → local and remote → merge, approved. About a minute each — it is a build, so do not narrate it twice. Then two asides, forty seconds each: *A conflict* and *The record* (the same commits as a `git log` list, with one diff beside it). | — |
| 14–15 | 14 | Divider: **agent**. "The thing that will make those commits today is not you. So what is it?" | — |
| 15–34 | 15–29 | **Act 2 — from a model to an agent.** Two history slides (1958–2017, then 2018 onwards) with the NVIDIA aside between them (why the most valuable company: CUDA, the software that opened the games chip to any maths) · the GPT-2 pair: the unicorn sample read aloud, then how it was trained (a strip: hide a word, guess, correct, and round again; the notes carry the data and the "one word at a time, nothing checks" hand-off) · the stack in four moves: a language model · tools · an agent · the harness · **end-to-end flow** (slowest slide in the act; titled *One exchange, in full.* until 2026-09-21) · reasoning, watched (the model reaches for a tool mid-thought; the loop is drawn down the left edge) · *Prompt engineering, 2022–2024*: five tricks in a table, step by step to please and thank you, and the purple callout that ended them: a model that works it out first, whose own guide says not to ask · the ReAct loop · context (one page the model reads: tools, rulebook, your message above the line, thought, call, result below it; the bracket shows why it can pick a tool) · context rot (mock terminal panels: `/context` an hour in, `/compact` beside it, three notes pointing in). | — |
| 34–35 | 30 | Divider: **Rules, judge, loop.** Point back at the opening slide: the purple middle is what this act is about; three controls on it: rules, a judge, a loop. Every slide until Your turn is bug 002. | — |
| 35–47 | 31–38 | **Act 3 — rules, judge, loop.** *AGENTS.md* (titled *Standing rules* for a while): the rulebook as the diff they will read, three rules as green added lines (+ live: replace the No-git line with them, commit) · *This task: the specification*: the spec as the page it reads, four sections tagged (intent · checklist = the judge · fence · finish line; one *Done when* line marked as untested) · *A test is a claim you can run*: one real test from their repo opened up --- name, docstring, `assert` --- because they have run tests since Class 3 without ever seeing inside one · *The judge comes from the spec*: What lines → tests → one verdict and nothing else, the arrows carrying the argument (+ live: run the red tests on stage) · *The assignment*: the ask as the message they will paste, the two slots that change highlighted, each paragraph labelled beside with its part and its reason · *The Ralph Wiggum loop* (the photo, and the name: cheerfully wrong, gets there anyway; a loop around the loop) · *Persistent agentic loop*: one canvas (prompt → agent → repo → eval; red sends the same assignment back), `/goal` on top with the ticket's *Done when*, the fence and a cap, and in the notes the setup step and who decides (Codex: its own confidence; Claude Code: a second model; neither runs the tests) · *Delegating coding agents*: the act as six steps under three headings (set it up · hand it over · check it yourself), each anchored to the real file in their repo, the slide to photograph. | Every laptop: an `AGENTS.md` commit pushed |
| 47–58 | 39 | **Live kick-off.** The "Your turn" slide goes up and stays up: branch → red → new thread → paste the ask → watch it loop → read the diff → click the app → merge. Let it get something wrong. | Room has seen one full loop and one "green but wrong" |
| 58–86 | 39–40 | **Your turn.** Bug on `main`, then feature 2 on a branch; "When it goes wrong" for the last ten minutes. | Bug test green and pushed; feature 2 green on its branch |
| 86–89 | 41 | **Retro.** Worst agent behaviour → one rule → commit with the reason. Three read out. | Every laptop: a second `AGENTS.md` commit |
| 89–90 | 42 | Wrap. | — |

**The lecture half is over budget by three minutes, and the history slides are the slack.** Act 2 is fifteen slides in twenty minutes and
Act 3 eight in thirteen (the spec and the step-by-step slide were added 2026-09-22, a minute each, and the opening bridge slide takes another minute before the agenda, so the live kick-off starts at 49 rather than 46; the three-questions and Tokenmaxxing slides were cut the same day in the retitling pass), so cut the history slides the moment you are behind at the `agent` divider. Rehearse to these weights: end-to-end flow 2½ min · the stack 1 min
a slide (four) · reasoning, ReAct, context rot 1½ each · prompt engineering 1 · context 1 · the two history slides 1½ and 1 · NVIDIA 1 · the GPT-2 pair 1 · 1½ (unicorn, trained).
In Act 3: AGENTS.md 3 (live: replace the No-git line with the three, commit) · the specification 1 · a test is a claim 45 s · the judge comes from the spec 2 (live: run the red tests, read one failure bottom up) · the assignment 1½ · the Ralph Wiggum loop 30 s · the persistent agentic loop 2 · delegating coding agents 1. Git runs at a minute a stage. **The 30
minutes of hands-on do not move.** If you are behind at the `agent` divider, cut the three history
  slides (15–17, NVIDIA included) and run them only if ahead: the GPT-2 pair carries the history the room
  needs. If still behind, the GPT-2 pair itself
  (18–19) is the next cut; nothing later depends on it except the phrase "append it and go again". If the room is quick, the
minutes belong to *your turn*, not to you.

## Exact prompts for the live part

- Proof of the rulebook: *"What does AGENTS.md tell you to do?"*
- Adding the rules: *"In AGENTS.md, under 'How to answer', replace the line 'No git in this project unless the student asks for it explicitly' with these three lines: …"* — the verbatim wording is on the Week 4 page and in the handout (slide 31 shows only the three concepts: boundary, evidence, off-limits). Read the diff. Accept.
- If a student has goals enabled in Codex and a red test: *"/goal every test in tests/test_feature_2.py passes, shown by the final pytest output, and nothing in tests/ changed. Stop after 20 turns."* Steps on the Week 4 page. Not on stage: the live part is the watched loop.
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
