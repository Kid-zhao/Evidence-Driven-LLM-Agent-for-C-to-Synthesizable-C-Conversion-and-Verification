from .types import CandidateCode, FailureAnalysis, HLSDesignBrief, TaskSpec


class ProgrammerAgent:
    """Creates initial mock code and a minimal patch when needed."""

    def generate(self, task: TaskSpec, brief: HLSDesignBrief) -> CandidateCode:
        code = (
            f"// top_function: {brief.top_function}\n"
            "// prompt: ...\n"
            "void demo_top(int *a, int *b, int n) {\n"
            "    for (int i = 0; i < n; ++i) {\n"
            "        b[i] = a[i];\n"
            "    }\n"
            "}\n"
        )
        return CandidateCode(code=code, notes=["Generated from a minimal structural brief."])

    def patch(self, candidate: CandidateCode, analysis: FailureAnalysis) -> CandidateCode:
        patched = candidate.code + "\n// patch_intent: " + analysis.patch_intent + "\n"
        return CandidateCode(code=patched, notes=candidate.notes + ["Applied a local mock patch."])
