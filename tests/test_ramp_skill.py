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

    def test_map_card_carries_entry_point_contract(self):
        body = self.section("--map")
        for need in ["ramp_run.py", "<step>", "exit 0", "exit 1", "exit 2"]:
            self.assertIn(need, body)

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


if __name__ == "__main__":
    unittest.main()
