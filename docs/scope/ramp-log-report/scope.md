## Goal
A ramp run leaves a log and a report the user can read.

## Path
1. The harness entry point wraps the pipeline and exposes its logs.
2. The entry point adds its own log lines for each QA diagnostic.
3. The entry point writes both to the log path set in the map.
4. The entry point flushes the log even when the run fails midway.
5. After every /ramp --run, failed or not, ramp writes a .md report from the log.
6. The report lists each interval, its diagnostic checks, and pass or fail for each.

## In
- Pipeline logs and QA diagnostic logs.
- Log path set in the map (#30).
- Report: a .md file that synthesizes the log.

## Out
- Choosing intervals, sizes and QA checks (#30).

## Done when
- After a run, the log holds pipeline lines and QA diagnostic lines.
- After a run that fails midway, the log file exists with lines up to the failure.
- After every /ramp --run, a .md report exists, even after a failed check or a crash.
- The report lists each interval run, each diagnostic check, and pass or fail.

## Assumptions
- /ramp --run writes the report, no new mode: confirmed
- ramp_run.py from #30 is the harness entry point: confirmed

## Decisions
- Report after every run, failed or not (user)
- Log path is set in the map (user)
- Harness entry point writes the log (user)
- Report shows diagnostic checks with pass or fail (user)
