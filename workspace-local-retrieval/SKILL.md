---
name: Agent-Scoped Local Retrieval
description: Build boundary-first local retrieval for OpenClaw with explicit corpora, deny-by-default agent access, separate memory layers, and a validated minimal demo path.
---

# Workspace Local Retrieval

Package retrieval as architecture, not ad-hoc glue.

This skill exists for a common failure mode in local RAG systems: indexing grows faster than boundary discipline. The result is usually a system that can sometimes retrieve relevant text, but cannot clearly answer:
- what should be searchable
- which agent should see which corpus
- what belongs in personal memory versus workspace knowledge
- how freshness should be maintained over time
- what has actually been validated versus merely sketched

Prefer this skill when the goal is **workspace knowledge retrieval**, not personal memory recall. Keep those layers separate.

## Core workflow

1. **Run a preflight gate before any retrieval work**
   - Run `scripts/check_retrieval_prereqs.py` before bootstrap, indexing, embedding refresh, or search.
   - Treat missing required prerequisites as a hard stop.
   - Read `references/dependencies-and-platforms.md` when deciding what is required on the current OS.
   - Read `references/preflight-and-install-policy.md` when deciding whether to stop, warn, or produce an installation plan.

2. **Decide the boundary model first**
   - Use built-in memory tools for personal continuity (`MEMORY.md`, `memory/*.md`).
   - Use this skill's retrieval pattern for workspace knowledge, docs, skills, plans, schemas, and agent-specific materials.
   - Do not merge personal notes into a general retrieval corpus unless the user explicitly wants that and understands the privacy tradeoff.
   - Read `references/privacy-and-boundaries.md` before writing corpus config.

3. **Design corpora and agent access explicitly**
   - Split knowledge into small allowlisted corpora.
   - Use deny-by-default agent retrieval policy.
   - Keep separate memory-boundary rules for personal memory vs domain memory.
   - Read `references/agent-scoping.md` when mapping corpora and memory roots to agents.

4. **Bootstrap templates safely**
   - Run `scripts/bootstrap_workspace_retrieval.py --dest <dir>` to generate sanitized starter templates.
   - The script creates template config files only. It does not read external services, call the network, or ingest private data.
   - Read `references/runtime-layout.md` before claiming the setup is runnable.

5. **Implement one stable retrieval entrypoint**
   - Keep one wrapper responsible for agent-facing search and corpus allowlist checks.
   - Keep indexing, embeddings, and scoring internals behind the wrapper.
   - Read `references/interface-contract.md` for the recommended search-wrapper contract.

6. **Add maintenance-aware refresh behavior**
   - Track corpus fingerprints or file signatures.
   - Prefer selective refresh when only a small set of files changed.
   - Fall back to full rebuild only when needed.
   - Read `references/maintenance-patterns.md` for a production-friendly approach.

7. **Validate before making maturity claims**
   - Do not claim retrieval is ready because indexing succeeded once.
   - Read `references/validation-contract.md` to classify the result as `architecture-only`, `minimally runnable`, or `fully validated`.
   - Read `references/anti-overclaim.md` before writing publish-facing or user-facing maturity claims.
   - When the user wants proof of a runnable closed loop, read `references/minimal-e2e-demo.md` and run the demo scripts rather than describing a hypothetical future validation plan.

## Hard truth rules

- No required prerequisites, no execution.
- No real closed loop, no `end-to-end` claim.
- No smoke-test suite, no `fully validated` claim.
- No reproducible evidence, no strong marketing language.
- If uncertain, downgrade the maturity label rather than stretch it.

## Recommended file layout

Use this skill as a pattern, not a rigid requirement.

```text
retrieval/
  config/
    corpora.json
    agent_corpora.json
    agent_memory.json
    backend.json
  scripts/
    workspace_search.mjs
    build_index.py
    build_embeddings.mjs
    retrieval_status.py
    refresh_incremental.py
  indexes/
    workspace_retrieval.sqlite
```

If the workspace already has a retrieval system, adapt the layout instead of forcing a rewrite.

## Defaults worth keeping

- local-first storage
- allowlisted corpora
- deny-by-default agent access
- personal memory separate from workspace retrieval
- minimal indexed file extensions
- explicit exclude globs
- incremental refresh before full rebuild
- one stable wrapper for agent-facing search
- validation before maturity claims

## When to read references

- Read `references/privacy-and-boundaries.md` for safe corpus design and exclusions.
- Read `references/agent-scoping.md` when mapping corpora and memory roots to agents.
- Read `references/interface-contract.md` when building or reviewing the agent-facing search wrapper.
- Read `references/maintenance-patterns.md` when adding status checks, selective refresh, and smoke tests.
- Read `references/example-templates.md` when you need sanitized starter JSON examples.
- Read `references/dependencies-and-platforms.md` when the user wants concrete runtime dependencies, embedding backend choices, or cross-platform guidance.
- Read `references/preflight-and-install-policy.md` when deciding whether the skill is runnable now, blocked, or should first produce an installation task plan.
- Read `references/runtime-layout.md` when the user wants a more runnable implementation footprint.
- Read `references/design-rationale.md` when the user needs the architectural thesis, tradeoffs, or public-facing positioning.
- Read `references/sanitized-demo.md` when the user wants a safe walkthrough or publishable example.
- Read `references/validation-contract.md` when deciding what completion level has actually been achieved.
- Read `references/minimal-e2e-demo.md` when the user wants a safe runnable proof path.
- Read `references/anti-overclaim.md` before packaging or publicly promoting the skill.
- Read `references/publish-readiness-checklist.md` before packaging or publicly promoting the skill.

## Output expectations

When using this skill for a user request, produce some or all of the following depending on scope:
- sanitized corpus config
- agent allowlist config
- memory-boundary config
- search wrapper contract
- maintenance workflow
- smoke-test checklist
- validation report with an honest maturity label
- packaging-ready skill contents when the user wants distribution
