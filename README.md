# Work Assistant

An orchestrator agent ecosystem for VS Code Copilot. Manages sub-agents, accumulates knowledge, and self-improves to assist with all professional tasks.

## Architecture

```
assistant (orchestrator)
├── knowledge-manager  — stores, retrieves, organizes knowledge
├── agent-factory      — creates/modifies agents, skills, scripts
├── task-planner       — breaks complex tasks into actionable steps
├── researcher         — deep research & synthesis
├── reviewer           — quality review & feedback
├── auditor            — holistic ecosystem review & diagnosis
└── service-architect  — designs reusable microservices as tools
```

## Setup

Add this repo to your VS Code Copilot agent plugins path so all agents and skills are discovered globally.

## Knowledge Structure

```
knowledge/
├── agents-registry.md      — catalog of all agents
├── services-registry.md    — catalog of reusable microservices
├── patterns.md             — learned patterns and workflows
├── decisions.md            — key decisions and rationale
├── work-topics.md          — active projects and domains
├── contacts.md             — key people and their roles
├── workflows.md            — standard workflows
├── logging-guidelines.md   — logging format and rules
└── logs/
    ├── YYYY-MM-DD.md       — daily activity logs
    └── messages/
        └── YYYY-MM-DD.md   — verbatim user message history
```

Personal data (user profile, preferences) stored in `/memories/` (user memory) for cross-workspace persistence.

## Services

Reusable microservices in `services/` — implemented as MCP servers, local scripts, or Docker containers. See `knowledge/services-registry.md` for the catalog.
