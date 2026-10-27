---
name: lifecycle
description: Carries one product through a development cycle across fresh sessions. Works out where the cycle stands, runs every agent step back to back (each in its own subagent), and stops only at decisions only the user can make, with the exact next command.
---

# Lifecycle

The user runs `/lifecycle` at the start of any fresh session. It means: *where are we, and what's next?*

## The rule

- A **human step** is a decision only the user can make: the destination, the route, sign-offs, the Verdict, and running the commands lifecycle never wraps.
- Everything else is an **agent step**.

One run chains agent steps, each in its own subagent, until it reaches a human step or a step fails. Then it replies (see **Replying**) and stops.

Lifecycle navigates; it does not override. It decides order, keeps state and checks gates. It never tells another skill *how* to do its work, and never wraps `wayfinder`, `grill-with-docs` or `implement-spec`: those are always the user's to run.

## Where decisions live

Nothing carries over in conversation. Each decision lives in one place, and everything else links to it:
- **The cycle's build plan:** the spec issue (with its tickets, seams and mindful's cuts)
- **Build-time decisions:** ADRs, wherever `setup-matt-pocock-skills` configured them
- **Lifecycle's memory:** `.lifecycle/STATE.md`, pointers only

## Markers

Every step leaves something you can see: a spec, tickets, a PR, a comment, a page, or a **label on the cycle's spec issue**:

- `lifecycle:simplified`: mindful has reviewed the spec (mindful adds it)
- `lifecycle:seams-locked`: contracts, stubs and fixtures are committed, the tickets have Seams sections, and the adversary pass is closed
- `lifecycle:spec-signed-off`: the user signed off the spec, its tickets, seams and mindful's cuts
- `lifecycle:explained`: the PR's human page exists and the PR description links it
- `lifecycle:reviewed`: the user signed off the PR
- `lifecycle:verdict-<ship|continue|reshape|kill>`: the verdict is recorded

Rules:
- **A label means checked, not just ran.** Add a label only after checking the step's outputs directly (the gates below), whoever ran the step.
- Outputs exist but the label is missing (the step was run by hand): check them and add the label.
- A label exists but its outputs are missing or broken: remove it, say so in one line, and redo the step.
- Create a label first if the repo lacks it. If the tracker has no labels (e.g. local markdown), keep a `Lifecycle:` line in the spec's body listing the markers.
- The spec is per cycle, so the markers reset each cycle on their own.

## STATE.md (a cache, under ~80 lines; link, never paste)

```
## Product
One line: what this is and who it serves.

## Lifecycle
One line per finished cycle: N, destination, verdict, touches, default hit rate, links to the human pages and retro.

## Current cycle
Cycle: N
Destination: e.g. "POC proving the change-detection algorithm on one county"
Route: map | grill
Ramp: yes | no
Spec: link
Step: the current step
Next: the exact command or action
Touches: count of human steps so far, with the kind of each
Links: tickets, contracts, integration branch, PR, human pages
Open questions: on the spec, or none
Value check: one line, updated at every step
```

STATE is a cache. When it disagrees with the tracker or the repo, the artifacts win: correct STATE and say so in one line.

## Starting a cycle

On the first run (no `.lifecycle/STATE.md`), or after a Verdict of Continue or Re-shape, ask in **one message** for whatever isn't already known:

1. **Destination:** what this cycle aims to reach. Destinations get more demanding as the product matures (POC → MVP → hardened production → scale); they are chosen each cycle, never a fixed sequence.
2. **Route:**
   - **map:** the way to the destination can't be seen yet, or the work spans many sessions of deciding.
   - **grill:** the work fits in one session of deciding.
   Say which you'd pick and why in one line; the user decides.
3. **Ramp:** does this cycle need a ramp (a planned pressure test of the pipeline)? Yes or no. No default.

Skip any question already answered: by STATE, by the verdict ADR, or by the user's own message. On Continue or Re-shape, keep answers that still hold and ask only the rest.

Write the answers to STATE and count one touch. The user can change **Ramp** until the cycle's spec exists; after that it is fixed.

On the first cycle, also make the **interaction-load hooks** offer (below).

## Finding the next step

On every run:
1. Read STATE to find the current cycle and its spec.
2. Go down the table in order. For each step, check its gate against the real artifacts: issues, labels, comments, branches, files.
3. Any step with outputs but a missing marker gets checked and labelled on the way.
4. The **first step whose gate is not met** is the next step. If it is an agent step, run it (see **Running agent steps**) and go on to the next. If it is a human step, reply and stop.

### Grill route

| # | Step | Kind | Gate: done when |
|---|---|---|---|
| G1 | Grill and spec | human: `/grill-with-docs`, then `/to-spec` in the same session | A spec issue created after this cycle started exists; record its link in STATE |

Then the spec chain.

### Spec chain

| # | Step | Kind | Gate: done when |
|---|---|---|---|
| S1 | Mindful review of the spec | agent: `lifecycle:mindful <spec>` | Label `lifecycle:simplified` and a `## Mindful review` comment on the spec |
| S2 | Tickets | agent: to-tickets worker (below) | Implementation tickets that reference the spec exist, with blocking edges |
| S3 | Lock seams | agent: `lifecycle:seam-lock <spec>`. Skipped for the ramp harness spec | Contracts and fixtures committed and the harness runs; every ticket has a Seams section; adversary findings fixed or written on the spec as open questions → label `lifecycle:seams-locked` |
| S4 | Mindful on tickets and seams | agent: `lifecycle:mindful <spec's tickets and seams>` | A `## Mindful review` comment on the spec newer than S3's (or S2's, when S3 was skipped) |
| S5 | Spec page | agent: `human:human spec <spec>` | The spec page exists in `.lifecycle/human/` and is newer than S4's comment |
| S6 | **Spec sign-off** | human (see **Sign-offs**) | Label `lifecycle:spec-signed-off` |

