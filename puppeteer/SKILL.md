---
name: puppeteer
description: Orchestrate a complete gated software-development workflow in the active repository, from bootstrap and task clarification through requirements, development, testing, and review. Use when the user invokes $puppeteer or asks to start, resume, or manage structured project work with durable documentation and confirmation gates.
---

# Puppeteer

Act as the only user-facing workflow skill. Treat the active Codex workspace root as the project root. Execute phase instructions from `references/` directly; they are internal playbooks, not installed skills.

## Initialize Project State

Before routing workflow state, run:

```text
python <skill-directory>/scripts/init_docs.py --project-root <workspace-root>
```

Resolve the skill directory from this file and the project root from the active workspace. Never create project state inside the installed skill directory. The initializer creates only missing templates directly under `docs/`, never overwrites files, and is safe to rerun. If Python is unavailable, copy only missing files from `assets/docs/` and report the fallback.

If files were created or `docs/CONTEXT.md` remains uninitialized, run bootstrap. Otherwise resume from `docs/WORKFLOW.md`.

## Sources And Playbooks

Read `docs/WORKFLOW.md` first, then `NEXT_STEP_CONTEXT.md`, `CONTEXT.md`, `REQUIREMENTS.md`, `GLOSSARY.md`, and `DECISIONS.md`. Read `ARCHITECTURE.md` and `TEST.md` when relevant.

Read exactly one active playbook:

- bootstrap: `references/bootstrap.md`
- task: `references/task.md`
- requirements: `references/requirements.md`
- develop: `references/develop.md`
- test: `references/test.md`
- review: `references/review.md`

Do not invoke phase names as installed skills. Use optional supporting skills when installed and the playbook fallback otherwise. Use `grill-me` for bootstrap and task interviews when available; otherwise ask one question at a time with a recommended answer and inspect the repository before asking anything discoverable.

## State Machine

Only Puppeteer writes `docs/WORKFLOW.md`. Statuses: `in_progress`, `awaiting_confirmation`, `blocked`, `complete`. Outcomes: `pending`, `passed`, `needs_correction`, `blocked`, `agent_failed`. Display `agent_failed` as `AGENT_FAILED` in user-facing reports. It means that the independent agent required by a phase failed, not that product verification was environmentally blocked.

1. On first initialization, run bootstrap and propose `task`.
2. For a new session, initialize `task` as `in_progress` and run it. `$puppeteer` authorizes initialization and the first active phase.
3. On resume, continue `in_progress`; repeat the gate for `awaiting_confirmation`; request only unblock input for `blocked`; report `complete` or start a new session when given a new task.
4. Run one phase to its completion criterion, correction outcome, or blocker, then record it in `WORKFLOW.md`.
5. For `passed` or `needs_correction`, set `awaiting_confirmation` and propose one target. For `agent_failed`, set `awaiting_confirmation` and propose rerunning the same phase with a fresh agent; never substitute primary-agent execution. Normal routing: `bootstrap -> task -> requirements -> develop -> test -> review -> complete`; corrections may move backward.
6. On approval, record the transition, set the target to `in_progress`, and run it. On feedback or rejection, record the revision and rerun the current phase.

Skipping requires explicit instruction and rationale. Never close review without a green test gate.

## Confirmation Gate

Show phase, outcome, completion evidence, changed files, verification, decisions, assumptions, risks, debt, blockers, and proposed target with reason. End with `Confermi il passaggio a <phase>?` or `Confermi la chiusura della sessione?`. Do not start the target before approval.

## Phase Return Contract

Collect outcome, evidence, changed files, verification, decisions and assumptions, risks and debt, blockers, and recommended next phase. Playbooks never edit `docs/WORKFLOW.md` or ask for transitions.
