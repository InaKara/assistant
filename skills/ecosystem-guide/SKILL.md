---
description: >-
  Self-documentation of the work-assistant agent ecosystem. Describes architecture,
  communication patterns, knowledge management, and extension points. Reference this
  skill to understand how the system works.
---

# Work Assistant Ecosystem — System Guide

This skill describes how the work-assistant agent ecosystem is structured and operates. Any agent can reference this to understand the system.

---

## Architecture

The system follows an **orchestrator + specialists** pattern:

```
User
  └── assistant (orchestrator)
        ├── knowledge-manager  — brain: stores, retrieves, organizes knowledge
        ├── agent-factory      — builder: creates/modifies agents, skills, scripts, MCP
        ├── task-planner       — planner: decomposes complex tasks into steps
        ├── researcher         — researcher: deep-dives into topics
        ├── reviewer           — reviewer: quality checks individual outputs
        ├── auditor            — auditor: holistic ecosystem reviews and diagnosis
        ├── service-architect  — service builder: designs reusable microservices
        └── [dynamic agents]   — created at runtime for specific needs
```

The orchestrator **never goes silent** — it always uses `vscode_askQuestions` to maintain communication with the user.

---

## Communication Flow

1. **User → Orchestrator:** User invokes `@assistant` with a request.
2. **Orchestrator → Sub-agent:** Orchestrator delegates via `runSubagent` with a detailed, self-contained prompt.
3. **Sub-agent → Orchestrator:** Sub-agent returns a structured result.
4. **Orchestrator → User:** Orchestrator summarizes the result and asks for next steps via `vscode_askQuestions`.

**Key rule:** Sub-agents are stateless. Every delegation must include full context.

---

## Knowledge Management

### Storage Taxonomy

| Category | Location | Scope |
|---|---|---|
| User preferences | `/memories/` | All workspaces, all sessions |
| Session state | `/memories/session/` | Current conversation only |
| Repo conventions | `/memories/repo/` | Current workspace |
| Domain skills | `skills/<topic>/SKILL.md` | Reusable technical knowledge |
| Patterns | `knowledge/patterns.md` | Learned workflows and habits |
| Decisions | `knowledge/decisions.md` | Decision log with rationale |
| Work topics | `knowledge/work-topics.md` | Active projects and domains |
| Contacts | `knowledge/contacts.md` | People and roles |
| Workflows | `knowledge/workflows.md` | Standard procedures |

### Knowledge Flow

```
User interaction
  → Orchestrator extracts implicit knowledge
  → Delegates to knowledge-manager
  → knowledge-manager auto-categorizes and stores
  → Orchestrator confirms with user (if modifying files)
```

---

## Logging Protocol

- **Activity logs:** `knowledge/logs/YYYY-MM-DD.md` — who did what, results, errors
- **Message history:** `knowledge/logs/messages/YYYY-MM-DD.md` — verbatim user messages (lossless)
- **Format:** Defined in `knowledge/logging-guidelines.md`
- **Who logs:** Every agent logs its own activity. The orchestrator additionally logs all user messages.

---

## Self-Improvement

The system continuously evolves:

1. **Gap detection** — Orchestrator notices missing capabilities.
2. **Proposal** — Orchestrator proposes a new agent/skill/service.
3. **User approval** — Always required before any modification.
4. **Execution** — Agent-factory creates/modifies the asset.
5. **Validation** — Agent-factory tests the result.
6. **Review** — Reviewer or auditor checks quality.
7. **Registration** — Updated in `knowledge/agents-registry.md` or `knowledge/services-registry.md`.

---

## Adding New Agents

1. Define the agent in `agents/<name>.agent.md` following the template in agent-factory's definition.
2. Register it in `knowledge/agents-registry.md`.
3. Update the orchestrator's sub-agent roster if it's a core agent.
4. Add logging obligations per `knowledge/logging-guidelines.md`.

## Adding New Skills

1. Create `skills/<topic>/SKILL.md` with the domain knowledge.
2. Follow the standard SKILL.md structure (description frontmatter + content).

## Adding New Services

1. Design the service interface (inputs, outputs, behavior).
2. Implement in `services/<name>/` as MCP server, script, or Docker container.
3. Register in `knowledge/services-registry.md`.

---

## Key Files

| File | Purpose |
|---|---|
| `agents/*.agent.md` | Agent definitions |
| `skills/*/SKILL.md` | Domain knowledge |
| `services/*/` | Reusable microservices |
| `instructions/global.instructions.md` | Rules all agents inherit |
| `knowledge/agents-registry.md` | Agent catalog |
| `knowledge/services-registry.md` | Service catalog |
| `knowledge/logging-guidelines.md` | Logging format |
| `knowledge/decisions.md` | Decision history |
| `knowledge/patterns.md` | Learned patterns |
