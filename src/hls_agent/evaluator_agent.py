from .types import RunSummary, VerificationEvidence


class EvaluatorAgent:
    """Summarizes the mock run in a result-friendly schema."""

    def summarize(self, task_id: str, evidence: VerificationEvidence, review_decision: str) -> RunSummary:
        passed = evidence.failure_stage is None
        final_stage = "cosim" if passed else evidence.failure_stage or "unknown"
        notes = ["Public repository result only.", f"review={review_decision}"]
        return RunSummary(
            task_id=task_id,
            stages=evidence.task_bundle["stages"],
            passed=passed,
            final_stage=final_stage,
            review_decision=review_decision,
            notes=notes,
        )
