---
name: ramp
description: Plan and run a ramp of a built pipeline. /ramp --map scopes a ramp harness. /ramp --run runs the built harness, one interval or all. User-invoked.
---

# Ramp

A ramp runs a built pipeline over several intervals. Each interval raises the load. QA checks run at each interval.

Two modes. The user picks one. Ramp never decides whether a project needs ramping.

## Voice

Plain words. Short sentences. Answer first.

## /ramp --map

Plans the harness. Writes one scope card. Builds nothing.

1. **Check the pipeline interface.** Look for one entry point to the pipeline (a BigQuery callable or a Python script). Check the README, the CLI and the code. If there is none, stop. Say:

   > Not ready to ramp: no pipeline interface. Build that first.

   Add one line on what is missing. Do nothing else.

2. **Ask the template.** Plain questions, one round:
   - What is the interval count? (s0, s1, …)
   - What is the size of each interval?
   - What QA checks run at each interval? At least one each. Performance, data quality, or both.
   - What is the log path?

3. **Write one card** for the whole harness, even with many components. Use the `/scope` card format at `docs/scope/<slug>/scope.md`. Put the intervals, sizes, QA checks and log path in it. Also put the entry point contract in it, so `/bones` builds to it: `ramp_run.py <step>` runs one interval and prints its QA results. Exit 0 means all QA checks passed. Exit 1 means a QA check failed. Exit 2 means the pipeline crashed.

   Also put the log contract in it. `ramp_run.py` wraps the pipeline and exposes its pipeline logs. It adds its own QA diagnostic lines. It writes both to the log path. It flushes the log even when the run fails midway. Every pipeline line starts with `PIPELINE`. Every QA line starts with `QA`, then the interval, the check name, and `PASS` or `FAIL`.

   Ask the user to confirm it.

The card is then built with `/bones`.

## /ramp --run

Runs the built harness. The harness has one entry point, `ramp_run.py`, made by `/bones` from the card.

Contract for `ramp_run.py <step>`: it runs one interval and its QA checks, and prints the QA results. Exit 0 means all QA checks passed. Exit 1 means a QA check failed. Exit 2 means the pipeline crashed.

- **`/ramp --run <step>`:** run `python ramp_run.py <step>`. Show its QA results. Run nothing else.
- **`/ramp --run`:** start over at s0. Run each interval in order, one `ramp_run.py` call each. Show each one's QA results.
- **A QA check fails (exit 1):** stop. Say which check failed. Run no later interval.
- **The pipeline crashes (exit 2):** stop. Say which interval crashed. Run no later interval.

**Report.** After every run, failed or not, write a .md report from the log, next to the log path. Do this when a QA check failed and when the pipeline crashed too. The report lists each interval run, each diagnostic check in it, and pass or fail for each.

If `ramp_run.py` is not there, stop and say so. Tell the user to build the harness first.
