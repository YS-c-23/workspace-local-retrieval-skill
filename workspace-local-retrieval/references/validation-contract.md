# Validation Contract

Use this file when deciding whether a workspace-local-retrieval setup is merely scaffolded, minimally runnable, or fully validated.

## Levels of completion

### 1. Architecture-only
Use this label when the work includes boundary design, corpus policy, agent allowlists, config templates, or interface design, but does not yet run a real retrieval loop.

Typical evidence:
- corpus config exists
- agent access policy exists
- memory-boundary policy exists
- preflight script exists
- bootstrap templates exist

Do **not** call this runnable retrieval.

### 2. Minimally runnable
Use this label when a safe local demo can complete a real closed loop:
- read a small corpus
- build a local index
- run at least one query
- return at least one expected result

Required evidence:
- preflight passes for the chosen runtime path
- demo corpus exists
- index builder runs successfully
- search wrapper runs successfully
- at least one positive query passes

Do **not** call this fully validated unless the smoke-test contract below also passes.

### 3. Fully validated
Use this label only when the system has a reproducible minimal closed loop and the validation suite passes.

Required evidence:
- preflight passes
- bootstrap works
- minimal corpus indexes successfully
- search wrapper returns expected results
- corpus scoping behavior is exercised
- allowlist denial is enforced
- changed-file refresh behavior is exercised
- smoke tests all pass in a clean isolated environment
- results are documented clearly enough for another agent to reproduce

If any required item is missing, failed, or untested, do **not** claim fully validated.

## Mandatory smoke tests

Run all of these before claiming fully validated:

1. **Broad query**
   - Query should retrieve a clearly relevant result from the demo corpus.
2. **Corpus-scoped query**
   - Query should return a result only when the allowed corpus is included.
3. **Allowlist denial**
   - An agent or request targeting a forbidden corpus should be rejected clearly.
4. **Changed-file refresh**
   - After modifying one indexed file, selective refresh should update search results without requiring a full rebuild.
5. **Missing prerequisite hard stop**
   - If a required runtime dependency is missing for the chosen path, execution should stop rather than quietly continue.
6. **No-hit behavior**
   - A query with no relevant match should return a clear no-hit response rather than fabricated confidence.

## Clean-environment requirement

Validation should be run in an isolated temp directory or other non-destructive environment.

Avoid using:
- private memory files
- live secrets
- the user's primary workspace index
- any corpus that includes sensitive notes by default

## Output contract for validation reports

A validation report should explicitly say:
- what environment was used
- what scripts were run
- which smoke tests passed
- which smoke tests failed or were skipped
- whether the result is architecture-only, minimally runnable, or fully validated
- what remains before the next level can be claimed

## Decision rule

When in doubt, downgrade the maturity claim.

Prefer:
- "architecture pattern"
- "starter kit"
- "minimally runnable demo"

over:
- "fully validated"
- "production-ready"
- "complete local RAG system"
