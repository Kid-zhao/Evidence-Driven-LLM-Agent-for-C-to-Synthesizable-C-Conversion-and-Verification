from __future__ import annotations

import json
from pathlib import Path

from .evaluator_agent import EvaluatorAgent
from .hls_failure_analyst import HLSFailureAnalyst
from .instrumentor_agent import InstrumentorAgent
from .mock_verifier import MockVerifier
from .planner_agent import PlannerAgent
from .programmer_agent import ProgrammerAgent
from .reviewer_agent import ReviewerAgent
from .types import RunSummary, TaskSpec


class HLSOrchestrator:
    """Wires the public demo modules into a tiny closed loop."""

    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.programmer = ProgrammerAgent()
        self.instrumentor = InstrumentorAgent()
        self.verifier = MockVerifier()
        self.analyst = HLSFailureAnalyst()
        self.reviewer = ReviewerAgent()
        self.evaluator = EvaluatorAgent()

    def load_task(self, path: str | Path) -> TaskSpec:
        payload = json.loads(Path(path).read_text())
        return TaskSpec(**payload)

    def run(self, task: TaskSpec) -> RunSummary:
        brief = self.planner.plan(task)
        candidate = self.programmer.generate(task, brief)
        evidence = self.verifier.verify(task, candidate)
        analysis = None

        if evidence.failure_stage is not None:
            analysis = self.analyst.analyze(evidence)
            candidate = self.instrumentor.instrument(candidate)
            candidate = self.programmer.patch(candidate, analysis)
            evidence = self.verifier.verify(task, candidate)

        review_decision = self.reviewer.review(candidate, analysis)
        return self.evaluator.summarize(task.task_id, evidence, review_decision)
