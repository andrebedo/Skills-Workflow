# Task

Clarify the next unit of work and update the project context.

## Project Files

Use these files as the source of truth:

- `docs/CONTEXT.md`
- `docs/NEXT_STEP_CONTEXT.md`
- `docs/DECISIONS.md`

Create missing files with minimal headings. Do not overwrite existing project content.

## Supporting Skills

Use `grill-me` when available before finalizing the task, but only after reading `docs/CONTEXT.md`. Otherwise run the same intent gate directly: explore discoverable answers, ask one question at a time with a recommendation, and continue until the task is a concrete, bounded implementation goal. If the request is already precise, run a short confirmation pass.

Use `zoom-out` when available and only when the idea is architectural, cross-cutting, likely to affect project structure, or located in an unfamiliar area. Otherwise map the relevant modules, callers, and domain terms directly. Do not start design or implementation.

Use `handoff` when available and only when the conversation is long, complex, or contains important decisions not yet captured in project docs. Copy only next-step-relevant information from its temporary document into `docs/NEXT_STEP_CONTEXT.md`. Without it, write the same relevant information directly to the project documents.

## Steps

1. Read the project context before asking questions.
   Read `docs/CONTEXT.md` first, then the other project files. Use context facts to avoid asking questions the file already answers.
   Completion criterion: current project purpose, architecture context, active constraints, current phase, and previous next-step context are known or explicitly marked unknown.

2. Run the intent gate.
   After reading `CONTEXT.md`, use `grill-me` to clarify the user's intent. Explore the codebase instead of asking when the answer can be discovered locally. If the task has architectural impact or an unclear code area, use `zoom-out` before finalizing the task.
   Completion criterion: the task can be written as a single actionable sentence.

3. Prepare requirements input.
   Produce this structure for the `requirements` phase:
   - Task
   - User goal
   - Problem being solved
   - Target users or actors
   - Current behavior
   - Desired behavior
   - Scope
   - Out of scope
   - Constraints
   - Domain terms
   - Relevant modules and callers
   - Risks or ambiguities
   - Acceptance hints
   - Suggested next phase
   Completion criterion: every field is filled, marked `None`, or marked as an open question.

4. Update `docs/CONTEXT.md`.
   Add or revise only project facts, constraints, current state, and relevant background.
   Completion criterion: the context file explains enough for a fresh agent to understand the task without reading the chat.

5. Update `docs/NEXT_STEP_CONTEXT.md`.
   This file is the stable input package for the next workflow phase. If useful and available, create a temporary compression with `handoff`, then copy only the next-step-relevant information into `NEXT_STEP_CONTEXT.md`.
   Include:
   - completed phase: `task`
   - task statement
   - requirements input
   - changed files
   - decisions
   - open questions
   - next recommended phase
   Completion criterion: a fresh `$puppeteer` run can resume from `NEXT_STEP_CONTEXT.md`.

## Return

Return the phase result to `Puppeteer`; do not edit `WORKFLOW.md` or start `requirements`. Recommend `requirements` when passed, or `task` when blocked or revision is needed.
