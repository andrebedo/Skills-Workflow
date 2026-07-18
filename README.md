# Skills Workflow

A personal Codex skill kit for a gated software-development workflow, from project bootstrap to final review.

The kit provides two user entry points:

- `$setup` bootstraps the containing project once.
- `$workflow` orchestrates every development session afterward.

## Workflow

```text
setup
  |
  v
task -> requirements -> develop -> test -> review -> complete
                         ^         |
                         |---------|
                       correction
```

`$workflow` records state in `docs/project/WORKFLOW.md` and asks for confirmation before every forward, corrective, or closing transition.

## Installation

Place this repository inside the project you want to create or configure:

```text
your-project/
|-- Skills Workflow/
|-- existing project files...
```

Open Codex in `Skills Workflow` and invoke `$setup`. The skill treats its parent as the default project root, analyzes it, interviews you, proposes the stack and tooling, asks for approval, installs the personal skills, verifies the environment, and prepares the project documents.

After setup is approved, invoke `$workflow`.

## Included Skills

| Skill | Responsibility |
| --- | --- |
| `setup` | Bootstrap the project, tooling, skills, and initial context |
| `workflow` | Own workflow state and orchestrate gated transitions |
| `task` | Clarify one bounded unit of work |
| `requirements` | Produce implementation-ready requirements |
| `develop` | Implement end-to-end vertical slices |
| `test` | Run tracer-bullet behavioral verification |
| `review` | Verify the slice and document its architecture |

The personal skills live in `.agent-skills/my-workflow-skills/`.

## Project Documents

The workflow uses `docs/project/` as durable state:

| Document | Purpose |
| --- | --- |
| `CONTEXT.md` | Project vision, architecture, environment, and constraints |
| `REQUIREMENTS.md` | Active requirements and acceptance criteria |
| `GLOSSARY.md` | Canonical domain language |
| `DECISIONS.md` | Durable decisions and rationale |
| `WORKFLOW.md` | Current session state and confirmed transitions |
| `NEXT_STEP_CONTEXT.md` | Handoff package for the next phase |
| `TEST.md` | Test gate and execution history, created during testing |
| `ARCHITECTURE.md` | Verified architecture, created or updated during review |

Only `workflow` writes `WORKFLOW.md`. Phase skills update their artifacts and return evidence to the orchestrator.

## Optional Integrations

The workflow can use `grill-me`, `zoom-out`, `diagnose`, `tdd`, `handoff`, `ubiquitous-language`, `setup-pre-commit`, and browser control when available.

They are not published in this repository. Every required behavior has an internal fallback, so the personal kit remains usable without them.

## Safety And Reproducibility

- Existing project files are preserved and merged deliberately.
- Material or incompatible changes require approval.
- Dependencies are project-local whenever possible.
- Lockfiles and existing package-manager choices are respected.
- Setup is idempotent and can resume after partial failure.
- No phase transition occurs without confirmation.
- Review cannot close a session without a green test gate.

## Repository Layout

The personal skill sources are in `.agent-skills/my-workflow-skills/`; reusable project-state templates are in `docs/project/`.

## License

Released under the [MIT License](LICENSE).
