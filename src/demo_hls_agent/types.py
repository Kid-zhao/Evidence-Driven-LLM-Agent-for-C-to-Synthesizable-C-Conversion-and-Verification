from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class TaskSpec:
    task_id: str
    top_function: str
    source_summary: str
    interface_summary: str
    constraints: list[str] = field(default_factory=list)


@dataclass
class HLSDesignBrief:
    top_function: str
    interface_summary: str
    hotspot_summary: str
    risk_points: list[str]
    prompt_excerpt: str = "..."


@dataclass
class CandidateCode:
    code: str
    notes: list[str]


@dataclass
class VerificationEvidence:
    failure_stage: str | None
    raw_stage_errors: list[str]
    current_code: str
    task_bundle: dict[str, Any]
    artifact_trace: dict[str, Any] = field(default_factory=dict)


@dataclass
class FailureAnalysis:
    failure_family: str
    root_cause_summary: str
    patch_intent: str
    patch_scope: str
    must_preserve: list[str]
    retrieval_tags: list[str]
    next_action: str
    confidence: float
    evidence_citations: list[str]


@dataclass
class EvidenceCard:
    title: str
    summary: str
    allowed_stages: list[str]
    prompt_excerpt: str = "..."


@dataclass
class RunSummary:
    task_id: str
    stages: list[str]
    passed: bool
    final_stage: str
    review_decision: str
    notes: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
