# Decision Log

<!-- Key decisions and their rationale, maintained by knowledge-manager. -->

## 2026-05-08 — Initial Architecture

- **Decision:** Orchestrator + 7 core sub-agents (knowledge-manager, agent-factory, task-planner, researcher, reviewer, auditor, service-architect)
- **Rationale:** Separation of concerns. Orchestrator delegates, never executes directly.
- **Autonomy:** Medium — act on routine, confirm on agent/skill modifications.
- **Knowledge:** Hybrid storage (memory system + SKILL.md + dedicated knowledge files).
- **Logging:** Hybrid — real-time agent-side logging + verbatim message history + session export.
- **Self-improvement:** Always confirm before modifying any agent, skill, or knowledge file.

---

## 2026-05-10 — gitignore-based work/personal separation
*Consolidated: 2026-05-14 | Confidence: high*

Personal/work artifact separation is handled by gitignoring knowledge files (logs, todos, patterns, etc.), not by branching or separate repos. The same repo code is cloned to different machines; local knowledge stays local.

## 2026-05-10 — Phone comms: polling not background watcher
*Consolidated: 2026-05-14 | Confidence: high*

Phone-to-agent communication uses polling on session startup (Option A), not a background watcher (Option B). Option B creates an unauthenticated remote-execution attack surface via ntfy topics.

## 2026-05-10 — Two-tier `.local.md` file structure for domain separation
*Consolidated: 2026-05-14 | Confidence: high*

Use `<file>.local.md` alongside committed knowledge files for domain-specific content. `.local.md` files are gitignored. Universal inferences go to committed file; domain-specific to `.local.md`. When in doubt, default to local. Applied to: backlog, staged-knowledge.

## 2026-05-14 — PKM improvements adopted (3 decisions)
*Consolidated: 2026-05-14 | Confidence: high*

Three PKM improvements adopted after researcher brief (2026-05-14):
1. Optional `expires`/`confidence` metadata on knowledge entries — populated at staging, flag-only on expiry
2. Wikilink cross-references added at consolidation time — anchor-level for decisions, file-level for patterns
3. `decisions.md` migrated to per-file ADR format with `Status: accepted | superseded` fields

All three are staged in backlog for implementation. Obsidian deferred until improvements 2 and 3 are complete.
