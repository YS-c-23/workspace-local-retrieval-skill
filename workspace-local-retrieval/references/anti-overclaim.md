# Anti-Overclaim Rules

Use this file before describing maturity in README text, release notes, ClawHub listings, or chat replies.

## Never claim more than the evidence supports

### Do not say "fully validated" unless:
- a real closed loop has been run
- required smoke tests have passed
- results were observed in an isolated environment

### Do not say "end-to-end" unless:
- corpus ingestion happened
- indexing happened
- querying happened
- expected output was verified

### Do not say "production-ready" unless:
- the user explicitly wants that bar
- operational concerns were addressed
- failure handling and maintenance expectations were tested

### Do not say "plug-and-play" unless:
- setup steps are genuinely short
- required dependencies are explicit
- another agent can reproduce the setup without hidden glue

## Safer wording by maturity

### If only architecture and templates exist
Say:
- "retrieval architecture skill"
- "starter kit"
- "scaffold"
- "boundary-first retrieval pattern"

### If a small demo loop works
Say:
- "minimally runnable demo"
- "validated smoke-tested demo path"
- "safe local proof of concept"

### If the full validation contract passes
Then you may say:
- "fully validated minimal closed loop"

Even then, avoid promising more than was tested.

## Mandatory honesty rules

- Name missing pieces explicitly.
- Separate tested behavior from intended future design.
- If a script was not run, say it was not run.
- If a workflow was only reviewed statically, say it was reviewed statically.
- If the skill package contains architecture plus starter scripts, do not market it as a complete retrieval product.

## Release wording check

Before publishing, ask:
1. What did I actually run?
2. What did I only design or describe?
3. Could another agent reproduce my claim from the repo contents?
4. Is any headline stronger than the validation evidence?

If any answer is uncomfortable, soften the claim.
