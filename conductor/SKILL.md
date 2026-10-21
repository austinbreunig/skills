---
name: conductor
description: Navigator for a product's whole lifecycle across many fresh sessions: reads state, says the exact next command, runs agent-callable steps, guards appetite and value.
---

# Conductor

The user runs `/conductor` at the start of any fresh session. It means: *where are we, and what's next?* Conductor works out the current position by checking real artifacts against the gates below. Then it does one of two things:
- runs the next step itself, if that step is agent-callable, or
- gives the user the exact command to run in a fresh session, and stops.

Conductor navigates; it does not override. It never tells another skill *how* to do its work. It decides order, keeps state, tracks appetite, and enforces gates.

## How work moves between sessions

Every step runs in a fresh session. Nothing carries over in conversation. Each decision lives in exactly one place, and everything else links to it:
- **Wayfinder decisions:** their tickets (the map is only an index)
- **Build-time decisions:** ADRs, wherever `setup-matt-pocock-skills` configured them
- **The cycle's build plan:** the spec issue
- **Conductor's memory:** `.lifecycle/STATE.md`, which holds pointers only

If a session overflows partway through a step, the user can run `/handoff`. Conductor never tries to do more than one step per session.

## Markers

Every step leaves something you can see. Pocock's skills already leave artifacts: a map, a spec, tickets, a PR. Conductor's own steps, plus the ones that leave no distinct artifact, get a **label on the cycle's spec issue**:

- `lifecycle:simplified`: wu-wei has run on the spec
- `lifecycle:seams-locked`: contracts, stubs and fixtures are committed, the tickets are amended, and the adversary pass is closed
- `lifecycle:explained`: the PR's human page exists and is linked
- `lifecycle:reviewed`: the user confirmed they reviewed the PR page
- `lifecycle:ramped`: the ramp report and its page exist
- `lifecycle:verdict-<ship|continue|reshape|kill>`: the verdict is recorded

Rules:
- **A label means checked, not just ran.** Conductor adds a label only after confirming the step's outputs directly (the checks in the table below), whoever ran the step.
- If the outputs exist but the label is missing (the step was run by hand), confirm them and add the label.
- If a label exists but its outputs are missing or broken, remove the label, tell the user in one line, and redo the step.
- Express labels however the repo's tracker doc defines them. If the tracker has no labels (e.g. local markdown), keep a `Lifecycle:` line in the spec's body listing the markers.
- The spec is per cycle, so the markers reset each cycle on their own.

## STATE.md (a cache, under ~80 lines; link, never paste)

```
## Product
One line: what this is and who it serves.

## Lifecycle
One line per finished cycle: N, destination, verdict, touches, default hit rate, appetite accuracy, links to the ramp report and retro.

## Current cycle
Cycle: N
Destination: e.g. "POC proving the change-detection algorithm on one county"
Appetite: budget, and how much has been spent
Route: foggy | clear
Map / Spec: links
Step: the current step
Next: the exact command or action
Touches: a count of each time the user had to act, with the kind
Links: tickets, contracts, integration branch, human pages, ramp report
Open one-way decisions: the list, or none
Value check: one line, updated at every step
```

STATE is a cache. When it disagrees with the tracker or the repo, the artifacts win: correct STATE and say so in one line.

## Starting a cycle

- **First run, or after a Verdict of Continue or Re-shape:** ask the user, in one message, for the cycle's **destination** and **appetite**.
- Destinations get more demanding as the product matures (inception POC → MVP → hardened production → scale). They are chosen each cycle at Verdict, never set as a fixed phase sequence.
- Decide the **route**:
  - **Foggy:** the destination can be named but the way there can't be seen, or the work spans many sessions → start with Wayfinder.
  - **Clear:** the work fits in one session of deciding → start with grill-with-docs.
  - When unsure, say which you'd pick and why in one line, and let the user overrule.

## Finding the next step

On every run:
1. Read STATE to find the current cycle's map and spec.
2. Go down the table in order. For each step, check its gate against the real artifacts: tracker queries, labels, branches, files.
3. The **first step whose gate is not met** is the next step. Any earlier step with outputs but a missing marker gets checked and labelled on the way.

