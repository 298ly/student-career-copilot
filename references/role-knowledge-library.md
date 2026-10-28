# Role knowledge library and company-pack contract

## One human-facing entrance

Use this layout by default:

```text
<learning-root>/
├── 00_从这里开始.md
├── 方向学习库/
│   ├── 数据分析/
│   ├── 信贷风控/
│   └── <new role family only when justified>/
├── 个人项目答案/
└── 公司专项/
    └── <company_role>/
```

The root index is the only general entrance. Each subfolder may have its own index, but it must state its scope and link back to the root. Do not create new peer roots such as `Downloads/数分学习求职` or `Downloads/风控学习求职`.

## Classify before creating

Determine the role family from the majority of core duties, deliverables, data grain, decision loop, and interview prerequisites. Job title alone is not decisive.

Reuse an existing role family when at least the main business workflow and most reusable foundations overlap. For example:

- growth analysis, business analysis, product analysis, and experiment analysis normally extend `数据分析`;
- credit strategy, fraud strategy, risk modeling, collections analytics, and risk data development normally extend `信贷风控`, with subtracks when needed;
- a role using SQL and Python is not automatically data analysis; classify by what decisions the work supports.

Create a new role family only when forcing it into an existing family would hide a materially different workflow, theory base, or deliverable. Record why the new family is needed and which foundations can still be linked instead of copied.

## Separate reusable, personal, and company-specific content

Put content in exactly one primary layer:

### Direction library

Contains reusable knowledge: business workflow, terminology, formulas, metrics, methods, modeling, SQL/Python/tooling, validation, cases, role-common questions, and the full learning order. This is the complete course.

### Personal project answers

Contains only evidence-backed first-person material: self-introduction modules, project stories, internship boundaries, personal contribution, metrics that can be supported, failure and reflection, and likely follow-ups. Share these modules across companies. Never copy a public interview author’s experience into this layer.

### Company pack

Contains only deltas: exact JD snapshot and interpretation, current resume mapping, gaps and risks, company or team context, public interview-report review, targeted question-answer set, company-specific motivation and values, interview-round plan, and a time-bounded study route. Link to universal chapters and personal answers instead of duplicating them.

## Zero-basis teaching standard

For every P0 or P1 concept, use this order:

1. **What problem it solves.** Begin with a concrete business or data problem.
2. **Definition.** Give a precise but plain-language definition.
3. **Intuition.** Explain what changes and why without relying on jargon.
4. **Formula or procedure.** Write the formula when one exists. Define every symbol, unit, numerator, denominator, time window, population, and edge condition.
5. **Inputs and outputs.** State the required data and the result produced.
6. **Worked example.** Use small numbers and calculate step by step, or trace a complete procedural example.
7. **Use conditions.** State assumptions and applicable scenarios.
8. **Failure modes.** Explain when the method is misleading, invalid, or inferior to an alternative.
9. **Common confusion.** Contrast nearby concepts and expose likely traps.
10. **Interview response.** Give a 30–90 second spoken answer that remains understandable without the long explanation.
11. **Follow-ups.** Add likely second-level questions with answers immediately below them.
12. **Source and status.** Distinguish sourced fact, personal evidence, inference, teaching example, and unknown.

Do not call a chapter “complete” when it only provides definitions or memorized conclusions. A beginner must be able to understand the worked example and explain why the method is used.

## Question-answer adjacency

Every interview question must be followed immediately by its answer. Do not maintain a question bank whose answers live in another file unless the question line contains a direct link to the exact answer section. For code questions, include the problem, assumptions, code, line-by-line reasoning, complexity, edge cases, and dialect or runtime limitations.

## JD update workflow

1. Save the exact JD and identify source/date/status.
2. Inspect the actual resume version to be submitted or already submitted.
3. Map each core duty to verified evidence, trainable gap, or unknown.
4. Classify the role family and list reusable concepts missing from its curriculum.
5. Extend the direction library with full zero-basis explanations.
6. Update personal project answers only from inspected evidence.
7. Create or update the thin company pack.
8. Tailor the resume without inventing facts.
9. Add a study route that points first to prerequisite direction chapters, then personal project drills, then company deltas.
10. Validate links, stale paths, empty files, question-answer adjacency, and the zero-basis checklist.

## Completion checks

Before reporting completion, verify:

- one root entry exists under `<learning-root>`;
- no new competing learning root was created outside the configured learning root;
- the JD-specific directory does not duplicate the full curriculum;
- each important unfamiliar term has a real explanation, not only a one-line answer;
- formulas define symbols and include a worked example;
- personal claims point to evidence or are explicitly marked self-reported/unknown;
- public interview reports remain anecdotes, not confirmed company policy or fixed question banks;
- every question is adjacent to its answer;
- all local Markdown links resolve after moving or renaming files.
