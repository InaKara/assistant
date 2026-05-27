# Backlog

Items to address in future sessions. Maintained by the assistant.

---

## Open

- [x] **Rename "work-assistant" → domain-agnostic branding** — Replace all `work-assistant ecosystem` / `Work Orchestrator` / `professional tasks` references across agents, instructions, skill, and logging guidelines. Rename `knowledge/work-topics.md` → `knowledge/topics.md`. See session 2026-05-10 for full inventory.

- [x] **Deep discussion: how information is stored** — Completed 2026-05-14. Research brief produced by researcher agent. Three improvements decided (see below).

- [ ] **PKM Improvement 1: Temporal decay metadata** — Add optional `Confidence:` (high/medium/low) and `Expires:` (date) fields to knowledge entries. Populated at staging time by the AI using these defaults: high → 12-18 months, medium → 6-9 months, low → 3 months. Human can override at review. On expiry: flag at rampup only ("⚠️ N entries need re-verification"), no auto-action. **Implementation:** (a) Update `knowledge-manager.agent.md` staging procedure to populate these fields. (b) Update `assistant.agent.md` rampup sequence to grep for `Expires:` dates ≤ today and surface them. No file format migration needed — new entries get fields going forward.

- [ ] **PKM Improvement 2: Wikilink cross-references at consolidation** — At consolidation time, knowledge-manager scans existing knowledge files for semantically related entries and adds a `Related:` line to the new entry. Format: anchor-level for decisions (`[[decisions/0003-phone-comms]]`), file-level for patterns (`[[patterns]]`). Goal: make the knowledge graph explicit so the AI can follow links at retrieval time and Obsidian can render a graph. **Implementation:** Update `knowledge-manager.agent.md` consolidation procedure to add this scan-and-link step before writing entries to target files.

- [ ] **PKM Improvement 3: Migrate decisions.md to per-file ADR format** — Replace `knowledge/decisions.md` (flat log) with `knowledge/decisions/` directory of numbered files. Each file: `0001-decision-title.md` with fields `Status: accepted | deprecated | superseded by [NNNN]`, `Created:`, `Supersedes:`, `Superseded by:`, plus Context / Decision / Consequences sections. When a decision changes: create a new ADR, update old one to `Status: superseded by [NNNN]`. `knowledge/decisions/index.md` is a generated list maintained by knowledge-manager. **Implementation:** (a) Create `knowledge/decisions/` and migrate ~3 existing entries. (b) Update `knowledge-manager.agent.md` to create ADR files (not append to decisions.md). (c) Update `assistant.agent.md` context-load to read `knowledge/decisions/index.md` instead of `decisions.md`. Note: implement after Improvement 2 (wikilinks) so new ADRs get cross-references from the start.

- [ ] **Plan information storage and retrieval improvements** -- Generate a concrete implementation plan from PKM Improvement items 1-3, `knowledge/IMPLEMENTATION-PLAN.md`, and `knowledge/rippling-stirring-whistle.md`.

- [ ] **Create raw input folder** -- Add a repo folder for raw plan or information inputs before they are processed into structured knowledge.

- [ ] **Create deep research teaching/import agent or skill** -- Create an agent/skill that takes `deep_research.md` from `chatgpt.com` files as input, explains or teaches them back to me, and stores them in the knowledge repo.

- [ ] **Define a git sync strategy** — How and when to sync this repo across multiple clones (work, personal). What gets committed (agents, skills, instructions), what stays gitignored (knowledge docs, logs, personal data). Branching strategy if clones diverge.

- [ ] **Test adding services** — Stand up a first `service-architect`-managed microservice. Validate the end-to-end flow: design → define → deploy → invoke from an agent.

- [ ] **Design a maintenance trigger protocol** — Discuss how to structure and invoke a periodic "maintenance session" (review backlog, flush logs, consolidate knowledge, self-audit) given that agents cannot call themselves proactively. Define what the trigger looks like and who/what initiates it.

- [ ] **Define continuous learning strategy** — How to make structured knowledge capture the repo's biggest strength. Topics: what gets captured automatically vs. on-demand, storage taxonomy review, retrieval patterns, when to consolidate vs. archive.

- [ ] **Design auditor knowledge-file review routine** — Define a thorough routine for the `auditor` agent to periodically check all knowledge files. Should cover: detecting misrouted content (domain-specific items in committed files), checking `backlog.md` vs `backlog.local.md` routing, verifying staged knowledge is not stale, flagging sensitive information committed by mistake. Define triggers and output format.

---

## Done

<!-- Completed items moved here with date -->
