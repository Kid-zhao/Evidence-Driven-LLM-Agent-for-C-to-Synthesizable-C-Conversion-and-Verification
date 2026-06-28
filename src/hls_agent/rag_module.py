from .types import EvidenceCard


class RetrievalModule:
    """Public stub only. Real retrieval logic is intentionally omitted."""

    def retrieve(self, query: str, stage: str) -> list[EvidenceCard]:
        return [
            EvidenceCard(
                title="Toy mismatch repair card",
                summary=f"Retrieved for stage={stage}, query={query[:32]}...",
                allowed_stages=[stage],
            )
        ]
