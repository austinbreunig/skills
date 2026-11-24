1: --map's harness card says ramp_run.py wraps the pipeline and exposes its pipeline logs | built | agent's choice
2: card says ramp_run.py adds QA diagnostic lines | built | agent's choice
3: card says both go to the log path set in the map | built | agent's choice
4: card says the log is flushed even when the run fails midway | built | agent's choice
5: --run writes a .md report after every run, on QA fail and crash too, next to the log path | built | agent's choice
6: report lists each interval, each diagnostic check, pass or fail | built | agent's choice
Tests: 4 more shape tests in tests/test_ramp_skill.py, text only | built | agent's choice
5b: log line format fixed: PIPELINE / QA <interval> <check> PASS|FAIL (door 1, fixed now) | built | user
