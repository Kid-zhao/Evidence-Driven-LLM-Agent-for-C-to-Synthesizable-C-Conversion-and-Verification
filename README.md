# Evidence-Driven LLM Agent Open Demo

This repository is a minimal public demo for an evidence-driven HLS agent workflow.

It only keeps the high-level module relationships:

- `planner -> programmer -> instrumentor -> verifier -> analyst -> reviewer -> evaluator`
- typed evidence objects passed between modules
- a mock four-stage verification loop: `compile -> csim -> synth -> cosim`

Sensitive details are intentionally removed:

- prompts are replaced with `...`
- real repair heuristics are omitted
- private benchmarks and locked experiment assets are not included
- the verifier is a mock implementation, not a vendor HLS toolchain

## Repository Layout

```text
src/demo_hls_agent/   Minimal Python package
examples/             One toy task input
tests/                One smoke test
```

## Quick Start

```bash
PYTHONPATH=src python3 -m demo_hls_agent.cli --task examples/task.json
```

## Scope

This demo is meant to show structure only. It is not intended to reproduce paper results or expose the private research workflow.
