# Agent-Scoped Local Retrieval

A boundary-first local retrieval architecture skill for OpenClaw workspaces.

This repository packages a reusable pattern for building retrieval in multi-agent environments with stronger boundary discipline, clearer agent scoping, safer maintenance defaults, a **prerequisite gate** that blocks execution until required runtime dependencies are actually ready, and explicit rules for honest maturity claims.

## Why this exists

Many local RAG setups start with one simple idea: index everything and add search.

That works for quick demos, but it breaks down in longer-running workspaces. The first problems are often not ranking quality. They are:
- personal memory mixed with reusable workspace knowledge
- unclear retrieval boundaries
- agents getting broader access than they should
- noisy recall from over-broad indexing
- refresh workflows that default to blind full rebuilds
- runtime dependencies discovered too late, after execution has already started failing
- maturity claims that outrun what has actually been tested

`workspace-local-retrieval` packages a different default.

## Core ideas

- **Separate personal memory from workspace retrieval**
- **Use allowlisted corpora instead of indexing everything**
- **Enforce deny-by-default access per agent**
- **Keep one stable retrieval interface for callers**
- **Treat maintenance and selective refresh as part of the design**
- **Gate execution on prerequisite checks**
- **Classify maturity honestly using explicit validation rules**

The emphasis is not only retrieval quality. It is retrieval architecture, runtime discipline, and validation honesty.

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
  - validation contract
  - anti-overclaim guidance
  - design rationale
  - publish readiness
- a conservative bootstrap script that generates starter config without ingesting private data automatically
- a runnable prerequisite check script for Python / Node / SQLite / FTS5 / embedding-backend readiness
- a sanitized demo corpus plus minimal index/search/smoke-test scripts for a closed-loop proof path
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
- a fully validated closed-loop retrieval system by default

It is a reusable architectural pattern and starter kit.

## Maturity labels

Use these labels honestly:
- **architecture-only**: boundaries, templates, and contracts exist, but no real retrieval loop has been proven
- **minimally runnable**: a safe demo path can ingest a small corpus, build an index, and answer at least one query
- **fully validated**: the minimal closed loop exists and the validation contract passes

Do not call the repo `fully validated`, `end-to-end`, `production-ready`, or `plug-and-play` unless the actual evidence supports that claim.

## Repository contents

```text
workspace-local-retrieval/
  SKILL.md
  assets/
    demo-corpus/
  references/
    agent-scoping.md
    anti-overclaim.md
    dependencies-and-platforms.md
    design-rationale.md
    example-templates.md
    interface-contract.md
    maintenance-patterns.md
    minimal-e2e-demo.md
    preflight-and-install-policy.md
    privacy-and-boundaries.md
    publish-readiness-checklist.md
    runtime-layout.md
    sanitized-demo.md
    validation-contract.md
  scripts/
    bootstrap_workspace_retrieval.py
    build_minimal_index.py
    check_retrieval_prereqs.py
    run_minimal_smoke_tests.py
    search_minimal_index.py
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
9. Validate using the maturity labels and validation contract.

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
