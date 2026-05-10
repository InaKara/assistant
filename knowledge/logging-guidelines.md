# Logging Guidelines

All agents in the work-assistant ecosystem must log their activity to daily log files.

## Log Location

`knowledge/logs/YYYY-MM-DD.md`

## Log Format

Each log entry is a markdown section:

```markdown
### [HH:MM] [Agent Name] — [Action]

- **Caller:** [who invoked this agent]
- **Task:** [brief description]
- **Result:** [success/failure + one-line summary]
- **Decision:** [any decision made and rationale, if applicable]
- **Duration:** [approximate]
- **Notes:** [anything noteworthy]
```

## What to Log

| Category | Detail Level | Example |
|---|---|---|
| Agent invocations | Who called whom, task summary | "orchestrator → researcher: find docs on X" |
| Decisions | What was decided and why | "Chose MCP over script because of..." |
| Results | Success/failure + brief summary | "Found 3 relevant docs, synthesized brief" |
| Errors | Full error context | "Agent X failed: [error]. Retried with Y." |
| User activity | Tasks started/completed | "User started: refactor auth module" |
| Knowledge changes | What was stored/modified | "Stored user preference: prefers TypeScript" |

## Rules

- Every agent appends to the daily log as part of its interaction protocol.
- Use concise entries — one log entry should be 3-6 lines.
- Never log sensitive information (passwords, tokens, secrets).
- The auditor agent reads and analyzes these logs for diagnostics.

---

## Verbatim Message History

**Location:** `knowledge/logs/messages/YYYY-MM-DD.md`

The orchestrator must log **every user message verbatim** to enable future knowledge restructuring from raw source.

### Format:

```markdown
### [HH:MM] User Message

> [exact user message, quoted]

**Context:** [what task/topic this relates to]
**Actions taken:** [one-line summary of response]
```

### Rules:
- Log the exact user input — no paraphrasing, no summarizing.
- Include context so the message can be understood later without the full conversation.
- This is the **lossless** record. Activity logs can be lossy; message logs cannot.

### Periodic Export:
- At the end of each session (when the user stops interacting), the orchestrator should prompt to export the full session transcript if any messages were not captured by real-time logging.
- Use the VS Code session debug log as a backup source if needed.
