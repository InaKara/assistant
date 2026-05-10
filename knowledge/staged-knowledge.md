# Staged Knowledge

> Inferred from logs and session history. Review, edit, or delete entries before consolidating.
> To consolidate approved items: ask the assistant to "consolidate staged knowledge".

---

## Pending Review

### [2026-05-10] User prefers ntfy.sh over Pushover for notifications
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > For push notifications, prefer ntfy.sh: simpler API, free, no per-device payment. Pushover remains a known alternative.
- **Status:** pending

### [2026-05-10] Personal vs. work separation via gitignore, not branching
- **Source:** knowledge/logs/messages/2026-05-10.md
- **Proposed target:** knowledge/decisions.md
- **Proposed entry:**
  > Decision: personal/work artifact separation is handled by gitignoring knowledge files (logs, todos, patterns, etc.), not by branching or separate repos. The same repo code is cloned to different machines; local knowledge stays local.
- **Status:** pending

### [2026-05-10] Option B (background script auto-executing phone commands) is too risky
- **Source:** knowledge/logs/messages/2026-05-10.md
- **Proposed target:** knowledge/decisions.md
- **Proposed entry:**
  > Decision: phone-to-agent communication uses polling on session startup (Option A), not a background watcher (Option B). Option B creates an unauthenticated remote-execution attack surface via ntfy topics.
- **Status:** pending

### [2026-05-10] Sign as "Pertev", add sub-agent attribution
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > The assistant signs all responses as "— Pertev". When relaying a sub-agent result, prefix with "responding on behalf of [agent-name]". This helps the user track which agent is active.
- **Status:** pending

### [2026-05-10] Separate todos (user tasks) from backlog (ecosystem improvements)
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > todos.md = user's personal task list. backlog.md = ecosystem/agent improvement items. These are distinct files with distinct purposes.
- **Status:** pending

### [2026-05-10] Session lifecycle uses Rampup / Rampdown naming (also: Brief / Debrief)
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > Session startup is called "Rampup" (also accepts "Brief"). Session shutdown is called "Rampdown" (also accepts "Debrief"). Trigger phrases: Rampup = "rampup", "brief me", "let's start". Rampdown = "rampdown", "debrief", "goodbye", "wrap up", "we're done", "close session". User prefers "rampup/rampdown" as primary names.
- **Status:** pending

### [2026-05-10] Missed rampdown detected via file state, not chat history
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > Agent has no access to previous chat sessions. Missed rampdown detection is file-based: git status (uncommitted files), staged-knowledge.md (pending items), log file dates (last session date ≠ today). Surfaced non-blocking at rampup.
- **Status:** pending

### [2026-05-10] Two-tier knowledge file structure for domain separation
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/decisions.md
- **Proposed entry:**
  > Decision: use `<file>.local.md` alongside committed knowledge files for domain-specific content. `.local.md` files are gitignored. Universal inferences go to committed file; domain-specific to `.local.md`. When in doubt, default to local. Applied to: backlog, staged-knowledge.
- **Status:** pending

### [2026-05-10] Staged knowledge review is user-driven, not part of rampdown
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > Rampdown writes new inferences to staged-knowledge.md but does NOT prompt the user to review them. Staged knowledge review is the user's own responsibility, done on their own schedule. Consolidation is a separate, explicitly-triggered action.
- **Status:** pending

### [2026-05-10] Session lifecycle uses Brief / Debrief naming
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > Session startup is called "Brief". Session shutdown is called "Debrief". Trigger phrases: Brief = "brief me", "let's start", new session. Debrief = "debrief", "goodbye", "wrap up", "we're done", "close session". These terms are intentional — borrowed from professional briefing workflows.
- **Status:** pending

### [2026-05-10] Missed debrief is detected non-blocking at startup
- **Source:** knowledge/logs/2026-05-10.md
- **Proposed target:** knowledge/patterns.md
- **Proposed entry:**
  > When starting a new session, the Brief checks for a missed debrief from the previous session (uncommitted changes, pending staged knowledge). This is surfaced as a non-blocking offer, not a forced step. User can defer to later in the session.
- **Status:** pending

---

## Approved (ready to consolidate)

*(none yet)*

---

## Consolidated (archived)

*(none yet)*