| Step | Runs it | Gate: done when (and how to check it) |
|---|---|---|
| 1. Chart (foggy) | User: `/wayfinder <idea + destination>` | A `wayfinder:map` issue for this cycle exists, with a Destination |
| 2. Walk the map (foggy) | User, one ticket per fresh session: `/wayfinder <map>` | The map has no open child tickets |
| 1′. Grill (clear) | User: `/grill-with-docs`, then `/to-spec` in the same session | (covered by step 3) |
| 3. Spec | User: `/to-spec <map>` | A spec issue exists that is linked to this cycle's map, or created after the grill session; record its link in STATE |
| 4. Simplify | User: `/wu-wei <spec>` | Label `lifecycle:simplified` (wu-wei adds it; see below) |
| 5. Slice | User: `/to-tickets <spec>` | Implementation tickets referencing the spec exist, with blocking edges |
| 6. Lock seams | Conductor: invoke `seam-lock` | Check the contracts and fixtures are committed and the harness runs; every ticket has a Seams section; the adversary findings are closed or recorded as ADRs → label `lifecycle:seams-locked` |
| 7. Build | User: `/implement-spec <spec>` | The integration-branch PR is open and every implementation ticket is closed |
| 8. Explain | Conductor: invoke `human` in pr mode | Check the page file exists and the PR description links it → label `lifecycle:explained` |
| 9. Review | Conductor asks the user: "Reviewed the PR page? Anything to change?" | When the user confirms → label `lifecycle:reviewed`. If they ask for changes, record them as tickets and go back to step 7 |
| 10. Ramp | Conductor: invoke `ramp` | Check `RAMP.md` has a level 0 (break-it) result, a capacity statement and a break list, and the ramp page exists → label `lifecycle:ramped` |
| 11. Verdict | Conductor, with the user | A verdict ADR exists → label `lifecycle:verdict-<choice>` |
| 12. Retro | Conductor: invoke `cycle-retro` | `.lifecycle/CYCLE-RETRO-N.md` exists → the cycle is closed; start the next one, or stop if the verdict was Ship or Kill |

**The wu-wei marker:** wu-wei is the user's own skill and leaves no distinct artifact. On the first cycle, if step 4 has no marker, tell the user to add one line to the end of their wu-wei skill: "When finished, add the label `lifecycle:simplified` to the spec issue (or append it to the spec's `Lifecycle:` line)." Until they do, ask once after step 4 ("Has wu-wei run on the spec?") and add the label yourself on a yes.

The user can open the map or spec in `human` (map or spec mode) at any time, to see where things stand.

## Replying

When the next step is the user's, reply with only:
1. where things stand, in one line
2. the exact command, in a code block
3. "Clear the session first" whenever that step needs a fresh one

Then update STATE's `Next` line, increment `Touches`, and stop.

When the next step is conductor's, run it, check its gate, add the marker, update STATE, and then give the next command the same way.

## Interaction-load hooks (configure, don't override)

On the first cycle, offer once to add these standing preferences to the Wayfinder map's **Notes** and to the project's `CLAUDE.md`:
- "Ask grilling questions as a short decision sheet: each question in at most two lines, with a proposed default; the user edits only what's wrong."
- "Prototype choices belong to the user. Never pick a variant and close the ticket."

Only add them if the user agrees. Don't edit other skills' files. Later changes to these hooks come through `cycle-retro`.

## Circuit breaker

Update the appetite spent at every step. If spent exceeds appetite, or a step is clearly heading past it, stop routing and go to Verdict. Never extend the appetite silently.

## Value check

At every step, write one line into STATE: *is this cycle still on track to reach its destination within its appetite, and is that destination still worth reaching?* If the answer is no, tell the user now, not at Verdict.

## Verdict

Open the ramp's `human` page and summarize it briefly:
- the destination versus what was delivered
- appetite spent
- the ramp capacity statement and the top breaks

Ask for one choice:
- **Ship:** this destination is good enough to release
- **Continue:** the next cycle's destination is the next level of maturity, starting from the break list
- **Re-shape:** same goal, new approach or appetite
- **Kill**

Record the verdict as an ADR, add the verdict label, and add the cycle to Lifecycle in STATE. Then invoke `cycle-retro`.

For the next cycle's route: if the break list is foggy, the user charts a new Wayfinder map from it (`/wayfinder` with the break list as input). If it is clear, go straight to grill-with-docs or to-spec.
