# ClawHub Listing Copy

## Short description

Design a boundary-first local retrieval layer for OpenClaw workspaces with explicit corpus boundaries, deny-by-default agent access, and a validated minimal closed-loop demo.

## Medium description

`workspace-local-retrieval` packages a reusable retrieval architecture for OpenClaw workspaces that need more than ad-hoc local RAG.

It helps you:
- separate personal memory from workspace retrieval
- design explicit corpora instead of indexing everything
- scope retrieval access per agent
- keep a stable retrieval interface for callers
- add prerequisite gates before bootstrap, indexing, embeddings, or search
- stop cleanly when required dependencies are missing
- validate a minimal closed loop with runnable smoke tests
- make maturity claims honestly instead of overpromising

This skill is especially useful for multi-agent systems where retrieval quality depends on architecture, access control, maintenance discipline, and trust boundaries—not just ranking.

## Long description

`workspace-local-retrieval` is a publishable, boundary-first retrieval architecture skill for OpenClaw.

It is aimed at builders who want a local-first retrieval layer that is:
- privacy-aware
- agent-scoped
- maintainable over time
- explicit about runtime readiness
- credible in front of technical reviewers

The skill focuses on the parts of local retrieval that usually matter most in real systems:
- separating personal memory from reusable workspace knowledge
- defining allowlisted corpora instead of indexing everything
- enforcing deny-by-default access per agent
- using a stable search-wrapper contract for callers
- preferring selective refresh over blind rebuilds
- gating execution on prerequisite checks
- tying maturity claims to an explicit validation contract

What is included:
- a workflow-driven `SKILL.md`
- sanitized starter templates for corpora, agent allowlists, memory boundaries, and backend config
- reference docs for privacy boundaries, agent scoping, maintenance patterns, interface contracts, runtime dependencies, validation policy, and publish-readiness guidance
- a conservative bootstrap script that generates starter config without auto-indexing user data
- a runnable prerequisite check script
- a sanitized demo corpus plus minimal SQLite FTS5 index/search/smoke-test scripts

Current honest framing:
- this skill is more than a conceptual write-up
- it includes a **fully validated minimal closed-loop demo path**
- it is still not claiming to be a turnkey enterprise retrieval product

Use this skill when you want retrieval architecture that looks thoughtful, explainable, and technically disciplined—not just quickly hacked together.
