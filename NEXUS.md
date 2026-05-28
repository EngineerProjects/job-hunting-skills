# NEXUS — Agent Context File

This file is for any agent (Claude, Codex, or NEXUS itself) working on the NEXUS project.
Read it before making changes. These conventions are mandatory.

---

## Project identity

**NEXUS** is an AI-native orchestration runtime and operational workspace.

It is designed to build, coordinate, and execute intelligent workflows, tools, agents, and
automation systems through a modular, extensible, production-oriented architecture.

Core differentiators vs Claude Code / Codex:
- Full agentic and sub-agentic system support (not just code assistance)
- **Mono-run automations**: a single agent run that completes an entire task end-to-end without
  human checkpoints — fire, execute, done
- **Team working**: multiple specialized agents collaborating within a single coordinated run,
  each handling a slice of the problem
- Production-oriented: built to run in real environments, not just dev/demo contexts

NEXUS does everything Claude Code and Codex do, and layers on top:
- Autonomous full-run workflows
- Multi-agent team coordination within one execution context
- Extensible tool and skill system
- Orchestration primitives (routing, retry, fallback, handoff)

---

## Architecture overview

```
nexus/
├── core/               # Runtime engine — task lifecycle, agent loop, execution context
├── orchestrator/       # Routing, team coordination, mono-run scheduler
├── agents/             # Agent definitions (role, tools, constraints, handoff rules)
├── tools/              # Registered tools available to agents
├── skills/             # Packaged skill bundles (like this job-hunting repo)
├── memory/             # Context storage — working memory, long-term, shared team state
├── integrations/       # External connectors (APIs, browsers, DBs, file systems)
├── runtime/            # Execution modes: interactive, mono-run, team-run
└── config/             # Environment, agent profiles, orchestration policies
```

> TODO: Update this tree once the actual repo structure is confirmed.

---

## Core concepts

### Mono-run

A **mono-run** is a self-contained, fully autonomous agent execution. No human-in-the-loop.
The agent receives a goal, plans, executes, handles errors, and terminates with a result.

Design contract:
- Input: a well-defined goal + context bundle
- Output: a result artifact + execution log
- No mid-run confirmation prompts
- Failures handled internally (retry, fallback, graceful degradation)
- Idempotent where possible

### Team working

A **team run** is a coordinated execution involving multiple specialized agents.

Architecture:
- One **orchestrator agent** holds the plan and routes subtasks
- N **worker agents** each own a slice (research, coding, validation, writing, etc.)
- Shared memory space for handoffs — no re-explaining context between agents
- Orchestrator decides: serialize, parallelize, or gate (worker B waits for worker A's output)
- Any worker can escalate to orchestrator; orchestrator escalates to human only on hard blockers

### Orchestration primitives

| Primitive | Description |
|---|---|
| `route` | Send a subtask to the most capable agent for it |
| `fork` | Run N subtasks in parallel, collect results |
| `gate` | Block step B until step A produces a required output |
| `retry` | Re-run a failed step with modified input or different agent |
| `handoff` | Transfer context + task ownership from one agent to another |
| `escalate` | Surface a blocker to human only when agents cannot resolve it |

### Tool system

Tools are typed, versioned, and registered. An agent declares which tools it uses.
Tools can be: bash commands, API calls, file ops, browser actions, sub-agents, or skill bundles.

> TODO: Define tool registration spec (schema, auth, versioning conventions).

---

## Agent definitions

Each agent in NEXUS is defined by:

```yaml
name: string           # unique identifier
role: string           # one-sentence description of what this agent does
model: string          # LLM backing this agent (claude-opus-4, gpt-4o, etc.)
tools: [list]          # tools this agent can call
memory: shared | local # whether it reads/writes to team shared memory
handoff_to: [list]     # agents it can hand off to
escalate_on: [list]    # conditions that trigger human escalation
```

> TODO: Add example agent definitions once the spec is stable.

---

## Execution modes

| Mode | Description | Human involvement |
|---|---|---|
| `interactive` | Conversational, Claude Code-style | High — approval at each step |
| `mono-run` | Fire and forget, single agent | None — result at the end |
| `team-run` | Multi-agent coordinated execution | None (or minimal escalation) |
| `supervised` | Team-run with human approval gates at defined checkpoints | Defined checkpoints only |

---

## Versioning

- Bump PATCH (`0.0.X`) for every shippable commit.
- Bump MINOR for new primitives, new execution modes, or breaking tool API changes.
- Bump MAJOR for runtime architecture changes.
- Tag + release after each version bump.

---

## Commits

- Keep commits focused: one primitive / one agent / one integration per commit.
- Co-author trailer: `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>`
- Validate before push: runtime smoke test passes, no broken agent references.

---

## Development conventions

> TODO: Fill in once stack is confirmed (language, package manager, test runner, lint config).

Placeholders:
- **Language**: [Python / TypeScript / Go / other]
- **Package manager**: [pip / npm / cargo / other]
- **Test runner**: [pytest / jest / other]
- **Lint / format**: [ruff / eslint / other]
- **CI**: [GitHub Actions / other]

---

## What NOT to build in NEXUS

- A chatbot or assistant interface — NEXUS is a runtime, not a UI
- Hard-coded workflows — everything should be composable and configurable
- Agents that call other LLMs without declaring it — all model calls must be traceable
- Long-running daemons without health checks and graceful shutdown

---

## Status

> TODO: Track current phase here (e.g. "Phase 1 — core runtime + mono-run agent loop")

Current focus: [fill in]
What's working: [fill in]
What's next: [fill in]
Known blockers: [fill in]
