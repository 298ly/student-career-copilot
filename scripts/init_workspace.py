#!/usr/bin/env python3
"""Create a privacy-first career workspace from bundled templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent.parent / "assets" / "workspace-template"
    destination = args.destination.expanduser().resolve()
    if destination.exists() and any(destination.iterdir()):
        parser.error(f"destination is not empty: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
