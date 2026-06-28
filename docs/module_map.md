# Module Map

## Core Runtime

- `src/demo_hls_agent/orchestrator.py`
  Owns the end-to-end loop and module wiring.
- `src/demo_hls_agent/types.py`
  Shared data structures.
- `src/demo_hls_agent/planner_agent.py`
  Produces the task brief.
- `src/demo_hls_agent/programmer_agent.py`
  Handles initial generation and local patching.
- `src/demo_hls_agent/instrumentor_agent.py`
  Adds trace hooks for mismatch-oriented debugging.
- `src/demo_hls_agent/mock_verifier.py`
  Public substitute for the real HLS verification pipeline.
- `src/demo_hls_agent/hls_failure_analyst.py`
  Produces a compact failure analysis object.
- `src/demo_hls_agent/reviewer_agent.py`
  Performs a light contract sanity check.
- `src/demo_hls_agent/evaluator_agent.py`
  Emits a run summary.
- `src/demo_hls_agent/rag_module.py`
  Stub retrieval interface only.

## Support Artifacts

- `examples/task.json`
  Example input task.
- `results/demo_run_summary.json`
  Example result schema.
- `configs/demo_config.yaml`
  Placeholder configuration with `...` values.
