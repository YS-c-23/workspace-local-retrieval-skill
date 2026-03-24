# ClawHub Listing Copy

## Short description

A local-first retrieval architecture skill for OpenClaw workspaces with explicit corpus boundaries, deny-by-default agent access, and a prerequisite gate that blocks execution until required runtime dependencies are ready.

## Medium description

`workspace-local-retrieval` packages a reusable retrieval pattern for OpenClaw workspaces that need more than ad-hoc local RAG.

It helps you:
- separate personal memory from workspace retrieval
- design explicit corpora instead of indexing everything
- scope retrieval access per agent
- keep a stable retrieval interface for callers
- add a prerequisite gate before bootstrap, indexing, embeddings, or search
- stop cleanly when required dependencies are missing
- create an OS-aware installation plan before execution when environment prep is needed

This skill is especially useful for multi-agent setups where retrieval quality depends not just on ranking, but on boundary design, access control, and operational discipline.

## Long description

`workspace-local-retrieval` is a safety-conscious skill for building a local-first retrieval layer in an OpenClaw workspace.

It is designed for users who want retrieval to be:
- reusable
- explainable
- privacy-aware
- agent-scoped
- maintainable over time
- honest about runtime readiness

Instead of encouraging naive “index everything” patterns, the skill focuses on architectural quality:
- personal memory and workspace retrieval are treated as separate layers
- corpora are allowlisted explicitly
- agent access is deny-by-default
- retrieval callers use one stable wrapper contract
- maintenance includes freshness checks and selective refresh patterns
- execution is gated by prerequisite checks rather than assumption

The skill includes:
- a workflow-driven `SKILL.md`
- sanitized JSON starter templates
- reference docs for privacy boundaries, agent scoping, interface contracts, maintenance patterns, runtime dependencies, and preflight/install policy
- a conservative bootstrap script that generates starter config without indexing user data automatically
- a runnable prerequisite check script

Use this skill when you want a retrieval architecture that reflects real multi-agent operational constraints, not just a quick demo.
