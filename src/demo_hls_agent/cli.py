from __future__ import annotations

import argparse
import json

from .orchestrator import HLSOrchestrator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True, help="Path to a demo task JSON file.")
    args = parser.parse_args()

    orchestrator = HLSOrchestrator()
    task = orchestrator.load_task(args.task)
    summary = orchestrator.run(task)
    print(json.dumps(summary.to_dict(), indent=2))


if __name__ == "__main__":
    main()
