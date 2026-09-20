#!/usr/bin/env python3
"""Perform dependency-free structural checks on a career workspace."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED = [
    "workspace.yaml", "student_profile.yaml", "evidence_inventory.yaml",
    "career_hypotheses.yaml", "growth_roadmap.yaml", "applications.csv",
    "question_sources.csv", "applications", "jds", "resume_versions", "interviews", "raw_inputs",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=Path)
    args = parser.parse_args()
    root = args.workspace.expanduser().resolve()
    errors = [f"missing: {name}" for name in REQUIRED if not (root / name).exists()]
    headers = {
        "applications.csv": ["application_id", "company", "role", "jd_id", "resume_version", "applied_at", "stage", "result", "official_reason", "notes"],
        "question_sources.csv": ["source_id", "url", "title", "platform", "published_at", "accessed_at", "company", "role", "source_type", "question_paraphrase", "confidence"],
    }
    for filename, expected in headers.items():
        path = root / filename
        if path.exists():
            with path.open(newline="", encoding="utf-8-sig") as handle:
                actual = next(csv.reader(handle), [])
            if actual != expected:
                errors.append(f"invalid header: {filename}")
    if errors:
        print("INVALID")
        print("\n".join(errors))
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
