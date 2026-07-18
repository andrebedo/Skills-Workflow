---
name: requirements
description: Convert a clarified task into implementation-ready requirements. Use only when the workflow skill routes the active session to requirements.
---

# Requirements

Turn the current task into implementation-ready requirements.

## Project Files

Use these files as the source of truth:

- `docs/project/CONTEXT.md`
- `docs/project/REQUIREMENTS.md`
- `docs/project/GLOSSARY.md`
- `docs/project/DECISIONS.md`
- `docs/project/NEXT_STEP_CONTEXT.md`

When a requirement has architectural impact and `docs/project/ARCHITECTURE.md` exists, read it for current system boundaries and dependencies.

Create missing files with minimal headings. Do not overwrite existing project content.

## Steps

1. Read the project files.
   Completion criterion: the current task, existing requirements, glossary terms, decisions, and workflow state are known.

2. Extract requirements.
   Separate functional requirements, non-functional requirements, constraints, assumptions, and acceptance criteria. If a requirement depends on an unresolved product decision, ask one targeted question.
   Completion criterion: every requirement is testable or explicitly marked as an assumption/open question.

3. Update `docs/project/REQUIREMENTS.md`.
   Add the new requirement set under a clear heading. Preserve existing requirements unless the user asked to replace them.
   Completion criterion: the file can guide `develop` without relying on chat memory.

4. Update `docs/project/GLOSSARY.md`.
   Add canonical domain terms, short definitions, known synonyms, and rejected ambiguous terms when relevant.
   Completion criterion: every new domain term used in the requirements is either defined or intentionally left out because it is ordinary language.

5. Update `docs/project/DECISIONS.md`.
   Record only decisions that affect future implementation or workflow.
   Completion criterion: important choices are stated with a short rationale.

6. Update `docs/project/NEXT_STEP_CONTEXT.md`.
   Include:
   - completed phase: `requirements`
   - requirement summary
   - glossary changes
   - decisions
   - changed files
   - open questions
   - next recommended phase
   Completion criterion: a fresh `$workflow` run can resume from `NEXT_STEP_CONTEXT.md`.

## Return

Return the phase result to `workflow`; do not edit `WORKFLOW.md` or start `develop`. Recommend `develop` when passed, or `requirements` when blocked or revision is needed.
