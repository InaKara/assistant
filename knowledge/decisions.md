# Decision Log

<!-- Key decisions and their rationale, maintained by knowledge-manager. -->

## 2026-05-08 — Initial Architecture

- **Decision:** Orchestrator + 7 core sub-agents (knowledge-manager, agent-factory, task-planner, researcher, reviewer, auditor, service-architect)
- **Rationale:** Separation of concerns. Orchestrator delegates, never executes directly.
- **Autonomy:** Medium — act on routine, confirm on agent/skill modifications.
- **Knowledge:** Hybrid storage (memory system + SKILL.md + dedicated knowledge files).
- **Logging:** Hybrid — real-time agent-side logging + verbatim message history + session export.
- **Self-improvement:** Always confirm before modifying any agent, skill, or knowledge file.
