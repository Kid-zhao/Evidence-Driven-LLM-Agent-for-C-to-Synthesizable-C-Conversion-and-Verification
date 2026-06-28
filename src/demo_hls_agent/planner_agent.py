from .types import HLSDesignBrief, TaskSpec


class PlannerAgent:
    """Produces a minimal task brief for downstream modules."""

    def plan(self, task: TaskSpec) -> HLSDesignBrief:
        return HLSDesignBrief(
            top_function=task.top_function,
            interface_summary=task.interface_summary,
            hotspot_summary="Toy loop and buffer handling only.",
            risk_points=[
                "Keep the top function name stable.",
                "Do not change the declared interface shape.",
                "Prefer small, local edits during repair.",
            ],
        )
