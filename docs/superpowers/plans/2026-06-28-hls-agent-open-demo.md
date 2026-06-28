# HLS Agent Open Demo Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a minimal public demo repo that shows module relationships and an evidence-driven HLS workflow without exposing prompts, private assets, or real research logic.

**Architecture:** The repo is a small Python package with typed objects, mock agents, and a mock verifier wired by an orchestrator. Public docs explain the workflow, module boundaries, schema, and privacy redactions, while examples and results show a tiny end-to-end path.

**Tech Stack:** Python 3.9+, setuptools, unittest-compatible smoke test, Markdown, JSON, YAML

---

### Task 1: Define Public Repo Surface

**Files:**
- Create: `README.md`
- Create: `docs/workflow.md`
- Create: `docs/module_map.md`
- Create: `docs/experiment_schema.md`
- Create: `docs/privacy_notes.md`

- [ ] **Step 1: Write the public scope docs**
- [ ] **Step 2: Keep prompts and sensitive logic as `...`**
- [ ] **Step 3: Verify docs match the open-source boundary**

### Task 2: Build Minimal Runtime Skeleton

**Files:**
- Create: `src/demo_hls_agent/types.py`
- Create: `src/demo_hls_agent/planner_agent.py`
- Create: `src/demo_hls_agent/programmer_agent.py`
- Create: `src/demo_hls_agent/instrumentor_agent.py`
- Create: `src/demo_hls_agent/mock_verifier.py`
- Create: `src/demo_hls_agent/hls_failure_analyst.py`
- Create: `src/demo_hls_agent/reviewer_agent.py`
- Create: `src/demo_hls_agent/evaluator_agent.py`
- Create: `src/demo_hls_agent/rag_module.py`
- Create: `src/demo_hls_agent/orchestrator.py`
- Create: `src/demo_hls_agent/cli.py`

- [ ] **Step 1: Add typed data structures**
- [ ] **Step 2: Add mock modules with small interfaces**
- [ ] **Step 3: Wire the modules through the orchestrator**

### Task 3: Add Examples, Config, and Verification

**Files:**
- Create: `examples/task.json`
- Create: `results/demo_run_summary.json`
- Create: `configs/demo_config.yaml`
- Create: `tests/test_demo_pipeline.py`
- Create: `pyproject.toml`

- [ ] **Step 1: Add one toy input and one toy output**
- [ ] **Step 2: Add a smoke test for the CLI**
- [ ] **Step 3: Run the smoke test and package the repo**
