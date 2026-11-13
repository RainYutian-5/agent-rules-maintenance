import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/agent-rules-maintenance/scripts/rule_metrics.py"
spec = importlib.util.spec_from_file_location("rule_metrics", SCRIPT)
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)


class MetricsTests(unittest.TestCase):
    def test_only_outer_items_count_and_input_is_unchanged(self):
        content = "# Rules\n- First\n  - Nested\n```md\n- Example\n```\n+ Second\n1. Third\n"
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "AGENTS.md"
            path.write_text(content)
            before = path.read_bytes()
            report = metrics.measure(path)
            self.assertEqual(report["top_level_list_items"], 3)
            self.assertEqual(report["sections"], ["Rules"])
            self.assertEqual(path.read_bytes(), before)

    def test_unicode_bytes_and_empty_baseline(self):
        with tempfile.TemporaryDirectory() as folder:
            current, baseline = Path(folder) / "current.md", Path(folder) / "before.md"
            current.write_text("- 中文规则\n")
            baseline.write_bytes(b"")
            result = subprocess.run([sys.executable, str(SCRIPT), str(current), "--baseline", str(baseline)], capture_output=True, text=True, check=True)
            import json
            report = json.loads(result.stdout)
            self.assertEqual(report["current"]["bytes"], len(current.read_bytes()))
            self.assertIsNone(report["byte_reduction_percent"])

    def test_missing_input_fails_without_creating_it(self):
        with tempfile.TemporaryDirectory() as folder:
            missing = Path(folder) / "missing.md"
            result = subprocess.run([sys.executable, str(SCRIPT), str(missing)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(missing.exists())
            self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
