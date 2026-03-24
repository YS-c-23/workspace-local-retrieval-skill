# Publish Readiness Checklist

Use this file before publishing the skill to ClawHub or promoting it publicly.

## 1. Privacy review

Confirm the skill does **not** contain:
- real usernames
- real chat ids
- personal paths
- private workspace names
- sample data copied from live notes
- credentials, tokens, or hidden config
- generated indexes or embeddings

## 2. Generalization review

Confirm the skill uses:
- neutral corpus names
- neutral agent names where possible
- placeholder paths instead of machine-specific paths
- templates instead of snapshots from one workspace

## 3. Safety review

Confirm scripts:
- do not call the network unless clearly documented
- do not auto-index private data on install
- do not overwrite files silently unless the user requests force behavior
- fail clearly when configuration is incomplete
- stop when required prerequisites for the chosen path are missing

## 4. Quality review

Confirm the skill provides:
- a clear problem statement
- an opinionated but reusable architecture
- at least one bootstrap or starter path
- enough detail to be genuinely useful
- examples that are realistic but sanitized
- clear references for validation expectations and maturity claims

## 5. Validation honesty review

Confirm the public wording matches the evidence:
- If only templates and architecture exist, describe it as an architecture skill or starter kit.
- If a minimal closed loop runs, describe it as a minimally runnable demo.
- Claim `fully validated` only if the validation contract has actually passed.
- Do not use `end-to-end`, `production-ready`, or `plug-and-play` unless the repo contents and tests truly support those claims.

Read:
- `references/validation-contract.md`
- `references/anti-overclaim.md`

## 6. Credibility review

Before public promotion, ask:
- Would a staff engineer find this architecture coherent?
- Would a security-minded reader see clear boundary thinking?
- Would another user know where to start within 5 minutes?
- Does the public copy distinguish tested behavior from intended future design?

## 7. Final release gate

Publish only if the answer is yes to all of these:
- Is it safe?
- Is it reusable?
- Is it technically coherent?
- Is it specific enough to be useful?
- Is it honest about maturity?
- Is it clean enough to represent publicly?
