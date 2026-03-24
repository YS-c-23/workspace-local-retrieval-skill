# ClawHub Listing Copy

## Short description

A boundary-first local retrieval architecture skill for OpenClaw workspaces with explicit corpus boundaries, deny-by-default agent access, a prerequisite gate for runtime readiness, and explicit validation rules for maturity claims.

## Medium description

`workspace-local-retrieval` packages a reusable retrieval pattern for OpenClaw workspaces that need more than ad-hoc local RAG.

It helps you:
- separate personal memory from workspace retrieval
- design explicit corpora instead of indexing everything
- scope retrieval access per agent
- keep a stable retrieval interface for callers
- add a prerequisite gate before bootstrap, indexing, embeddings, or search
- stop cleanly when required dependencies are missing
- classify outcomes honestly as architecture-only, minimally runnable, or fully validated
- avoid overclaiming maturity before a real closed loop is tested

This skill is especially useful for multi-agent setups where retrieval quality depends not just on ranking, but on boundary design, access control, maintenance discipline, and validation honesty.

## Long description

`workspace-local-retrieval` is a safety-conscious skill for building a local-first retrieval layer in an OpenClaw workspace.

It is designed for users who want retrieval to be:
- reusable
- explainable
- privacy-aware
- agent-scoped
- maintainable over time
- honest about runtime readiness and maturity

Instead of encouraging naive “index everything” patterns, the skill focuses on architectural quality:
- personal memory and workspace retrieval are treated as separate layers
- corpora are allowlisted explicitly
- agent access is deny-by-default
- retrieval callers use one stable wrapper contract
- maintenance includes freshness checks and selective refresh patterns
- execution is gated by prerequisite checks rather than assumption
- maturity claims are constrained by an explicit validation contract

The skill includes:
- a workflow-driven `SKILL.md`
- sanitized JSON starter templates
- reference docs for privacy boundaries, agent scoping, interface contracts, maintenance patterns, runtime dependencies, validation contract, anti-overclaim policy, and preflight/install policy
- a conservative bootstrap script that generates starter config without indexing user data automatically
- a runnable prerequisite check script

Current honest framing:
- this repo is an architecture skill and starter kit
- it should not be marketed as a complete retrieval product unless a real closed loop and validation suite are present and passing

Use this skill when you want a retrieval architecture that reflects real multi-agent operational constraints, not just a quick demo.
