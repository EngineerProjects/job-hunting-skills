# Project conventions — NEXUS

This file is for any agent (Claude, Codex, or NEXUS itself) working on the NEXUS project.
Read it before making changes. These conventions are mandatory.

---

## Project identity

NEXUS is an AI-native orchestration runtime and operational workspace.
Goal: build, coordinate, and execute intelligent workflows, tools, agents, and automation
systems through a modular, extensible, production-oriented architecture.

Two execution models: **mono-run** (single agent, fully autonomous, no human checkpoints)
and **team-run** (multiple specialized agents coordinating in one execution context).

---

## Versioning

- Bump PATCH (`0.0.X`) by default for every shippable commit.
- Bump MINOR for new primitives, new execution modes, or breaking tool API changes.
- Bump MAJOR for runtime architecture changes.
- After bumping:
  1. `git tag -a v<X.Y.Z> -m "..."`
  2. `gh release create v<X.Y.Z> --title "v<X.Y.Z>" --notes "<changelog>" --latest`

---

## Commits

- Co-author trailer is fine: `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>`
- Verify locally before push: runtime smoke test passes, no broken agent references.
- Keep commits focused: one primitive / one agent / one integration per commit.

---

## Architecture conventions

- `core/` — runtime engine, task lifecycle, agent loop. No business logic here.
- `orchestrator/` — routing, team coordination, mono-run scheduler.
- `agents/` — agent definitions (role, tools, constraints, handoff rules).
- `tools/` — registered tools available to agents. Each tool is typed and versioned.
- `skills/` — packaged skill bundles callable by agents.
- `memory/` — working memory, long-term store, shared team state.
- `integrations/` — external connectors (APIs, browsers, DBs, file systems).
- `runtime/` — execution modes: interactive, mono-run, team-run.
- `config/` — environment, agent profiles, orchestration policies.

---

## Layer separation

- No LLM calls in scripts or tools. All content generation happens in the running agent.
- Tools do I/O only — file ops, API calls, bash commands, browser actions.
- Agents declare which tools they use. No undeclared side effects.
- All model calls must be traceable — no silent sub-agent spawning.

---

## Agent definition rules

- Every agent has: `name`, `role` (one sentence), `model`, `tools`, `memory` scope, `handoff_to`, `escalate_on`.
- Roles are single-purpose. An agent that does everything does nothing well.
- Escalate to human only on hard blockers — not on every uncertainty.

---

## testing/ is gitignored

Local scratch for API keys, sample responses, integration tests.
Never write secrets above `testing/`.

---

## Validation before push

```bash
# TODO: replace with actual smoke test once stack is defined
python3 -c "import nexus; print('OK')"
```
