---
name: develop
description: Implement requirements as coherent end-to-end vertical slices. Use only when the workflow skill routes the active session to develop.
---

# Develop

Implement every acceptance criterion and hand test-ready code to the `test` phase.

## Sources

Read first:

- `docs/project/REQUIREMENTS.md` for the requirement and acceptance criteria.
- `docs/project/NEXT_STEP_CONTEXT.md` for the active requirement context.
- `docs/project/CONTEXT.md` for the general architecture.

When present, read `docs/project/ARCHITECTURE.md` for detailed system boundaries, dependencies, and end-to-end flows.

Also read `docs/project/WORKFLOW.md`, `docs/project/DECISIONS.md`, `docs/project/GLOSSARY.md`, and the relevant code. The code is authoritative for the current implementation; documents are authoritative for intended behavior and approved decisions.

## Steps

1. Reconstruct the change.
   Inspect callers, contracts, domain logic, persistence, backend, and frontend touched by the requirement. Use `zoom-out` when unfamiliar modules or cross-layer dependencies obscure the end-to-end flow.
   Completion criterion: every acceptance criterion maps to the affected layers and an ordered set of vertical slices.

2. Resolve material conflicts before editing.
   Infer minor details from repository evidence and record the assumptions. For contradictions or gaps that affect behavior, APIs, data, architecture, scope, or verifiability, summarize the evidence and impacts across all affected layers, recommend a choice, present alternatives, and ask for confirmation.
   Completion criterion: no material conflict remains unresolved; ordinary reversible changes need no approval.

3. Implement all vertical slices.
   Complete one behavior end-to-end before starting the next. Make the minimum coherent change across every necessary layer; do not treat frontend and backend as separate deliveries. Refactor only where required by the requirement. Record non-blocking debt instead of expanding scope. Use `diagnose` when a failure's cause is not immediate.
   Completion criterion: all acceptance criteria are implemented with no requirement-critical placeholder, temporary mock, or TODO.

4. Prepare the code for testing.
   Run the repository's relevant type-check, lint, build, and existing tests. Modify an existing test only when it describes behavior intentionally replaced by the requirement; leave new behavioral coverage to `test`. For UI changes, use `browser:control-in-app-browser` for a brief main-path smoke check when the app can run locally. Distinguish relevant failures from clearly pre-existing unrelated failures.
   Completion criterion: relevant checks pass; unavailable checks and unrelated failures are evidenced and recorded; failures caused by the change block completion.

5. Update shared project state.
   Follow the existing structures in `docs/project`. Update `docs/project/DECISIONS.md` for approved implementation decisions, `docs/project/CONTEXT.md` for general architectural changes, and `docs/project/GLOSSARY.md` for changed domain language. Do not change `docs/project/REQUIREMENTS.md` without explicit approval. Update `docs/project/NEXT_STEP_CONTEXT.md` with completed slices, acceptance-criterion-to-change mapping, changed files, affected contracts and flows, verification results, modified existing tests, scenarios for `test`, assumptions, residual risks, debt, and blockers.
   Completion criterion: the repository and project documents contain every fact the `test` phase needs without chat history.

Do not commit, push, or open a pull request.

## Return

Return the phase result to `workflow`; do not edit `WORKFLOW.md` or start `test`. Recommend `test` when passed, or `develop` when blocked or revision is needed.
