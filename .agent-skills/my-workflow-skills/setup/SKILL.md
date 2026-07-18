---
name: setup
description: Bootstrap a project and install the complete workflow kit.
disable-model-invocation: true
---

# Setup

Run this once from the downloaded workflow-kit folder. Bootstrap the containing project, then hand a verified project context to `$workflow`.

## Boundaries

Treat the folder containing this kit as the source and its parent as the default project root. Never create application files, project documentation, manifests, lockfiles, or dependencies inside the kit. If source or target is ambiguous, show both paths and ask one question.

Preserve existing project content. Before incompatible edits, replacement, installation, scaffolding, global tooling, or system changes, show the exact plan and ask for confirmation. Prefer project-local dependencies and the existing package manager.

## Steps

1. Discover source and target.
   Locate the kit, inspect the proposed project root for Git, manifests, code, documentation, and toolchain markers, and classify it as new or existing.
   Completion criterion: source, project root, project state, existing stack, and conflicts are known.

2. Install the skill kit.
   Copy the personal `.agent-skills/my-workflow-skills/` tree into the project root. Preserve unrelated skills and merge only after disclosing overwritten workflow-kit files. Detect optional `grill-me`, `zoom-out`, `diagnose`, `tdd`, `handoff`, `ubiquitous-language`, `setup-pre-commit`, and browser support in the project or user environment. Offer installation through an available skill installer when a trusted source is known; otherwise use the phase fallback and record the missing integration.
   Completion criterion: every workflow skill exists in the project root and every optional integration is available or recorded as skipped with its fallback.

3. Reconstruct an existing project.
   Inspect code, manifests, scripts, tests, deployment configuration, and existing docs. Use `zoom-out` when boundaries or flows are unclear. Do not ask questions answerable from the repository.
   Completion criterion: observed architecture, tooling, runnable commands, and material gaps are known; for a new project they are explicitly absent.

4. Run the project interview.
   Use `grill-me` when available; otherwise apply its contract directly: ask one question at a time, recommend an answer, inspect the repository instead of asking discoverable questions, and follow dependent decisions to shared understanding. Resolve vision, problem, users, core use cases, capabilities, platform, distribution, data, integrations, constraints, non-goals, technology preferences, security, accessibility, performance, and operational needs. Keep feature-level requirements for `task` and `requirements`.
   Completion criterion: every topic is answered, inferred from evidence, marked not applicable, or retained as an explicit open question.

5. Propose the bootstrap.
   For a new or incomplete project, recommend a minimal compatible stack, structure, runtime, package manager, application dependencies, formatter, lint, type checking where available, test and coverage tooling, build and quality commands, local Mermaid CLI, environment-example handling, and `.gitignore`. Offer pre-commit through `setup-pre-commit` and a minimal CI pipeline for the detected repository platform. Verify current stable versions from official sources and respect existing constraints. Every proposed dependency must have an immediate consumer.
   Show alternatives only when they materially change trade-offs, then show files, dependencies, versions, commands, and risks. Ask for confirmation.
   Completion criterion: one complete bootstrap plan is explicitly approved.

6. Apply the approved plan.
   Integrate rather than overwrite. Use project-local dependencies, update manifests, generate the lockfile, and avoid global installs unless unavoidable and separately approved. For a new project, create only a runnable infrastructure tracer bullet: application start, configuration, health behavior, and one proving test; implement no product feature.
   Completion criterion: every approved file and dependency exists, no speculative dependency was added, and unrelated existing behavior is preserved.

7. Verify the environment.
   Run the exact install, format/lint, type-check, test, build, application smoke, dependency-audit, and Mermaid commands that apply. Validate that CI runs the same reproducible quality commands. Report vulnerabilities and incompatible fixes; never apply a breaking security upgrade without approval. Use browser support for a runnable web smoke test and `diagnose` for non-obvious failures. Record commands, installed versions, results, and recovery actions. Do not report success while a relevant check fails.
   Completion criterion: all applicable checks pass, or setup is explicitly blocked with reproducible evidence.

8. Publish the workflow input.
   Create missing `docs/project/` files from the kit templates; merge existing files without discarding content. Update `CONTEXT.md` with stable project context and environment facts. Seed `GLOSSARY.md` from the interview, using `ubiquitous-language` when available. Record durable choices in `DECISIONS.md`. Keep `REQUIREMENTS.md` free of invented feature requirements. Update `NEXT_STEP_CONTEXT.md` with bootstrap results, changed files, verification, open questions, and next phase `task`. Initialize `WORKFLOW.md` to `task / in_progress / pending`.
   Completion criterion: a fresh `$workflow` can begin without chat history.

9. Close the bootstrap.
   Present source and target, project summary, installed skills and dependencies, changed files, verification, decisions, risks, skips, and open questions. Ask: `Confermi che il progetto e pronto per $workflow?` On approval, record setup completion and tell the user to invoke `$workflow`; do not start it.
   Completion criterion: readiness is approved and the sole next command is `$workflow`.

## Recovery

Setup is idempotent. On rerun, detect completed work, preserve lockfiles and configuration, skip verified steps, and resume from the first incomplete criterion. Record blockers and recovery actions in `NEXT_STEP_CONTEXT.md`.
