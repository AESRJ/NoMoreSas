"""Exercise state gates that prevent an invalid implementation handoff."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts/check_harness.py"
spec = importlib.util.spec_from_file_location("harness", MODULE_PATH)
harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harness)


class Gates(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        directory = self.root / "specs/001-test"
        directory.mkdir(parents=True)
        for name, text in [("spec.md", "Acceptance"), ("plan.md", "Plan"),
                           ("tasks.md", "- [ ] T001 Implement\n")]:
            (directory / name).write_text(text, encoding="utf-8")
        self.features = [{"id": "001-test", "status": "in_progress", "owner": "claude-code",
                          "spec_dir": "specs/001-test"}]
        self.handoff = dict(feature_id="001-test", status="ready", planner="codex",
                            executor="claude-code", spec_dir="specs/001-test",
                            task_ids=["T001"], allowed_paths=["src"], blockers=[],
                            verification_commands=["python -m unittest discover -s tests"],
                            implementation_report="progress/impl_test.md", review_report="progress/review_test.md")

    def check(self):
        harness.validate_handoff(self.root, self.handoff, self.features, implementation=True)

    def test_complete_handoff_is_accepted(self):
        self.check()

    def test_draft_cannot_start_implementation(self):
        self.handoff["status"] = "draft"
        with self.assertRaises(harness.InvalidHarness):
            self.check()

    def test_missing_plan_is_rejected(self):
        (self.root / "specs/001-test/plan.md").unlink()
        with self.assertRaises(harness.InvalidHarness):
            self.check()

    def test_completed_task_is_rejected(self):
        (self.root / "specs/001-test/tasks.md").write_text("- [x] T001 Done\n", encoding="utf-8")
        with self.assertRaises(harness.InvalidHarness):
            self.check()

    def test_blockers_are_rejected(self):
        self.handoff["blockers"] = ["No stack"]
        with self.assertRaises(harness.InvalidHarness):
            self.check()

    def test_multiple_active_features_are_rejected(self):
        self.features.append(dict(self.features[0], id="002-test"))
        with self.assertRaises(harness.InvalidHarness):
            harness.validate_features(self.root, dict(schema_version=1, features=self.features))

    def test_path_outside_repository_is_rejected(self):
        self.handoff["allowed_paths"] = ["../outside"]
        with self.assertRaises(harness.InvalidHarness):
            self.check()

    def test_wrong_executor_is_rejected(self):
        self.handoff["executor"] = "codex"
        with self.assertRaises(harness.InvalidHarness):
            self.check()

    def test_inactive_feature_is_rejected(self):
        self.features[0]["status"] = "pending"
        with self.assertRaises(harness.InvalidHarness):
            self.check()


if __name__ == "__main__":
    unittest.main()
