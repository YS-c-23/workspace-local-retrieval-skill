# Quickstart: adapt the pattern to a real workspace

Use this after the minimal demo passes.

## Goal

Move from the sanitized demo to a real workspace retrieval baseline without pretending the whole system is turnkey.

## Step 1 — bootstrap starter config

From the skill root:

```bash
python3 scripts/bootstrap_workspace_retrieval.py --dest ./retrieval --workspace-root "$(pwd)"
```

This generates:
- `retrieval/config/corpora.json`
- `retrieval/config/agent_corpora.json`
- `retrieval/config/agent_memory.json`
- `retrieval/config/backend.json`

## Step 2 — edit corpus boundaries first

Before indexing anything:
- remove paths that should not be searchable
- confirm `memory/**` and private note folders stay excluded
- narrow `skills/**`, `agents/**`, and specialist docs to only what the workspace actually needs

If in doubt, start too narrow, not too broad.

## Step 3 — define agent access

Edit `retrieval/config/agent_corpora.json`:
- keep `defaultPolicy` deny-by-default
- allow each agent only the corpora it actually needs
- do not let specialist agents inherit broad access just because it is convenient

## Step 4 — choose your first runtime mode

For the first real workspace version, prefer a lexical baseline:
- SQLite FTS5
- small set of markdown/text files
- one wrapper script or command for search

Only add semantic retrieval after the lexical baseline works and the boundary model is stable.

## Step 5 — validate one narrow workflow

Do not try to validate the whole workspace at once.

Pick one narrow proof path, for example:
- search workspace policy docs
- search one specialist knowledge area
- prove one agent cannot access another agent's corpus

## Step 6 — add semantic retrieval only if needed

If you need local semantic retrieval:
- install Ollama or another local embedding backend
- update `retrieval/config/backend.json`
- add embedding refresh behind the same stable wrapper instead of exposing internals directly

## Step 7 — keep claims honest

After adapting to a real workspace, call it:
- `architecture-only` if boundaries and config exist but real retrieval is not validated
- `minimally runnable` if one real retrieval workflow works
- `fully validated` only if your validation contract really passes

## Recommended first publish claim

A safe claim is:

> This repo includes a validated minimal demo path and a bootstrap pattern for adapting the retrieval architecture to a real OpenClaw workspace.

That is much safer than claiming full turnkey workspace retrieval.
