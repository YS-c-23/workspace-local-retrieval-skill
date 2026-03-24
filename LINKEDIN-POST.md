# LinkedIn Launch Copy — recruiter-standard version

I just published a new OpenClaw skill: **workspace-local-retrieval**.

It packages a local-first retrieval architecture for multi-agent workspaces — with explicit privacy boundaries, deny-by-default agent access, and maintenance-aware refresh workflows.

What I wanted to solve was not just “how to add search.”

In practice, many local RAG setups break down earlier than people expect:
- personal memory gets mixed with reusable workspace knowledge
- agents inherit more context than they should
- indexing scope grows without clear ownership
- retrieval quality gets noisy
- maintenance becomes a blind full-rebuild habit

So instead of treating retrieval as “embed everything and hope ranking works,” I packaged a different default:

- **separate personal memory from workspace retrieval**
- **use allowlisted corpora instead of indexing everything**
- **enforce deny-by-default access by agent**
- **keep one stable retrieval interface for callers**
- **treat freshness and selective refresh as part of the architecture**

The result is not a flashy demo. It is a reusable retrieval pattern that is more opinionated about:
- boundary design
- memory governance
- agent scoping
- operational reliability

Inside the skill:
- a detailed workflow-oriented `SKILL.md`
- sanitized starter templates for corpora, agent policies, and memory boundaries
- reference docs covering privacy, scoping, interface design, maintenance, and design rationale
- a conservative bootstrap script that generates config templates without touching network services or private data

Why I think this matters:

As soon as you move from a single assistant to a multi-agent workspace, retrieval stops being “just search plumbing.” It becomes a systems problem:
- who can know what
- what should stay isolated
- what belongs in personal memory vs workspace knowledge
- how to keep retrieval fresh without rebuilding everything every time

That is the lens behind this skill.

If you are building local AI assistants, agent infrastructure, privacy-sensitive RAG systems, or long-running multi-agent workspaces, this pattern may be useful.

Happy to share more about the design tradeoffs, what I excluded on purpose, and why I think retrieval architecture needs stronger boundary discipline than most demos show.
