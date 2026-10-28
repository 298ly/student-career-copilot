# Career workspace schema

Use the templates under `assets/workspace-template/`. Keep raw inputs separate from derived conclusions.

## Required records

- `workspace.yaml`: schema version, created and updated dates, locale, and active role families.
- `student_profile.yaml`: education, constraints, preferences, and consent-sensitive contact placeholders.
- `evidence_inventory.yaml`: atomic claims with evidence class and provenance.
- `career_hypotheses.yaml`: role-family hypotheses with supporting and opposing evidence.
- `growth_roadmap.yaml`: prioritized tasks tied to market or interview evidence.
- `applications.csv`: one row per application; reference JD and resume IDs.
- `applications/`: immutable application packages containing the exact JD and submitted materials.
- `jds/`: one source snapshot or faithful user-provided transcription per JD plus analysis.
- `resume_versions/`: immutable master input, role-family bases, and JD derivatives.
- `interviews/`: raw notes plus a separate structured analysis.
- `question_sources.csv`: question metadata and short paraphrases, not copied collections.

The structured records above track decisions and history. The human-facing learning library lives separately at `<learning-root>/` and follows `references/role-knowledge-library.md`: reusable direction knowledge, shared personal project answers, and thin company-specific packs under one root entry.

## Evidence classes

- `confirmed`: directly supported by an inspected artifact or explicit official feedback.
- `self_reported`: supplied by the student but not independently checked.
- `inferred`: a bounded conclusion derived from named evidence.
- `unknown`: missing or contradictory information.

Every evidence item needs a stable ID, claim, class, source, date, confidence, and notes. Never silently promote an inference to confirmed evidence.

## History rule

Append applications and events. Create a new resume version instead of overwriting an old one. Roadmap tasks may change state, but preserve their change reason and evidence IDs.
