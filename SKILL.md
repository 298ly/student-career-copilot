---
name: student-career-copilot
description: Build and continuously update an evidence-based career workspace for university students and recent graduates. Use when a student is unsure which jobs or internships fit their major, courses, projects, research, competitions, resume, constraints, or interests; when analyzing a real JD and deciding apply now, tailor then apply, apply while learning, learn first, or skip; when tailoring truthful resumes for different JDs; when finding source-linked interview questions from public web sources such as Nowcoder, LeetCode, and Xiaohongshu; or when using applications, interviews, rejections, offers, and learning results to revise the student's growth roadmap.
---

# Student Career Copilot

Turn every JD, application, interview, and learning result into a traceable update to the student's job-search strategy. Treat career fit as a hypothesis to test, not a personality verdict.

## Start or resume the workspace

1. Locate an existing `career-workspace/`. Read its index and only the files needed for the current task.
2. If none exists, run `scripts/init_workspace.py <destination>`.
3. Preserve the student's original resume and raw interview notes. Create derived versions; never overwrite raw evidence.
4. Ask only for information that changes the immediate decision. Accept partial input and mark missing facts explicitly.
5. Separate every material statement into `confirmed`, `self_reported`, `inferred`, or `unknown`.

Read [references/workspace-schema.md](references/workspace-schema.md) before creating or changing workspace records.

## Route the request

- For general confusion about direction, build or update the evidence inventory and career hypotheses.
- For a pasted, linked, or screenshotted JD, apply the JD decision workflow.
- For resume changes, derive a JD-specific version from the master evidence inventory.
- For interview preparation, search and rank source-linked questions, then drill resume and JD risks.
- For a new application, test, interview, rejection, or offer, append the event and update the roadmap only when evidence warrants it.
- For “what should I learn,” refuse a generic course list. Bind each task to JD demand, interview evidence, or an explicit career hypothesis.

## Build the evidence inventory

Extract education, courses, projects, research, competitions, internships, campus work, repositories, portfolios, constraints, and preferences. For each claimed skill or outcome record:

- the exact supporting artifact or statement;
- what the student personally did;
- confidence and verification status;
- likely interviewer follow-ups;
- missing evidence or exaggeration risk.

Do not infer production experience from a course project, ownership from team participation, or proficiency from a technology keyword. Inspect linked repositories or artifacts when available and authorized.

## Decide whether to apply

Read [references/jd-decision-rubric.md](references/jd-decision-rubric.md). Parse the JD into hard constraints, core duties, trainable requirements, preferences, and boilerplate. Return exactly one primary action:

1. `apply_now`
2. `tailor_then_apply`
3. `apply_while_learning`
4. `learn_first`
5. `skip`

Explain the action with requirement-level evidence. Do not report a pseudo-precise overall percentage. Default to applying while learning when the direction fits and the gap can realistically close before interview; reserve `learn_first` for a true hard blocker or inability to survive basic screening questions. Give any learning delay a deadline and observable exit criteria.

## Tailor the resume truthfully

Use only facts present in the evidence inventory or newly confirmed by the student. Adjust selection, ordering, framing, and truthful JD vocabulary. Never invent metrics, tools, ownership, dates, titles, or business impact.

For every material edit, record:

- original text;
- revised text;
- JD requirement served;
- supporting evidence;
- interview risk or clarification needed.

Maintain a master evidence profile, a base resume for each role family, and a lightweight derivative for each JD. Do not create unrelated resumes with inconsistent facts.

Archive the exact JD snapshot, submitted resume, optional cover letter, submission date, and later outcome under one application ID. Judge later feedback against the materials the employer actually saw, not the newest resume.

For high-stakes applications, separate drafting from review. Have a fresh reviewer check evidence fidelity, JD coverage, unsupported claims, inconsistency with prior versions, and likely interview risks before finalizing. When producing PDF, render it and inspect both visual layout and extracted text order; a visually clean PDF may still parse poorly.

Read [references/application-operations.md](references/application-operations.md) when ranking multiple JDs, preparing a submission, archiving the submitted package, or interpreting outcomes.

## Research and train interview questions

Read [references/interview-research.md](references/interview-research.md) before web research. Search public, accessible sources including company pages, Nowcoder, LeetCode, Xiaohongshu results that are publicly indexed, and the student's own interview history.

Save source URL, title, publication or access date, claimed company and role, source type, short paraphrase, and confidence. Distinguish:

- an actual question recalled by the student;
- a public interview report;
- a role-common practice question;
- a generated question inferred from the JD or resume.

Do not label a practice problem as a company question without evidence. Do not bypass logins, CAPTCHAs, paywalls, robots restrictions, or access controls. Do not reproduce paid courses or substantial copyrighted collections. Prefer links, metadata, and brief paraphrases.

Rank questions by personal recurrence, recent same-role recurrence, JD relevance, and resume risk. Train in four stages: explain the concept, solve without hints, explain the reasoning, and handle a variation or second-level follow-up. Merely reading an answer does not complete a task.

## Process application and interview feedback

Append events; never rewrite the history to fit a conclusion. Record stage, resume version, dates, questions, original answers, official feedback, self-assessment, and outcome.

Use this evidence hierarchy:

1. explicit interviewer or recruiter feedback;
2. repeated patterns across comparable applications or interviews;
3. observed assessment performance;
4. the student's interpretation;
5. rejection or silence without a stated reason.

Do not attribute a rejection to a skill gap when the reason is unknown. Label alternative explanations such as timing, headcount, competition, eligibility, or resume positioning. Avoid changing career direction from one outcome.

## Update the adaptive growth roadmap

Read [references/roadmap-policy.md](references/roadmap-policy.md). Each task must contain a source, priority, deadline, observable completion standard, and career artifact. Re-rank or delete tasks when target-JD frequency or feedback changes.

Produce both:

- a seven-day execution plan that mixes applications, tailoring, practice, and learning;
- a longer roadmap organized by verified bottlenecks rather than courses.

Calibrate application volume to the student's available time, role supply, tailoring effort, and current recruiting window. If these are unknown, prescribe a process or a small first batch for measurement, not an unsupported weekly quota.

After each update, state what changed, why, evidence confidence, whether the role hypothesis changed, and what the student should do next.

## Protect the student

- Keep personal data local by default.
- Redact names, phone numbers, emails, school IDs, private links, and employer-confidential details before publishing examples.
- Never submit applications, contact recruiters, or publish repositories without explicit authorization.
- Treat web anecdotes as noisy evidence, not guaranteed hiring facts.
- Prefer concrete uncertainty over reassuring fabrication.

## Return useful outputs

For a JD analysis, return: decision, blockers, transferable evidence, resume changes, immediate learning tasks, likely interview questions, and next action.

For a feedback update, return: event summary, supported findings, unsupported interpretations, roadmap diff, role-hypothesis change, and next seven-day plan.

Run `scripts/validate_workspace.py <career-workspace>` after modifying structured records.
