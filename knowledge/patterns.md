# Learned Patterns

<!-- Automatically maintained by knowledge-manager. Do not edit manually unless necessary. -->

---

## Agent Behavior

### Sign as "Pertev" + sub-agent attribution
*Consolidated: 2026-05-14 | Source: 2026-05-10 session | Confidence: high*

The assistant signs all responses as "— Pertev". When relaying a sub-agent result, prefix with "responding on behalf of [agent-name]". This helps the user track which agent is active.

### Staged knowledge review is user-driven
*Consolidated: 2026-05-14 | Source: 2026-05-10 session | Confidence: high*

Rampdown writes new inferences to staged-knowledge.md but does NOT prompt the user to review them. Staged knowledge review is the user's own responsibility, done on their own schedule. Consolidation is a separate, explicitly-triggered action.

---

## Session Lifecycle

### Rampup/Rampdown naming + trigger phrases
*Consolidated: 2026-05-14 | Source: 2026-05-10 session | Confidence: high*

Session startup is called "Rampup" (also accepts "Brief"). Session shutdown is called "Rampdown" (also accepts "Debrief"). Trigger phrases: Rampup = "rampup", "brief me", "let's start". Rampdown = "rampdown", "debrief", "goodbye", "wrap up", "we're done", "close session". User prefers "rampup/rampdown" as primary names.

### Missed rampdown detected via file state
*Consolidated: 2026-05-14 | Source: 2026-05-10 session | Confidence: high*

Agent has no access to previous chat sessions. Missed rampdown detection is file-based: git status (uncommitted files), staged-knowledge.md (pending items), log file dates (last session date ≠ today). Surfaced non-blocking at rampup.

---

## Knowledge Management

### todos.md vs backlog.md separation
*Consolidated: 2026-05-14 | Source: 2026-05-10 session | Confidence: high*

todos.md = user's personal task list. backlog.md = ecosystem/agent improvement items. These are distinct files with distinct purposes.

---

## Tooling

### Prefer ntfy.sh for push notifications
*Consolidated: 2026-05-14 | Source: 2026-05-10 session | Confidence: high*

For push notifications, prefer ntfy.sh: simpler API, free, no per-device payment. Pushover remains a known alternative.

### Obsidian is a rendering layer, not a storage layer
*Consolidated: 2026-05-14 | Source: 2026-05-14 session | Confidence: high*

Obsidian is a UI/rendering layer over plain markdown files — it does not impose a format or require migration. Value becomes meaningful only after wikilinks and structured metadata exist. Defer Obsidian setup until PKM Improvements 2 and 3 (wikilinks + ADR migration) are implemented.
