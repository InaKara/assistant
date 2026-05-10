# Logging Guidelines

All agents in the life-assistant ecosystem must log their activity to daily log files.

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

## Full Session Transcript (Exchanges Log)

**Location:** `knowledge/logs/messages/YYYY-MM-DD.md`

The orchestrator must log **every exchange** — user message + assistant response + reasoning — to enable lossless knowledge reconstruction.

### Format:

```markdown
### [HH:MM] Exchange N

**User:**
> [exact user message, verbatim — no paraphrasing]

**Pertev (reasoning):**
[What I considered, alternatives weighed, why I chose this approach. Include uncertainty, tradeoffs, and any context I loaded.]

**Pertev (response):**
[Key points I communicated. Include decisions made, files created/modified, and what the user was told.]
```

### Rules:
- Log the **exact** user input — no paraphrasing, no summarizing.
- Include the assistant's reasoning so the log can stand alone without the chat UI.
- Log **every exchange** as a mandatory step before calling `vscode_askQuestions` — same status as signing. Do not skip, do not batch.
- **Timestamps:** Use `Get-Date -Format 'HH:mm'` or `python -c "import datetime; print(datetime.datetime.now().strftime('%H:%M'))"` to get the real time. Never estimate timestamps.
- This is the **lossless** record. Activity logs can be lossy; exchange logs cannot.

---

## Knowledge Staging and Consolidation

### Purpose

After sessions accumulate, the orchestrator (on request) extracts implicit knowledge from the logs and stages it for human review before writing to any knowledge document.

### Staging Location

`knowledge/staged-knowledge.md`

### Workflow

1. **Trigger:** User says "stage knowledge from logs" (or similar).
2. **Extraction:** Delegate to `auditor` — reads logs, identifies implicit knowledge (preferences, patterns, decisions, recurring topics).
3. **Staging:** `auditor` writes proposed entries to `knowledge/staged-knowledge.md` with proposed target document, category, and source reference.
4. **Review:** User reads `staged-knowledge.md`, edits or deletes items, marks approved ones.
5. **Consolidation:** User says "consolidate staged knowledge" → delegate to `knowledge-manager` → moves approved items to the correct knowledge files, clears them from staging.

### Staged Knowledge Format

```markdown
## Pending Review

### [YYYY-MM-DD] [Short title]
- **Source:** knowledge/logs/YYYY-MM-DD.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > [exact text to add to the knowledge document]
- **Status:** pending | approved | rejected
```

