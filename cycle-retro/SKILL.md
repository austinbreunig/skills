---
name: cycle-retro
description: Retrospective on a whole development cycle across sessions: find where the workflow wasted interaction, defaults were wrong, or decisions reversed, and propose concrete skill and steering edits.
---

# Cycle Retro

Pocock's `/retro` improves the *code environment* for one session: checks, standards, navigation. This skill improves the *workflow* across a whole cycle. Its aim is that each cycle needs fewer interruptions, has fewer wrong defaults, and reverses fewer decisions than the last. That is how the workflow earns trust you can walk away from.

It proposes changes. It never applies edits to skills or steering files without the user's approval.

Inputs (follow pointers; don't load everything):
- `.lifecycle/STATE.md`: the destination, appetite, touches and verdict for this cycle
- the ADRs created or superseded during the cycle
- the Wayfinder map (if there was one) and its decision summaries
- the decision sheets and their edits (in tickets, ADRs or STATE)
- the seam-lock adversary findings, `RAMP.md` (including the level 0 break-it result), and the `human` pages
- `CYCLE-RETRO` notes from earlier cycles, to spot repeat problems

## 1. Measure the cycle

Calculate these from the sources. Don't estimate.
- **Touches:** the number of times the user had to act, split by kind (commands, decision sheets, prototype choices, reviews, escalations).
- **Default hit rate:** of the defaults proposed in decision sheets, how many the user accepted unchanged.
- **Appetite accuracy:** spent versus budgeted, and which step overran.
- **Reversals:** decisions closed and later superseded, with when each was caught (seam-lock, build, review, ramp, verdict).
- **Escapes:** breaks found at a later, costlier stage that an earlier stage could have caught. For example, a real-data ramp break that the level 0 break-it pass, a golden fixture or seam-lock's adversary should have found.

Compare with earlier cycles, where they exist.

## 2. Find candidates, in these categories

- **Wasted interaction:** touches that changed nothing, such as defaults always accepted or questions already answered in an ADR. Fix: widen what the agent may decide alone, or improve the defaults.
- **Wrong defaults:** patterns in what the user corrected. Fix: a standing preference (map Notes, CLAUDE.md) or an edit to the skill that drafted the default.
- **Late discovery:** reversals and escapes. Identify the step that should have caught each one. Fix: a new golden fixture, a break-it attack, a variety stratum, a contract convention, or a new line in the adversary's brief.
- **Appetite drift:** steps that overran repeatedly. Fix: better appetite guidance in conductor, or splitting that step.
- **Context pressure:** sessions that overflowed or needed `/handoff`. Fix: smaller tickets, better pointers, or moving a step into a subagent.
- **No-ops:** instructions in our skills that never changed behavior this cycle. Fix: delete them (kanso).

The scope covers `conductor`, `seam-lock`, `ramp`, `human`, `cycle-retro` itself, and steering text such as the map's Notes and `CLAUDE.md`. Don't propose edits to Pocock's skills. Where one of them is the cause, propose a standing preference in Notes or `CLAUDE.md` instead, and suggest a fork only if a preference can't fix it.

## 3. Propose

Present at most five candidates, most severe first. Each one gets:
- the evidence (a link or a number)
- the exact proposed edit, as a short diff or the new line
- the expected effect, e.g. "removes about 3 touches per cycle"

Apply only the edits the user approves.

## 4. Record

Write `.lifecycle/CYCLE-RETRO-N.md` with the metrics, the candidates, and which edits were applied. Add one line to the cycle's Lifecycle entry in STATE: touches, default hit rate, appetite accuracy.

If the cycle's heaviest session (usually implement-spec) had code-environment problems, such as missed checks or slow navigation, suggest the user run `/retro` on that session.
