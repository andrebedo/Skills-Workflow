# Puppeteer

Puppeteer is a single personal Codex skill that guides a project through a gated development workflow:

```text
bootstrap -> task -> requirements -> develop -> test -> review -> complete
                                  ^         |
                                  |---------|
                                    correction
```

## Installation

Copy only the `puppeteer/` directory into the personal Codex skills directory:

```text
~/.codex/skills/puppeteer/
```

Reload Codex after copying it. Puppeteer is the only installed entry point; the phase files under `references/` are internal playbooks and are not loaded as separate skills.

## Usage

Open Codex in the repository to manage and invoke:

```text
$puppeteer
```

On first activation, Puppeteer creates missing workflow files directly in that repository:

```text
docs/
|-- CONTEXT.md
|-- DECISIONS.md
|-- GLOSSARY.md
|-- NEXT_STEP_CONTEXT.md
|-- REQUIREMENTS.md
`-- WORKFLOW.md
```

Existing files are preserved. `TEST.md` is created only during testing and `ARCHITECTURE.md` only during review. Re-running `$puppeteer` reads `docs/WORKFLOW.md` and resumes the recorded phase.

Puppeteer inspects the repository before asking questions. It uses `grill-me` internally when available and follows the same one-question-at-a-time method when it is not installed. Other optional integrations such as `zoom-out`, `diagnose`, `tdd`, `handoff`, and browser control also have internal fallbacks.

The `test` phase is executed by a fresh, isolated secondary agent rather than by the primary workflow agent. The tester works only from durable repository artifacts, may change tests and test documentation, and cannot change application code or delegate further. If it fails, Puppeteer retries once with another fresh tester. A second agent failure produces the distinct `AGENT_FAILED` outcome and proposes rerunning `test`; it is not reported as a blocked product test, and the primary agent never takes over test execution.

Creating the missing workflow documents is automatic. Code changes, scaffolding, dependency installation, incompatible configuration edits, phase transitions, and session closure require the approvals described by the playbooks.

## Skill Layout

```text
puppeteer/
|-- SKILL.md
|-- agents/openai.yaml
|-- assets/docs/*.md
|-- references/*.md
`-- scripts/init_docs.py
```

- `SKILL.md` is the only discoverable skill definition.
- `assets/docs/` contains templates bundled with the skill, not project documents.
- `scripts/init_docs.py` copies only missing templates to the active project.
- `references/` contains the bootstrap, task, requirements, develop, test, and review playbooks.

## Guarantees

- The installed skill directory is never used as the project root.
- Existing project documents are never overwritten by initialization.
- Only Puppeteer writes `docs/WORKFLOW.md`.
- Each transition requires confirmation.
- Testing is owned by a fresh independent agent on every entry into the phase.
- Test-agent failure is retried once, then reported as `AGENT_FAILED` without primary-agent fallback.
- A failed test may route the workflow back to development.
- Review cannot close without a green test gate.

## License

Released under the MIT License.
