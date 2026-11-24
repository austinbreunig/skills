"""Shape tests for lifecycle/skills/ramp/SKILL.md.

One test per "Done when" line in docs/scope/ramp-harness/scope.md.
They check the skill's text, not live behaviour.
"""
import re
import unittest
from pathlib import Path

SKILL = Path(__file__).parent.parent / "lifecycle/skills/ramp/SKILL.md"


def sections(text):
    """Map each '## ' heading to its body."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return {parts[i].strip().lower(): parts[i + 1] for i in range(1, len(parts), 2)}


class RampSkill(unittest.TestCase):
    def setUp(self):
        self.text = SKILL.read_text()
        self.sec = sections(self.text)

    def section(self, word):
        for name, body in self.sec.items():
            if word in name:
                return body.lower()
        self.fail(f"no section with '{word}' in its heading")

    def test_frontmatter(self):
        self.assertRegex(self.text, r"\A---\nname: ramp\ndescription: .+\n---\n")

    def test_map_stops_without_pipeline_interface(self):
        body = self.section("--map")
        self.assertIn("not ready to ramp", body)
        self.assertIn("stop", body)

    def test_map_writes_one_card_from_template(self):
        body = self.section("--map")
        for need in ["interval count", "size", "qa check", "at least one", "log path", "scope.md"]:
            self.assertIn(need, body)

    def test_one_contract_section_holds_entry_point_rules(self):
        body = self.section("contract")
        for need in ["ramp_run.py", "<step>", "exit 0", "exit 1", "exit 2"]:
            self.assertIn(need, body)

    def test_exit_codes_are_stated_once(self):
        self.assertEqual(self.text.lower().count("exit 2"), 1)

    def test_map_puts_contract_in_the_card(self):
        self.assertIn("contract", self.section("--map"))

    def test_run_one_step_prints_qa_results(self):
        body = self.section("--run")
        self.assertIn("ramp_run.py", body)
        self.assertIn("<step>", body)
        self.assertIn("qa results", body)

    def test_run_stops_at_first_failing_qa_check(self):
        body = self.section("--run")
        self.assertRegex(body, r"qa check.{0,80}(fail|stop)|(fail|stop).{0,80}qa check")
        self.assertIn("no later", body)

    def test_run_stops_at_first_pipeline_crash(self):
        body = self.section("--run")
        self.assertIn("crash", body)

    # --- #35: logging and report ---

    def test_log_holds_pipeline_and_qa_lines(self):
        body = self.section("contract")
        self.assertIn("pipeline log", body)
        self.assertIn("qa diagnostic", body)
        self.assertIn("log path", body)

    def test_log_line_format_is_fixed(self):
        body = self.section("contract")
        for need in ["`pipeline`", "`qa`", "`pass`", "`fail`"]:
            self.assertIn(need, body)

    def test_log_flushed_when_run_fails_midway(self):
        body = self.section("contract")
        self.assertIn("flush", body)
        self.assertIn("midway", body)

    def test_report_written_after_every_run(self):
        body = self.section("--run")
        self.assertIn(".md report", body)
        self.assertIn("every run", body)
        self.assertIn("crash", body)

    def test_report_lists_intervals_checks_and_pass_fail(self):
        body = self.section("--run")
        for need in ["each interval", "diagnostic check", "pass", "fail"]:
            self.assertIn(need, body)


if __name__ == "__main__":
    unittest.main()
