# HLS Agent Open Demo

This repository is a minimal open-source skeleton that demonstrates the module boundaries and data flow of an evidence-driven HLS agent workflow.

It is intentionally simplified:

- Sensitive prompts are replaced with `...`.
- Real repair heuristics are omitted.
- Real benchmark assets and locked experiment data are not included.
- The verifier is a mock four-stage pipeline rather than a real HLS toolchain.

## What This Demo Shows

- A planner -> programmer -> instrumentor -> verifier -> reviewer -> evaluator workflow
- Evidence objects that move between modules
- A retrieval interface stub for future RAG integration
- A mock end-to-end run that produces a structured summary

## Repository Layout

```text
src/demo_hls_agent/      Minimal Python package
docs/                    Public-facing workflow and module docs
configs/                 Demo configuration
examples/                Example task input
data/toy_cases/          Tiny toy case instead of real benchmark assets
results/                 Example output schema
tests/                   Basic smoke tests
```

## Quick Start

```bash
python3 -m demo_hls_agent.cli --task examples/task.json
```

## Design Notes

- The orchestrator owns the loop and module wiring.
- Each module exposes a small interface and returns typed objects.
- The mock verifier simulates `compile -> csim -> synth -> cosim`.
- Prompt-bearing fields are represented as `...` placeholders.

## Non-Goals

- Reproducing paper results
- Shipping real prompts
- Shipping real repair cards or private evidence corpora
- Interfacing with Vivado/Vitis or other vendor tools
