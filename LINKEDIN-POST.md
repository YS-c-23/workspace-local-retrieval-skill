# LinkedIn Launch Copy — prerequisite-gated version

I just published **workspace-local-retrieval** to GitHub and ClawHub.

It packages a local-first retrieval pattern for multi-agent workspaces, with:
- explicit corpus boundaries
- deny-by-default agent access
- clear separation between personal memory and workspace knowledge
- a **prerequisite gate** before execution

That last piece is the part I especially care about.

A lot of retrieval tooling assumes the runtime is ready and only discovers missing dependencies halfway through bootstrap, indexing, or search. I wanted a stricter and more honest default:

- run preflight checks first
- classify dependencies as required / recommended / optional
- if required prerequisites are missing, **stop**
- if environment changes are allowed, create an OS-aware install plan first
- re-validate before execution

In short:

**No required prerequisites, no execution.**

That turns retrieval from a fragile demo path into something closer to real agent infrastructure.

The skill is designed for local-first and privacy-aware systems where retrieval is not just about ranking quality. It is also about:
- boundary design
- memory governance
- scoped access
- operational reliability across macOS / Linux / Windows

Inside the skill:
- a workflow-oriented `SKILL.md`
- dependency and platform guidance
- preflight and install policy
- sanitized starter templates for corpora and backend config
- a runnable prerequisite check script

GitHub: <https://github.com/YS-c-23/workspace-local-retrieval-skill>
ClawHub: <https://clawhub.ai/ys-c-23/workspace-local-retrieval>

If you care about agent infrastructure, local RAG, or building systems that fail early instead of failing halfway through execution, I’d love to compare notes.
