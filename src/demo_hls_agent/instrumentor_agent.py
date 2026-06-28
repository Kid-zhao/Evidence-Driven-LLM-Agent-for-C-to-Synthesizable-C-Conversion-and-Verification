from .types import CandidateCode


class InstrumentorAgent:
    """Adds trivial trace hooks to illustrate a mismatch-oriented path."""

    def instrument(self, candidate: CandidateCode) -> CandidateCode:
        instrumented = candidate.code + "// trace_hooks: ...\n"
        return CandidateCode(
            code=instrumented,
            notes=candidate.notes + ["Inserted mock trace hooks."],
        )
