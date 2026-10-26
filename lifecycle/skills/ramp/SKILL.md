---
name: ramp
description: Plan how to pressure-test a built pipeline. Charts a wayfinder map whose destination is one spec for a ramp harness. Planning only; nothing is run.
---

# Ramp

The pipeline works end to end. The next question is where it breaks. This skill plans how to find out. It does not run anything.

The output is a **ramp map**: a wayfinder map with three grilling tickets. Walking that map ends in one spec for a **ramp harness**. The harness is then built like any other spec. Running it, and writing `RAMP.md`, is lifecycle's **Run ramp** step, not this skill.

Walking the map is plain `/wayfinder <map>`. This skill only charts it.

## 1. Check the entry point

A ramp needs something to run. Look for one **entry point**: a single command that takes an input and an output location and runs the whole pipeline. Check the README, the CLI, scripts and the code.

If there is none, stop. Say:

> Not ready to ramp: no single entry point that takes an input and an output location and runs the pipeline. Build that first.

Add one line on what is missing (e.g. "stages run one by one", "no output option"). Do nothing else.

## 2. Find how far the ramp goes

- **With lifecycle** (`.lifecycle/STATE.md` exists): read the cycle's **Destination**. Don't ask.
- **Alone** (no `.lifecycle/`): ask "How far should this ramp go?", with one example (e.g. "one county, or the full national load?"). Wait for the answer.

Also check whether the repo already has a ramp harness. If it does, the plan extends it rather than starting over.

## 3. Small ramp? Skip the map

If one grilling session could settle all three seed questions below (e.g. one dataset, one or two levels, no new harness parts), ask the user once:

> This ramp looks small. Skip the map? We'd do one `/grilling` session on the three questions, then `/to-spec`.

If yes, list the three questions and stop. Otherwise, chart the map.

## 4. Chart the map

Find wayfinder's installed `SKILL.md` by name: search `~/.claude/plugins/` for a path ending in `wayfinder/SKILL.md`. If there are several versions, use the newest. Follow its **Chart the map** steps, with these changes:

1. **Destination is fixed.** Don't grill for it. Use: "One spec issue for the ramp harness of `<pipeline>`, ramping to `<how far>`, ready for `/to-tickets`."
2. **Frontier is fixed.** Don't run the breadth-first grilling. The frontier is the three seed tickets below.
3. **Create the map** as wayfinder says. Put in **Notes**: the entry point command, any existing harness, and the plan rules below. Sketch any fog you can already see (e.g. data you don't have yet) in **Not yet specified**.
4. **Create the three seeds** as child issues of the map, each labelled `wayfinder:grilling`. Then, in a second pass, wire native blocking: 2 is blocked by 1, and 3 is blocked by 2. Use the tracker's native blocking, as wayfinder says. A body note is only for trackers that have none.
5. **No research step.** The seeds are all grillings.
6. **Stop.** Charting resolves nothing.

If wayfinder's `SKILL.md` can't be found, don't guess. Print the destination, notes and seeds, and tell the user to run `/wayfinder` with them.

### The three seeds

1. **Grilling: ramp levels and the break-it pass.** What levels does this ramp climb (level 1 is the smallest real run, the baseline), and what does the break-it pass attack before level 1?
2. **Grilling: checks for each level.** Blocked by 1. What number checks and judgment checks does each level need to pass?
3. **Grilling: what the harness needs beyond running the pipeline.** Blocked by 2. QA scripts, a sample pack for judgment checks, the report, and anything else the checks need.

### Plan rules (copy into the map's Notes)

- The **break-it pass** comes before level 1. Made-up hostile inputs try to make the pipeline fail. Levels are numbered from 1.
- **Number checks** are relative to level 1. They are absolute only when the destination states a hard limit (e.g. "under 2 hours").
- **Judgment checks** are the user's call, made by looking at samples. The user gives feedback in ticket comments.
- A level passes only when both its number checks and its judgment checks pass.
- The harness lives in the pipeline's own repo and is kept across cycles. Its break-it tests become a permanent regression suite.
- The harness must give Run ramp what `RAMP.md` holds: the break-it result, a capacity statement ("holds to X, slows at Y, breaks at Z because W"), a levels-vs-checks table, how accuracy changed across levels, a break list, the fixes made, and each judgment call linked to the user's comment.

## 5. Hand-off

- **With lifecycle:** in `.lifecycle/STATE.md`, link the ramp map and set Next to `/wayfinder <map>`.
- **Alone:** skip STATE.md.

End with a plain report, at most five lines: the entry point, how far the ramp goes, the map link, the three seed tickets, and the next command: `/wayfinder <map>`.
