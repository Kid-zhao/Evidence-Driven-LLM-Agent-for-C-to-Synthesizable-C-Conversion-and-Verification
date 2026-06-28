# Privacy Notes

This demo is designed to be safe to open-source.

## Removed

- Real prompts
- Full repair instructions
- Real HLS logs
- Private benchmark assets
- Locked experiment summaries
- Internal RAG corpora

## Replaced

- Sensitive prompts -> `...`
- Real verifier -> `MockVerifier`
- Real evidence cards -> a toy retrieval stub
- Real cases -> `data/toy_cases/example_01`

## Goal

Show the relationships between modules and the structure of the workflow without exposing research-sensitive implementation details.
