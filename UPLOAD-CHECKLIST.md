# workspace-local-retrieval — Final Upload Checklist

Use this checklist before uploading to GitHub, ClawHub, and announcing on LinkedIn.

---

## A. Privacy / Safety Gate

Confirm all of the following are true:

- [ ] No real usernames remain
- [ ] No chat ids or account ids remain
- [ ] No private local machine paths remain
- [ ] No private workspace names remain unless intentionally generic
- [ ] No `memory/`, `MEMORY.md`, `my_note/`, or profile data is included
- [ ] No credentials, tokens, cookies, or app secrets are included
- [ ] No generated retrieval indexes or embeddings are included
- [ ] No sample data copied from live private notes is included
- [ ] Scripts do not auto-ingest private data on install
- [ ] Scripts do not make undocumented network calls

---

## B. Quality Gate

Confirm all of the following are true:

- [ ] The problem statement is clear
- [ ] The skill has a real architectural thesis, not just feature bullets
- [ ] The skill explains why memory and retrieval are separate layers
- [ ] The skill explains deny-by-default agent access clearly
- [ ] The skill includes a usable bootstrap path
- [ ] The skill includes at least one sanitized demo or walkthrough
- [ ] The skill includes maintenance / refresh guidance
- [ ] The skill reads like a reusable system artifact, not private glue code

---

## C. GitHub Release Gate

Recommended public repo contents:

- [ ] `workspace-local-retrieval/` skill folder
- [ ] `README.md`
- [ ] optional `LICENSE`
- [ ] optional `release-notes.md`

Do **not** publish:

- [ ] whole private workspace
- [ ] personal notes or memory files
- [ ] runtime state
- [ ] retrieval databases
- [ ] machine-specific configuration snapshots

Suggested repo names:

- `workspace-local-retrieval-skill`
- `openclaw-workspace-local-retrieval`

---

## D. ClawHub Release Gate

Before upload:

- [ ] Re-run skill packaging
- [ ] Confirm packaging validation passes
- [ ] Confirm `.skill` artifact is the latest version
- [ ] Confirm the description matches the current positioning
- [ ] Confirm no private content slipped into references or examples

Artifact expected:

- [ ] `workspace-local-retrieval.skill`

---

## E. LinkedIn Release Gate

Before posting:

- [ ] Lead with the problem and architectural thesis, not just “I published a skill”
- [ ] Emphasize boundary design, agent scoping, and maintenance-aware retrieval
- [ ] Avoid overstating this as a full platform product if it is a skill / pattern
- [ ] Keep the tone technical, clear, and not hype-heavy
- [ ] Be ready to answer “Why is this better than naive local RAG?”
- [ ] Be ready to explain the intentional tradeoffs

Good framing:
- retrieval as architecture
- memory governance
- privacy-aware local-first design
- multi-agent boundary control
- operational reliability

Avoid weaker framing:
- generic AI memory buzzwords
- “index everything” language
- hype without tradeoffs

---

## F. Final Confidence Check

Ask these before pressing publish:

- [ ] Would a recruiter understand why this is non-trivial?
- [ ] Would a senior engineer see clear design judgment here?
- [ ] Would a privacy-minded reader feel the safety stance is deliberate?
- [ ] Would I be comfortable walking through this in an interview?
- [ ] Does this represent the kind of engineering taste I want associated with my name?

If any answer is “not yet,” revise before publishing.
