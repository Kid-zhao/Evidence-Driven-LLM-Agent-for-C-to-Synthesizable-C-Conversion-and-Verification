from .types import CandidateCode, TaskSpec, VerificationEvidence


class MockVerifier:
    """Simulates a four-stage HLS verification pipeline."""

    stages = ["compile", "csim", "synth", "cosim"]

    def verify(self, task: TaskSpec, candidate: CandidateCode) -> VerificationEvidence:
        fails_csim = "trace_hooks" not in candidate.code
        failure_stage = "csim" if fails_csim else None
        errors = ["Mock CSim mismatch detected."] if fails_csim else []
        return VerificationEvidence(
            failure_stage=failure_stage,
            raw_stage_errors=errors,
            current_code=candidate.code,
            task_bundle={
                "task_id": task.task_id,
                "top_function": task.top_function,
                "stages": self.stages,
            },
            artifact_trace={
                "public_note": "Real tool logs are omitted in the open demo.",
            },
        )
