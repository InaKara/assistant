# Agent Registry

<!-- Catalog of all agents, their status, and capabilities. Maintained by agent-factory. -->

| Agent | File | Status | Role |
|---|---|---|---|
| assistant | `agents/assistant.agent.md` | active | Orchestrator — delegates all tasks, never executes directly |
| knowledge-manager | `agents/knowledge-manager.agent.md` | active | Knowledge storage, retrieval, and organization |
| agent-factory | `agents/agent-factory.agent.md` | active | Creates, modifies, and restructures agents and skills |
| task-planner | `agents/task-planner.agent.md` | active | Breaks complex tasks into steps, identifies dependencies |
| researcher | `agents/researcher.agent.md` | active | Deep research, doc reading, web fetching, synthesis |
| reviewer | `agents/reviewer.agent.md` | active | Quality review of code, plans, agents, and outputs |
| auditor | `agents/auditor.agent.md` | active | Holistic ecosystem review, log analysis, diagnosis |
| service-architect | `agents/service-architect.agent.md` | active | Designs and builds reusable microservices as tools |

## External Agents

Available from other repos (require those repos to be in the agent plugins path):

| Agent | Source | Status | Role |
|---|---|---|---|
| sw-developer | agents-skills repo | available | Software feature implementation with structured planning |
| vibe-coding | agents-skills repo | available | Architecture planning and design sessions |
| Deploy Automation Guide | agents-skills repo | available | CI/CD and deployment automation |
| personal-github | agents-skills repo | available | GitHub repo management with identity isolation |
| Premium Request Saver | agents-skills repo | available | General-purpose with session continuity |
| Explore | built-in | available | Fast read-only codebase exploration |
