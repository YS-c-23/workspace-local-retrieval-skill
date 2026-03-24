# workspace-local-retrieval

A local-first retrieval architecture skill for OpenClaw workspaces.

This skill packages a reusable pattern for building retrieval in multi-agent environments with stronger boundary discipline, clearer agent scoping, safer maintenance defaults, and a **prerequisite gate** that blocks execution until required runtime dependencies are actually ready.

## Why this exists

Many local RAG setups start with one simple idea: index everything and add search.

That works for quick demos, but it breaks down in longer-running workspaces. The first problems are often not ranking quality. They are:
- personal memory mixed with reusable workspace knowledge
- unclear retrieval boundaries
- agents getting broader access than they should
- noisy recall from over-broad indexing
- refresh workflows that default to blind full rebuilds
- runtime dependencies discovered too late, after execution has already started failing

`workspace-local-retrieval` packages a different default.

## Core ideas

- **Separate personal memory from workspace retrieval**
- **Use allowlisted corpora instead of indexing everything**
- **Enforce deny-by-default access per agent**
- **Keep one stable retrieval interface for callers**
- **Treat maintenance and selective refresh as part of the design**
- **Gate execution on prerequisite checks**

The emphasis is not only retrieval quality. It is retrieval architecture and runtime discipline.

## What the skill includes

- a workflow-oriented `SKILL.md`
- sanitized starter templates for corpora, agent allowlists, memory boundaries, and backend config
- reference docs for:
  - privacy and boundaries
  - agent scoping
  - interface contracts
  - maintenance patterns
  - dependency and platform guidance
  - preflight and install policy
  - design rationale
  - publish readiness
- a conservative bootstrap script that generates starter config without ingesting private data automatically
- a runnable prerequisite check script for Python / Node / SQLite / FTS5 / embedding-backend readiness
- a sanitized demo walkthrough for public explanation and validation

## Who this is for

This skill is useful if you are building:
- local AI assistants
- multi-agent workspaces
- privacy-sensitive local RAG systems
- agent infrastructure with scoped retrieval access
- long-running retrieval workflows that need maintenance discipline

## What this skill is not

This is not:
- a hosted vector database
- a turnkey enterprise retrieval platform
- a benchmark package for ranking quality
- a substitute for careful corpus design

It is a reusable architectural pattern and starter kit.

## Repository contents

```text
workspace-local-retrieval/
  SKILL.md
  references/
    agent-scoping.md
    dependencies-and-platforms.md
    design-rationale.md
    example-templates.md
    interface-contract.md
    maintenance-patterns.md
    preflight-and-install-policy.md
    privacy-and-boundaries.md
    publish-readiness-checklist.md
    runtime-layout.md
    sanitized-demo.md
  scripts/
    bootstrap_workspace_retrieval.py
    check_retrieval_prereqs.py
```

## Suggested usage

1. Run the prerequisite check first.
2. If required dependencies are missing, stop and either:
   - report the skill as currently unavailable, or
   - create an OS-aware install plan if environment prep is allowed.
3. Bootstrap sanitized retrieval config templates.
4. Define explicit corpora.
5. Define deny-by-default agent access.
6. Keep personal memory and workspace retrieval as separate layers.
7. Add a stable retrieval wrapper.
8. Add freshness checks and selective refresh.
9. Validate with a sanitized demo and smoke tests.

## Why the public version is sanitized

This repository is intentionally generalized.

It does **not** include:
- private workspace paths
- live user data
- private memory files
- credentials or tokens
- generated indexes or embeddings
- environment-specific runtime state

The goal is to publish the pattern, not leak the original workspace.

## Publishing

For ClawHub distribution, package and upload the `.skill` artifact.

For GitHub distribution, publish the skill folder plus a small amount of explanatory material such as this README and launch copy.

## License

This project is licensed under the MIT License. See `LICENSE`.

## Contact / discussion

If you are working on local-first assistants, agent infrastructure, retrieval governance, or privacy-aware multi-agent systems, feel free to adapt the pattern and compare notes.
