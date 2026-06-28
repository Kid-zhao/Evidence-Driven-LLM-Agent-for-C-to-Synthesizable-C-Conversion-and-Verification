from __future__ import annotations

from typing import Optional

from .types import CandidateCode, FailureAnalysis


class ReviewerAgent:
    """Performs a small contract sanity check."""

    def review(self, candidate: CandidateCode, analysis: Optional[FailureAnalysis]) -> str:
        if "demo_top" not in candidate.code:
            return "reject"
        if analysis and "interface" in analysis.patch_intent.lower():
            return "accept-with-warning"
        return "accept"
