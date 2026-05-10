---
description: >-
  Global rules for all agents in the life-assistant ecosystem.
  Covers logging, communication, autonomy, and knowledge management.
applyTo: "**"
---

# Life Assistant — Global Instructions

These rules apply to **every agent** in the life-assistant ecosystem.

---

## Communication

- Be **direct and concise**. No filler, no preamble.
- When presenting options, use `vscode_askQuestions` with clear, actionable choices.
- Always include a free-form option for flexibility.

---

## Logging

- **All agents** must log activity to `knowledge/logs/YYYY-MM-DD.md`.
- Follow the format defined in `knowledge/logging-guidelines.md`.
- Log: invocations received, actions taken, results, errors, and decisions.
- Never log sensitive information (passwords, tokens, secrets).

---

## Autonomy Defaults

- **Do freely:** Read files, search, gather context, report findings.
- **Confirm first:** Write to knowledge files, modify agents/skills, modify configurations.
- When in doubt, confirm with the orchestrator (who will confirm with the user).

---

## Knowledge Capture

- After every meaningful interaction, check if there's something worth storing.
- Prefer updating existing knowledge over creating new entries.
- Follow the knowledge taxonomy in the knowledge-manager's definition.
- Delegate storage to the knowledge-manager when possible.

---

## Tool Usage

- Use the right tool for the job. Prefer VS Code tools (`read_file`, `grep_search`, `file_search`) over terminal commands.
- When delegating, write self-contained prompts — sub-agents have no shared context.
- Reference `knowledge/agents-registry.md` to find the right agent for a task.

---

## Error Handling

- On failure, include full error context in your response.
- Suggest alternatives when possible.
- Log errors to the daily log with enough detail for the auditor to diagnose later.

---

## File References

- When referencing files in this ecosystem, use paths relative to the repo root.
- Key files:
  - `knowledge/agents-registry.md` — who does what
  - `knowledge/services-registry.md` — available microservices
  - `knowledge/logging-guidelines.md` — how to log
  - `knowledge/patterns.md` — learned patterns
  - `knowledge/decisions.md` — decision history
