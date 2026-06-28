from .types import FailureAnalysis, VerificationEvidence


class HLSFailureAnalyst:
    """Turns raw evidence into a compact patch-oriented summary."""

    def analyze(self, evidence: VerificationEvidence) -> FailureAnalysis:
        family = evidence.failure_stage or "none"
        return FailureAnalysis(
            failure_family=family,
            root_cause_summary="The mock run lacks the expected trace instrumentation.",
            patch_intent="Add the missing trace hooks and keep the interface unchanged.",
            patch_scope="Local patch in the generated top function only.",
            must_preserve=["top function name", "declared interface shape"],
            retrieval_tags=[family, "public-skeleton"],
            next_action="patch-and-reverify",
            confidence=0.8,
            evidence_citations=["raw_stage_errors[0]"] if evidence.raw_stage_errors else [],
        )
