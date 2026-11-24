## Goal
/ramp scopes a harness for a built pipeline, then runs it.

## Path
1. User runs /ramp --map on a project with a pipeline.
2. Ramp stops if no pipeline interface exists.
3. A template asks the user for the interval count and each interval's size.
4. The template asks for one or more QA checks per interval, and a log path.
5. Ramp writes one scope card for the whole harness.
6. /ramp --run <step> runs one interval and its QA checks.
7. /ramp --run restarts and runs every interval until a failure.

## In
- Pipeline: a BigQuery callable or a simple Python script.
- QA checks per interval: performance and data quality.
- Interval count and size are the user's choice.

## Out
- Deciding whether a project needs ramping.
- Logging and the report (#35).

## Done when
- /ramp --map with no pipeline interface stops with a message.
- /ramp --map writes one complete scope.md with at least one QA check per interval and a log path.
- /ramp --run s0 runs only s0 and prints its QA results.
- /ramp --run stops at the first failing QA check and runs no later interval.
- /ramp --run stops at the first pipeline crash and runs no later interval.

## Assumptions
- Pipeline interface exists first: confirmed (stop if not)
- User decides if a project needs ramping: confirmed

## Decisions
- Two modes, --map and --run (user)
- One scope card per harness, even with many components (user)
- Logging and report are a separate ticket (user) → #35

