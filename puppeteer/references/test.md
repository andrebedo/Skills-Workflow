# Test

Build behavioral evidence for the changed slice and route only a green gate to `review`.

## Independent Test Agent

The primary agent orchestrates this phase but never performs its test work. At every entry into `test`, spawn one fresh secondary agent as the sole test agent. Do not reuse an agent from an earlier `test -> develop -> test` cycle, and do not allow the test agent to spawn further agents.

Give the test agent no inherited conversation or development reasoning. Its context is limited to the durable repository artifacts named under Sources, the changed code, and repository test conventions. The test agent may create and correct tests and may update `docs/TEST.md` and `docs/NEXT_STEP_CONTEXT.md`; it must not modify application code or `docs/WORKFLOW.md`.

Before delegation, the primary agent records the application-code state needed to attribute later changes. After the test agent returns, the primary agent validates its structured phase result and verifies that it contains commands or manual steps, essential output, states, involved files, and acceptance-criterion coverage. The primary agent does not rerun tests. Missing, incomplete, contradictory, or unverifiable evidence is an agent failure.

If the test agent cannot be started, terminates unsuccessfully, returns a non-conforming result, or modifies application code, discard or revert only the application-code changes attributable to that agent and make one automatic recovery attempt with a fresh isolated test agent. Preserve valid test and documentation changes when they can be attributed safely. If the recovery agent also fails, return `agent_failed`; do not classify any test as `BLOCKED` merely because an agent failed, and never fall back to primary-agent test execution. Recommend a fresh `test` phase.

## Sources

Read `docs/REQUIREMENTS.md`, `docs/NEXT_STEP_CONTEXT.md`, `docs/CONTEXT.md`, `docs/WORKFLOW.md`, and the changed code. Use `tdd` and its references when available; otherwise this skill's tracer-bullet and red-green rules are authoritative.

Create `docs/TEST.md` on the first test run. Thereafter preserve its execution history and update it after every test execution.

## Steps

1. Define the gate.
   Map every acceptance criterion and relevant regression risk to observable behavior through public interfaces. Reuse repository test conventions. Do not request another approval when requirements, interfaces, and priorities are clear; ask one targeted question when coverage is unbounded, priority is missing, or testing would change a public contract.
   Completion criterion: every in-scope behavior has a stable test ID and a planned `NOT RUN` entry in `TEST.md`.

2. Run one tracer bullet.
   Select one behavior, add or identify one test, and run only enough verification to establish its state. Never write a batch of new tests before executing the first. Use `browser:control-in-app-browser` only when an acceptance criterion explicitly requires UI behavior and no adequate repository end-to-end runner exists.
   Completion criterion: the selected test is recorded as `GREEN`, `RED`, or `BLOCKED` before another test is created.

3. Classify the result.
   Use `GREEN` only for an executed pass, `RED` for executed non-conforming behavior, `NOT RUN` for planned work, and `BLOCKED` for an environment or dependency preventing execution. Correct evident syntax, setup, fixture, or interface-usage defects in tests and rerun them. Never weaken an assertion to obtain green. Ask for confirmation when a test expectation conflicts with requirements.
   Completion criterion: the state identifies product failure, test defect, or environmental blockage with evidence.

4. Close each red-green cycle.
   On `GREEN`, continue with the next planned behavior. On a valid `RED`, stop adding tests; do not modify application code. Add a failure package to `NEXT_STEP_CONTEXT.md` containing the test ID and description, criterion, command, essential output, expected and observed behavior, suspected area, and attempt count. Return a `needs_correction` outcome recommending `develop`. After `develop`, rerun the red test first, then the pertinent regression. Do not remove or change a valid failing test without explicit approval.
   Completion criterion: each tracer bullet is green before the next begins, or the workflow explicitly waits on `develop`, user input, or an environmental unblock.

5. Stop repeated ineffective loops.
   If the same test remains red after three `test -> develop -> test` cycles, keep it red, summarize all attempts and excluded hypotheses in `TEST.md`, and request a decision before another correction, architectural change, or requirement revision.
   Completion criterion: no fourth correction attempt starts without explicit direction.

6. Refactor tests only while green.
   Remove test duplication and improve names, fixtures, and behavioral clarity without changing coverage or application code. Rerun pertinent verification after every refactor. Record application refactor opportunities as debt or return them to `develop` when required by the requirement.
   Completion criterion: refactored tests remain green through public interfaces.

7. Evaluate and route the gate.
   Require green acceptance tests, pertinent regressions, type-check, lint, and build; require no in-scope `RED`, `NOT RUN`, or `BLOCKED`. Record proven pre-existing unrelated failures without blocking. Summarize results in `NEXT_STEP_CONTEXT.md`. When green, recommend `review`; when blocked, recommend `test`; when red, recommend `develop`.
   Completion criterion: a fresh `$puppeteer` run selects the correct next action without chat history.

## TEST.md Contract

Keep an immutable execution log and an updateable `Current gate`. Assign stable IDs such as `T-001`. Each execution records: cycle, test ID, short domain-language description, acceptance criterion ID and text, level, exact command or manual steps, state, evidence, and involved test files. Include unit, integration, end-to-end/UI, manual, type-check, lint, and build verification when applicable.

## Return

Return the phase result to `Puppeteer`; do not edit `WORKFLOW.md` or start another phase. The allowed results from this playbook are `passed`, `needs_correction`, `blocked`, and `agent_failed`. Use `agent_failed` only for failure of both the initial test agent and its single automatic recovery agent; display it as `AGENT_FAILED` in user-facing reports.
