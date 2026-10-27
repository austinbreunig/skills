# Skills

A published set of Claude Code skills in two families: lifecycle skills that carry a product from idea to production, and productivity skills that give one person awareness across all their projects.

## Families

**Lifecycle skill**:
A skill in `lifecycle/` that moves one product through a development cycle, layered on Matt Pocock's skills.
_Avoid_: development skill, workflow skill

**Productivity skill**:
A skill in `productivity/` that serves the person across many projects, not one product.
_Avoid_: personal skill, utility skill

**Shared skill**:
A skill both families use that belongs to neither, such as `human`.
_Avoid_: common skill, core skill

## Lifecycle

**Human step**:
A decision only the user can make, such as the destination, a sign-off or the Verdict. `/lifecycle` stops only at these, and each one counts as a touch.
_Avoid_: user step, approval gate, checkpoint

**Agent step**:
Any step that isn't a human step. `/lifecycle` runs these back to back, each in its own subagent, until it reaches a human step or a step fails.
_Avoid_: automatic step, auto step

**Destination**:
What one cycle aims to reach, anywhere from a POC exploration to a deployed final product.
_Avoid_: scope, goal, phase

**Main map**:
The wayfinder map that clears the fog on the product itself: its concepts, algorithms and architecture.
_Avoid_: design map, product map

**Tracer pipeline**:
The thinnest end-to-end version of the pipeline, built so a ramp has something real to run on.
_Avoid_: prototype, POC, skeleton

**Tracer map**:
The wayfinder map that decides the tracer pipeline. Charted alongside the main map when a cycle needs a ramp.
_Avoid_: pipeline map

**Ramp map**:
The wayfinder map, charted by `/ramp`, that decides the ramp plan. Its destination is one spec for the ramp harness. Charted only after the tracer pipeline is built.
_Avoid_: test map

**Spec sign-off**:
The user's approval of a spec, together with its tickets and locked seams, from its human page.
_Avoid_: spec review, plan approval

**PR sign-off**:
The user's approval of a built spec's pull request, from its human page.
_Avoid_: code review, merge approval

**Lens**:
The mode where `/mindful` stays on through a session and asks one question only when something is being forced or added without need.
_Avoid_: watch mode, background check

**Review**:
The mode where `/mindful` judges a finished spec (or its tickets, or a built branch) for shape and approach, applies its cuts directly, and writes each cut and why on the spec so the user can accept or undo it at spec sign-off.
_Avoid_: audit, simplicity gate, wu-wei pass

**Entry point**:
The one command that takes an input and an output location and runs the whole pipeline. `/ramp` won't plan without one.
_Avoid_: main script, runner

**Ramp plan**:
The levels a pipeline is pushed through, with the number checks and judgment checks for each level, and where the user gives feedback.
_Avoid_: ramp config, test plan

**Ramp harness**:
The test scaffold, kept in the pipeline's own repo, that runs the pipeline through each level of a ramp plan and reports how it held up.
_Avoid_: test suite, scaffold, QA rig

**Break-it pass**:
The cheap step before level 1, where made-up hostile inputs try to make the pipeline fail. Its tests are kept as a regression suite.
_Avoid_: level 0, fuzzing pass

**Number check**:
A limit the agent can test alone at a level, such as peak memory, quarantine rate or accuracy on golden fixtures.
_Avoid_: metric, quantitative check, threshold

**Judgment check**:
A call only the user can make at a level, by looking at samples of the output.
_Avoid_: qualitative check, manual review, eyeball test

**Run ramp**:
The `/lifecycle` agent step that runs the built ramp harness level by level, stops only at judgment checks or failures it can't fix with a small change, and writes `RAMP.md`. The user gives judgment calls as comments on a ticket per check.
_Avoid_: ramp run, execute ramp, ramp test

## Productivity

**HQ repo**:
The user's private GitHub repo, named at setup, that holds the connected-repo list, EOD compilations, jots and saved repo pages.
_Avoid_: headquarters, home repo, state repo

**HQ folder**:
The local clone of the HQ repo on one computer, chosen at setup and recorded in `~/.config/hq/config`.
_Avoid_: HQ path, local HQ, workspace

**Connected repo**:
A GitHub repo the user has added to HQ, so brief and EOD track it. Stored as `owner/name`, never a local path. Its issues on GitHub are the source of truth for its work.
_Avoid_: project, tracked repo, linked repo

**Jot**:
A very short note the agent writes from what the user says mid-session, kept in the HQ repo for 7 days and shown in EOD and brief under its repo.
_Avoid_: note, memo

**EOD compilation**:
The day's record in the HQ repo: per connected repo, what the sessions covered, issue activity and action items.
_Avoid_: EOD report, daily log, recap

**Brief**:
An at-a-glance view of every connected repo: what was done last time and where things stand now. Shown on its own, and at the end of every EOD.
_Avoid_: morning brief, status report, standup

## Shared

**Human page**:
A self-contained, visual HTML page made by `human` that turns any context into something a person can understand and reason about at their reader level.
_Avoid_: show-me doc, report page, explainer

**Human explanation**:
The in-chat version of what `human` makes, with the same parts as a human page but drawn in plain text.
_Avoid_: summary, recap, re-pitch

**Reader level**:
How much the reader already knows (newbie, beginner, proficient or master), which sets the words, background and questions `human` uses.
_Avoid_: audience, skill level, difficulty

**Think-it-through box**:
The box at the top of every human page and human explanation: the question in front of the reader and 2–4 guiding questions that point to the sections that help, or "Nothing to decide, just read." It never recommends.
_Avoid_: decision box, recommendation, TL;DR
