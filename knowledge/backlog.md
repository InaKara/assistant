# Backlog

Items to address in future sessions. Maintained by the assistant.

---

## Open

- [x] **Rename "work-assistant" → domain-agnostic branding** — Replace all `work-assistant ecosystem` / `Work Orchestrator` / `professional tasks` references across agents, instructions, skill, and logging guidelines. Rename `knowledge/work-topics.md` → `knowledge/topics.md`. See session 2026-05-10 for full inventory.

- [ ] **Deep discussion: how information is stored** — Review and discuss the full knowledge taxonomy: what gets stored where (memories, knowledge files, session, repo), how retrieval works, how to make it the ecosystem's biggest strength. Consider vector search, structured vs. free-form, decay and archiving strategies.

- [ ] **Define a git sync strategy** — How and when to sync this repo across multiple clones (work, personal). What gets committed (agents, skills, instructions), what stays gitignored (knowledge docs, logs, personal data). Branching strategy if clones diverge.

- [ ] **Test adding services** — Stand up a first `service-architect`-managed microservice. Validate the end-to-end flow: design → define → deploy → invoke from an agent.

- [ ] **Design a maintenance trigger protocol** — Discuss how to structure and invoke a periodic "maintenance session" (review backlog, flush logs, consolidate knowledge, self-audit) given that agents cannot call themselves proactively. Define what the trigger looks like and who/what initiates it.

- [ ] **Define continuous learning strategy** — How to make structured knowledge capture the repo's biggest strength. Topics: what gets captured automatically vs. on-demand, storage taxonomy review, retrieval patterns, when to consolidate vs. archive.

- [ ] **Design auditor knowledge-file review routine** — Define a thorough routine for the `auditor` agent to periodically check all knowledge files. Should cover: detecting misrouted content (domain-specific items in committed files), checking `backlog.md` vs `backlog.local.md` routing, verifying staged knowledge is not stale, flagging sensitive information committed by mistake. Define triggers and output format.

---

## Done

<!-- Completed items moved here with date -->
