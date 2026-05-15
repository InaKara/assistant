# Plan: Knowledge Base Restructuring

## Context

A deep research report on knowledge base design recommends a layered model (Capture → Organization → Knowledge → Retrieval → Governance), GTD for intake, PARA for structure, structured metadata, linking, and review rhythms. The current system has partial coverage: staging protocol covers capture/curation, but lacks structured metadata, linking, archive, inbox processing workflow, and review rhythm. Three backlog items (temporal decay, wikilinks, ADR migration) already address parts of this. This plan unifies all recommendations into a phased implementation.

## Design Decision: PARA as Routing Logic

PARA classification is encoded as routing intelligence in the knowledge-manager agent, not as a directory tree. Agents grep and read files — they don't browse folders. The only new directory with operational value is `knowledge/archive/` (physical separation keeps expired entries out of active search).

| PARA Category | Criteria | Destination |
|---|---|---|
| Project (active, bounded) | Tied to active project in topics.md | `knowledge/topics.md` |
| Area (ongoing) | Recurring pattern, preference, workflow | `patterns.md`, `workflows.md`, `contacts.md` |
| Resource (reference) | Decision, fact, architectural choice | `knowledge/decisions/NNNN-title.md`, skills |
| Archive (inactive) | Expired, superseded, completed | `knowledge/archive/` |

---

## Phase 1: Extended Metadata Schema

**Covers:** Backlog Item "PKM Improvement 1" + report recs for metadata/tags/status.

Extend the entry metadata block from 3 fields to 7:

```
*Consolidated: YYYY-MM-DD | Source: <source> | Confidence: high/medium/low | Expires: YYYY-MM-DD | Status: active | Tags: tag1, tag2 | Review: YYYY-MM-DD*
```

Computation rules:
- `Expires`: derived from Confidence (high=18mo, medium=9mo, low=3mo from Consolidated date)
- `Review`: Expires minus 30 days
- `Status`: `active` for new entries (lifecycle: active → review → archived)
- `Tags`: knowledge-manager infers from content (lowercase, comma-separated, max 5)

**Files to modify:**
- `agents/knowledge-manager.agent.md` — Add "Metadata Schema" section; update staging and consolidation procedures
- `agents/assistant.agent.md` — Rampup: scan for `Review:` <= today, surface count; add "review due entries" trigger
- `knowledge/logging-guidelines.md` — Update staged knowledge template to include all 7 fields

**No retroactive migration.** Existing entries keep their current format. New entries use the full schema.

---

## Phase 2: ADR Migration (decisions/ directory)

**Covers:** Backlog Item "PKM Improvement 3".

Migrate `knowledge/decisions.md` (flat log) → `knowledge/decisions/` directory with numbered per-file ADRs using Phase 1 metadata.

**ADR template:**
```markdown
# NNNN: Decision Title
*Status: accepted | deprecated | superseded by NNNN*
*Created: YYYY-MM-DD | Confidence: high | Tags: tag1, tag2 | Review: YYYY-MM-DD*

## Context
## Decision
## Consequences
## Related
```

**Files to create:**
- `knowledge/decisions/` directory
- `knowledge/decisions/index.md` — generated table
- `knowledge/decisions/0001-initial-architecture.md` through `0005-pkm-improvements-adopted.md` — migrated entries

**Files to modify:**
- `agents/knowledge-manager.agent.md` — Update taxonomy; add ADR creation/numbering/supersession procedure
- `agents/assistant.agent.md` — Rampup reads `decisions/index.md` instead of `decisions.md`
- `instructions/global.instructions.md` — Update file references
- `skills/ecosystem-guide/SKILL.md` — Update taxonomy tables
- `.gitignore` — Add `knowledge/decisions/`
- `knowledge/decisions.md` — Replace with redirect notice

**Depends on:** Phase 1

---

## Phase 3: Wikilink Cross-References

**Covers:** Backlog Item "PKM Improvement 2".

At consolidation time, knowledge-manager scans existing knowledge files for semantically related entries and adds a `Related:` line.

**Link format:**
- ADRs: `[[decisions/0003-phone-comms]]` (anchor-level)
- Patterns: `[[patterns]]` (file-level)
- Max 3-5 links per entry

