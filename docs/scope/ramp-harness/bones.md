1: /ramp --map is a section in lifecycle/skills/ramp/SKILL.md | built | agent's choice
2: --map stops with "Not ready to ramp" when no pipeline interface | built | agent's choice
3: --map asks interval count, size, QA checks, log path in one round | built | agent's choice
4: --map writes one /scope-format card at docs/scope/<slug>/scope.md | built | agent's choice
5: --run <step> calls `python ramp_run.py <step>`, shows QA results | built | agent's choice
6: --run loops s0..sN, stops on exit 1 (QA fail) or exit 2 (crash) | built | agent's choice
Tests: tests/test_ramp_skill.py, text-shape checks only (skill is prose; no live run) | built | agent's choice
