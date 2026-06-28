# Experiment Schema

The original evidence tree contains rich experiment bookkeeping. The public demo exposes only a small schema:

## Input Schema

```json
{
  "task_id": "toy_case_01",
  "top_function": "demo_top",
  "source_summary": "Toy C kernel summary",
  "interface_summary": "int* a, int* b, int n",
  "constraints": ["keep interface stable"]
}
```

## Output Schema

```json
{
  "task_id": "toy_case_01",
  "stages": ["compile", "csim", "synth", "cosim"],
  "passed": true,
  "final_stage": "cosim",
  "review_decision": "accept",
  "notes": ["Public demo result only.", "review=accept"]
}
```

## Privacy Rules

- Real design cases are not included.
- Real aggregate numbers are not included.
- Real repair cards and evidence excerpts are not included.
