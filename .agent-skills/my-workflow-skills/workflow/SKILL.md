---
name: workflow
description: Run the complete gated project workflow through task, requirements, develop, test, and review.
disable-model-invocation: true
---

# Workflow

This is the only user entry point. Remain active across phases; the user does not need to invoke phase skills.

## Sources

Read `docs/project/WORKFLOW.md` first, then `docs/project/NEXT_STEP_CONTEXT.md`, `docs/project/CONTEXT.md`, `docs/project/REQUIREMENTS.md`, `docs/project/GLOSSARY.md`, and `docs/project/DECISIONS.md`. Read `docs/project/ARCHITECTURE.md` and `docs/project/TEST.md` when present and relevant. Create missing project files with minimal headings without overwriting content.

The orchestrator alone writes `docs/project/WORKFLOW.md`. Phase skills own their phase behavior and other artifacts; read their `SKILL.md` when routed:

- `task` -> `../task/SKILL.md`
- `requirements` -> `../requirements/SKILL.md`
- `develop` -> `../develop/SKILL.md`
- `test` -> `../test/SKILL.md`
- `review` -> `../review/SKILL.md`

## State Machine

Valid statuses are `in_progress`, `awaiting_confirmation`, `blocked`, and `complete`. Valid outcomes are `pending`, `passed`, `needs_correction`, and `blocked`.

1. On a new session, clear the previous session history, initialize `task` as `in_progress`, and run it. Invoking `$workflow` authorizes this first phase.
2. On resume, continue an `in_progress` phase without another confirmation. For `awaiting_confirmation`, do no phase work: repeat the gate and wait. For `blocked`, request only the input needed to unblock. For `complete`, report the result or initialize a new session when the user supplies a new task.
3. Run exactly one phase skill until its completion criterion, correction outcome, or blocker. Supporting skills may run inside the phase when its instructions call for them; they are not workflow phases.
4. Record the result in `docs/project/WORKFLOW.md`. For `passed` or `needs_correction`, set `awaiting_confirmation` and propose exactly one target. Normal routing is `task -> requirements -> develop -> test -> review -> complete`; corrective routing may move backward. For `blocked`, set `blocked`, record the exact unblock condition, propose no transition, and ask only for the missing input. When supplied, return the same phase to `in_progress`.
5. Present the confirmation gate and stop. On approval, append it to current-session history. For a phase target, set that phase to `in_progress` and run it in the same conversation. For `complete`, close the session. On feedback or rejection, return the current phase to `in_progress`, record the requested revision, rerun it, and propose again.
6. Keep the completed final summary until a new task starts; then clear the closed session history.

Skipping a phase requires an explicit user instruction and recorded rationale. Never close `review` without a green test gate.

## Confirmation Gate

At every forward, corrective, or closure transition, show:

- completed or paused phase and outcome;
- satisfied completion criteria;
- changed files and verification performed;
- decisions, assumptions, risks, debt, and blockers;
- proposed phase or `complete`, and the reason.

End with `Confermi il passaggio a <phase>?` or, for `complete`, `Confermi la chiusura della sessione?` Do not apply the target before approval.

## WORKFLOW.md Contract

Maintain current session, phase, status, outcome, proposed next phase, reason, pending feedback or blocker, last update, final summary, and a compact current-session transition history. The history is append-only during a session and is cleared only when the next session starts.

Each phase returns to this orchestrator with: outcome, completion evidence, changed files, verification, decisions and assumptions, risks and debt, blockers, and recommended next phase. Phase skills never edit `WORKFLOW.md` or ask for the transition themselves.
