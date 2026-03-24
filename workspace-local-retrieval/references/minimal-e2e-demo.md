# Minimal E2E Demo

Use this reference when a user wants proof that the skill can drive a real, isolated minimal retrieval closed loop.

## Goal

Demonstrate a safe minimal path that can:
- read a sanitized corpus
- build a local SQLite FTS5 index
- answer queries through a stable wrapper
- enforce a simple corpus allowlist rule
- refresh changed content incrementally
- report smoke-test results honestly

## Demo assets and scripts

- Demo corpus: `assets/demo-corpus/`
- Index builder: `scripts/build_minimal_index.py`
- Search wrapper: `scripts/search_minimal_index.py`
- Smoke tests: `scripts/run_minimal_smoke_tests.py`

## Demo contract

This demo is intentionally narrow.

It proves:
- a minimal local closed loop exists
- agent-facing allowlist checks can be enforced
- incremental refresh can be exercised
- validation can be run in an isolated temp directory

It does **not** prove:
- semantic embedding quality
- large-scale ranking quality
- production operations
- broad workspace compatibility without adaptation

## How to run

1. Run preflight:
   - `python3 scripts/check_retrieval_prereqs.py --json`
2. Run the smoke suite:
   - `python3 scripts/run_minimal_smoke_tests.py`
3. Read the JSON report.
4. Use `references/validation-contract.md` to classify the maturity honestly.

## Interpretation

If the smoke suite passes in a clean isolated environment, the repo can honestly claim a **fully validated minimal closed loop** for the demo path.

Do not stretch that result into a claim about full production readiness.
