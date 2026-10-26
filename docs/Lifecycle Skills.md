Review set · 5 skills

# Lifecycle Skills

A thin layer around Matt Pocock's skills that carries an idea from inception POC to production, one fresh session at a time. Conductor navigates, the four helpers do the work Pocock's skills don't cover, and every step leaves a marker conductor can check.

[conductor](#conductor) [seam-lock](#seam-lock) [ramp](#ramp) [human](#human) [cycle-retro](#cycle-retro)

## One cycle

Clear the session, run `/conductor`, run the command it gives you. Repeat.

You type it or decideConductor runs it

1. YouChart the map`/wayfinder`Foggy route only
2. YouWalk the map, one ticket per session`/wayfinder <map>`Foggy route only
3. YouGrill`/grill-with-docs`Clear route only
4. YouWrite the spec`/to-spec`
5. YouSimplify`/wu-wei`lifecycle:simplified
6. YouSlice into tickets`/to-tickets`
7. ConductorLock the seams`seam-lock`lifecycle:seams-locked
8. YouBuild in parallel`/implement-spec`Runs /code-review inside
9. ConductorExplain the PR`human · pr`lifecycle:explained
10. YouReview the page`conductor asks`lifecycle:reviewed
11. ConductorRamp`ramp`lifecycle:ramped
12. YouVerdict`conductor asks`lifecycle:verdict-\*
13. ConductorRetro`cycle-retro`Proposes edits

After the Verdict, Continue or Re-shape starts the next cycle with a more demanding destination, seeded by the ramp's break list.

Skill · 145 lines

## `conductor`

Navigator. Run it at the start of every fresh session.

Trigger descriptionNavigator for a product's whole lifecycle across many fresh sessions: reads state, says the exact next command, runs agent-callable steps, guards appetite and value.

Read the full SKILL.md

Skill · 64 lines

## `seam-lock`

Commits contracts, stubs and fixtures, then attacks the split.

Trigger descriptionAfter to-tickets and before implement-spec: commit contracts, stubs and golden fixtures, amend the tickets to point at them, and run an adversarial review of the split.

Read the full SKILL.md

Skill · 94 lines

## `ramp`

Break-it pass, then real data at rising volume and variety.

Trigger descriptionPressure-test a built pipeline: an adversarial break-it pass first, then real data at rising volume and variety, to find where it breaks, revalidate the algorithm, and produce a capacity statement and break list.

Read the full SKILL.md

Skill · 82 lines

## `human`

Turns machine artifacts into a page you can decide from.

Trigger descriptionTurn a machine artifact (PR, ramp report, spec, or Wayfinder map) into a beginner-friendly, highly visual, self-contained HTML page a person can understand and decide from.

Read the full SKILL.md

Skill · 55 lines

## `cycle-retro`

Measures the cycle and proposes edits to the workflow.

Trigger descriptionRetrospective on a whole development cycle across sessions: find where the workflow wasted interaction, defaults were wrong, or decisions reversed, and propose concrete skill and steering edits.

Read the full SKILL.md

Install by copying each folder into your skills directory, then add the one marker line to the end of your wu-wei skill.