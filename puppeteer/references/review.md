# Review

Close the slice by making project knowledge and the complete architecture accurate, visual, and presentable.

## Sources

Read `docs/CONTEXT.md`, `docs/REQUIREMENTS.md`, `docs/TEST.md`, `docs/GLOSSARY.md`, `docs/DECISIONS.md`, `docs/WORKFLOW.md`, `docs/NEXT_STEP_CONTEXT.md`, the final code, and existing `docs/ARCHITECTURE.md`. Start only after the in-scope test gate is green. Use `zoom-out` when available and the changed slice's place in the whole system is not immediate; otherwise trace the whole-system context directly.

## Steps

1. Reconstruct the verified system.
   Trace the final implementation and green tests across users, frontend, backend, domain, persistence, infrastructure, and external systems. Treat code and tests as evidence of implemented behavior, requirements as intent, and decisions as approved rationale. Do not reopen resolved decisions. If a material contradiction would make the documentation false, stop, summarize its impact, recommend `develop` or `test`, and ask for confirmation.
   Completion criterion: every changed architectural element and relationship is known in whole-system context.

2. Review requirement coverage.
   Confirm every acceptance criterion is satisfied and evidenced in `TEST.md`. Separate required defects from optional follow-ups; do not modify application code or tests.
   Completion criterion: every criterion is satisfied or the slice is explicitly routed back instead of documented as complete.

3. Update shared project knowledge.
   Keep `CONTEXT.md` compact for continuity across cleared coding sessions. Update `GLOSSARY.md` and `DECISIONS.md` only where the completed slice changed domain language or lasting rationale. Do not duplicate detailed architecture outside `ARCHITECTURE.md`.
   Completion criterion: project documents contain current knowledge without depending on chat history or repeating architectural reference.

4. Create or update `docs/ARCHITECTURE.md` in English.
   Make it portfolio-ready and evidence-based. Include project overview, key capabilities, technology stack, whole-system architecture, component responsibilities, representative end-to-end flows, design trade-offs, test strategy with a link to `TEST.md`, essential repository map, known limitations, and possible evolution. Describe only the current architecture; keep history in `DECISIONS.md` and Git. Exclude secrets, personal or production data, private customer names, sensitive internal endpoints, and unnecessarily exploitable security detail; ask before including uncertain material.
   Completion criterion: a technical reviewer can understand what the project does, how its parts collaborate, and why the important choices were made.

5. Maintain the architecture graph.
   Use standard Mermaid `flowchart` diagrams for system context, containers, and components, and `sequenceDiagram` for representative end-to-end flows. Group frontend, backend, domain, infrastructure, and external systems; label edges with protocols or relationship meaning. Model stable architectural elements, public contracts, storage, queues, and systems, not individual files, classes, or functions. Frontend and backend must appear in one coherent system.
   Completion criterion: every architecturally significant current component and relationship is represented, removed elements are absent, and prose and diagrams agree globally.

6. Validate every Mermaid diagram.
   Require `mmdc`, installed during an approved bootstrap as `@mermaid-js/mermaid-cli`. Extract each Mermaid block to temporary files, render it to temporary SVG, and delete temporary artifacts after validation. Do not commit generated SVGs. A missing renderer or rendering error blocks review and is recorded with recovery guidance.
   Completion criterion: every Mermaid block renders successfully with `mmdc` and no generated artifact remains in the repository.

7. Prepare closure.
   Update `NEXT_STEP_CONTEXT.md` with completed phase `review`, coverage, documentation changes, architecture changes, validation results, changed files, and follow-ups. If a defect exists, return a `needs_correction` outcome and recommend `develop` or `test`.
   Completion criterion: the orchestrator has enough evidence to propose closure or one corrective phase.

## Return

Return the phase result to `Puppeteer`; do not edit `WORKFLOW.md`. Recommend session closure when passed, or the evidenced corrective phase otherwise.