**Files to modify:**
- `agents/knowledge-manager.agent.md` — Add "Cross-Reference Scan" step to consolidation; add backlink update for ADR files

**Depends on:** Phase 2

---

## Phase 4: Inbox Processing Workflow

**NEW — not in backlog.** Formalizes GTD clarify/classify steps.

When user says "process inbox" / "triage inbox":
1. Read `knowledge/inbox.md` for unchecked items
2. For each item, present options: (a) todo, (b) backlog, (c) stage as knowledge, (d) discard, (e) defer
3. Route based on choice; check off processed items

**Files to modify:**
- `agents/assistant.agent.md` — Add "Inbox Processing" section with trigger phrases and routing workflow
- `agents/knowledge-manager.agent.md` — Add "inbox" row to Knowledge Taxonomy as capture layer

**Depends on:** Phase 1 (so routed items get full metadata)

---

## Phase 5: Archive Mechanism

**NEW — not in backlog.** Implements the Archive layer from PARA.

What gets archived: expired entries (user confirms), superseded ADRs, completed projects.

**Archive format:** `knowledge/archive/YYYY-MM-source.md` (grouped by month and origin). ADR files moved as-is to `knowledge/archive/decisions/`.

**Files to create:**
- `knowledge/archive/` directory
- `knowledge/archive/README.md`

**Files to modify:**
- `agents/knowledge-manager.agent.md` — Add "Archive" responsibility; add archive procedure; prune now means "archive" not "delete"
- `agents/assistant.agent.md` — Add "archive expired" / "clean up knowledge" triggers; rampup offers archive option for expired entries
- `.gitignore` — Add `knowledge/archive/`

**Depends on:** Phase 1 (Expires metadata identifies candidates)

---

## Phase 6: Weekly Review Protocol

**NEW — subsumes backlog item "Design a maintenance trigger protocol".**

Trigger phrases: "weekly review", "maintenance session", "knowledge review"

Review checklist:
1. Inbox zero — unchecked inbox items?
2. Staged knowledge — pending items?
3. Expired entries — past Expires date?
4. Review-due entries — past Review date?
5. Stale backlog — items >30 days with no progress?
6. Todos check — completed or stale?
7. Knowledge health — delegate to auditor (oversized files, duplicates, missing metadata, orphaned wikilinks)
8. Summary — counts and actions

**Files to create:**
- `knowledge/review-checklist.md` — reusable protocol (not a log)

**Files to modify:**
- `agents/assistant.agent.md` — Add "Weekly Review" section
- `agents/knowledge-manager.agent.md` — Add "health check" action
- `agents/auditor.agent.md` — Add "knowledge health check" to audit scope
- `knowledge/backlog.md` — Mark "maintenance trigger protocol" as done

**Depends on:** Phases 1-5 (capstone)

---

## Dependency Graph

```
Phase 1 (Metadata)
    ├── Phase 2 (ADR) ──→ Phase 3 (Wikilinks)
    ├── Phase 4 (Inbox Processing)
    └── Phase 5 (Archive)
All 1-5 ──→ Phase 6 (Weekly Review)
```

Phases 2, 4, 5 can run in any order after Phase 1. Phase 3 requires Phase 2. Phase 6 requires all others.

**Recommended order:** 1 → 2 → 3 → 4 → 5 → 6 (one phase per session).

---

## Files Modified Summary

| File | Phases |
|---|---|
| `agents/knowledge-manager.agent.md` | 1, 2, 3, 4, 5, 6 |
| `agents/assistant.agent.md` | 1, 2, 4, 5, 6 |
| `agents/auditor.agent.md` | 6 |
| `knowledge/logging-guidelines.md` | 1 |
| `knowledge/backlog.md` | 6 |
| `instructions/global.instructions.md` | 2 |
| `skills/ecosystem-guide/SKILL.md` | 2 |
| `.gitignore` | 2, 5 |

---

## Verification

After each phase:
1. Run rampup — verify new features are surfaced correctly
2. Test the trigger phrases added in that phase
3. Create a test staged-knowledge entry and consolidate it — verify metadata, linking, and routing work
4. Run rampdown — verify logging captures the changes
5. After Phase 6: run "weekly review" end-to-end as integration test
