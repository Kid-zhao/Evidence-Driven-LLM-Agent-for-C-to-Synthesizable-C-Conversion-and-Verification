import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PipelineTest(unittest.TestCase):
    def test_cli_runs(self) -> None:
        env = {"PYTHONPATH": str(ROOT / "src")}
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "hls_agent.cli",
                "--task",
                str(ROOT / "examples" / "task.json"),
            ],
            capture_output=True,
            text=True,
            check=True,
            env=env,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["task_id"], "example_case_01")
        self.assertTrue(payload["passed"])


if __name__ == "__main__":
    unittest.main()
