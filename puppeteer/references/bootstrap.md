# Bootstrap

Bootstrap the active project once, then return verified context to Puppeteer.

## Boundaries

Treat the active Codex workspace root as the project root. The initializer has already created any missing workflow files directly under `docs/`. Never copy or install phase skills into the project and never write project state inside the installed Puppeteer directory.

Preserve existing content. Creating missing workflow documents is automatic. Before incompatible edits, dependency installation, scaffolding, global tooling, or system changes, show the exact plan and request separate approval. Prefer project-local dependencies and the existing package manager.

## Steps

1. Inspect the repository for Git, manifests, code, documentation, tests, deployment configuration, and toolchain markers. Classify it as new or existing. Do not ask questions answerable from repository evidence.
2. Use `grill-me` when installed to resolve vision, problem, users, use cases, platform, data, integrations, constraints, non-goals, security, accessibility, performance, and operations. Otherwise reproduce its contract: ask one question at a time, recommend an answer, and explore the repository first.
3. For a new or incomplete project, propose a minimal compatible bootstrap only when necessary. Show files, dependencies, commands, trade-offs, and risks. Do not apply it without explicit approval.
4. Apply only the approved plan. Integrate rather than overwrite, avoid global installs, respect existing lockfiles, and create no product feature during infrastructure bootstrap.
5. Run every applicable install, formatting/lint, type-check, test, build, application-smoke, dependency-audit, and Mermaid command. Report failures; never claim success while a relevant check fails.
6. Populate `docs/CONTEXT.md` with stable project and environment facts. Seed `docs/GLOSSARY.md`, record durable choices in `docs/DECISIONS.md`, and keep `docs/REQUIREMENTS.md` free of invented feature requirements.
7. Update `docs/NEXT_STEP_CONTEXT.md` with bootstrap evidence, changed files, verification, decisions, skipped optional integrations, open questions, and recommended phase `task`.

## Completion

Return outcome, evidence, changed files, verification, decisions, assumptions, risks, debt, blockers, and recommended phase `task` to Puppeteer. Do not edit `docs/WORKFLOW.md` and do not ask for the transition.

Bootstrap is idempotent. On rerun, preserve existing configuration and resume from the first incomplete criterion.