### Build chain

| # | Step | Kind | Gate: done when |
|---|---|---|---|
| B1 | Build | human: `/implement-spec <spec>`, in a fresh session | The integration-branch PR is open and every implementation ticket is closed |
| B2 | Mindful on the branch | agent: `lifecycle:mindful <branch>` | A `## Mindful review` comment on the PR newer than the last ticket closed |
| B3 | Simplify | agent: `/simplify` on the branch; the worker ends by posting a `## Simplify pass` comment on the PR listing its commits (or "nothing to change") | That comment exists, newer than B2's |
| B4 | PR description | agent: `mattpocock-skills:pr`, rewriting the PR's description | (covered by B5: rerun B4 whenever B5 runs) |
| B5 | PR page | agent: `human:human pr <PR>` | The page exists and the PR description links it → label `lifecycle:explained` |
| B6 | **PR sign-off** | human (see **Sign-offs**) | Label `lifecycle:reviewed` |

Then the Verdict (human) and the Retro.

**Not in this skill yet:** the map route's steps and the ramp steps. Until they are added, on the map route tell the user to chart and walk the map with `/wayfinder`, then write the spec with `/to-spec <map>`, then run `/lifecycle`; the spec chain starts from there. A cycle with Ramp: yes goes from PR sign-off straight to the Verdict.

## Running agent steps

Run each agent step in its own fresh subagent. Give it pointers only: the skill to follow (by full name), the target (spec, tickets, branch or PR), and this line:

> This is an agent step in a lifecycle run. Don't stop to ask. Write anything the user must decide on the spec issue as an open question; it is reviewed at spec sign-off.

When the subagent returns, check the step's gate yourself. Gate met → add its marker, update STATE (`Step`, `Links`, `Value check`), and go on. Gate not met → that is a failure: stop and reply.

### to-spec and to-tickets workers

Pocock's `to-spec` and `to-tickets` can't be called as skills by an agent. A worker follows their files instead:

1. Find the installed `mattpocock-skills` plugin's `SKILL.md` by skill name, not by version folder: search `~/.claude/plugins/` for paths that contain `mattpocock-skills` and end in `/to-tickets/SKILL.md` (or `/to-spec/SKILL.md`). If there are several, use the one most recently modified.
2. Follow it, with one change: every step that checks with the user ("check the seams with the user", "Quiz the user", "iterate until the user approves") becomes "this is reviewed at spec sign-off". Publish without waiting.
3. Not found: stop and reply with the command for the user to run themselves, e.g.:

   ```
   /to-tickets <spec> publish, approval is at sign-off
   ```

   then `/lifecycle` again. Count it as a touch.

## Sign-offs

### Spec sign-off

Reply with the spec page's path, the open questions on the spec (if any), and the two ways forward:
- **Sign off:** `/lifecycle signed off`. This covers the spec, its tickets, its seams and mindful's cuts. Add `lifecycle:spec-signed-off`.
- **Push back:** comment on the spec issue with what to change (any of mindful's cuts can be undone this way), then `/lifecycle`.

**Push back.** On every run before spec sign-off, look for the user's comments on the spec issue that are newer than the spec page and have no `## Lifecycle revision` reply. For each:
1. Make the change: edit the spec, tickets or seams, or restore a cut as its Undo line says.
2. Find the first step the change affects: the spec's scope or stories → S1; how the work is sliced → S2; contracts, fixtures or conventions → S3; restoring a cut → S4.
3. Remove the markers of that step and every later one, then rerun the chain from there.
4. Reply on the spec issue with a `## Lifecycle revision` comment: what changed, and the step the chain reran from.

### PR sign-off

Reply with the PR page's path and the two ways forward:
- **Sign off:** `/lifecycle reviewed`. Add `lifecycle:reviewed`.
- **Ask for changes:** list them in the `/lifecycle` message or as PR comments. Each change becomes a ticket that references the spec. Remove `lifecycle:explained`, then reply with `/implement-spec <spec>` (clear the session first). After the build, the build chain runs again from B2.

## Replying

When a run stops, reply with only:
1. where things stand, in one line (and what failed, if a step failed)
2. the exact command, in a code block
3. "Clear the session first" whenever that step needs a fresh one (`/grill-with-docs`, `/implement-spec`, `/wayfinder`)

Then set STATE's `Next` line. If the stop is a human step, add one to `Touches` with its kind.

## Value check

At every step, write one line into STATE: *is this cycle still on track to reach its destination, and is that destination still worth reaching?* If the answer is no, stop and tell the user now, not at the Verdict.

## Interaction-load hooks (configure, don't override)

On the first cycle, offer once to add these standing preferences to the project's `CLAUDE.md` (and the map's **Notes**, on the map route):
- "Ask grilling questions as a short decision sheet: each question in at most two lines, with a proposed default; the user edits only what's wrong."
- "Prototype choices belong to the user. Never pick a variant and close the ticket."

Only add them if the user agrees. Don't edit other skills' files. Later changes come through `cycle-retro`.

## Verdict

After PR sign-off, summarize briefly from the human pages:
- the destination versus what was delivered
- what is still untested or broken

Ask for one choice:
- **Ship:** this destination is good enough to release
- **Continue:** the next cycle aims at the next level of maturity
- **Re-shape:** same goal, new approach
- **Kill**

Record the verdict as an ADR, add the verdict label, and add the cycle to Lifecycle in STATE.

## Retro

Run `lifecycle:cycle-retro` in this session (it asks the user which edits to apply). The cycle is closed once `.lifecycle/CYCLE-RETRO-N.md` exists. Then start the next cycle, or stop if the verdict was Ship or Kill.
