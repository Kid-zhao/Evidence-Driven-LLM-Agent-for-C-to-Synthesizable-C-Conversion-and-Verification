# Workflow

This demo exposes the public shape of the research workflow without publishing the real prompts or repair logic.

```text
task brief
  -> structural generation
  -> verify
  -> failure analysis
  -> targeted patch
  -> re-verify
  -> review
  -> summarize
```

## Public Mapping

- `PlannerAgent`: produces a compact `HLSDesignBrief`
- `ProgrammerAgent`: creates initial code and a local patch
- `InstrumentorAgent`: inserts minimal trace hooks
- `MockVerifier`: simulates `compile -> csim -> synth -> cosim`
- `HLSFailureAnalyst`: converts raw evidence into a patch-oriented summary
- `ReviewerAgent`: checks interface stability at a high level
- `EvaluatorAgent`: emits a result summary

## Intentionally Omitted

- Real prompts
- Real failure-family heuristics
- Real HLS logs
- Real benchmark assets
- Real experiment ledger logic
