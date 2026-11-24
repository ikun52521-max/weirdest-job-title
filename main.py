#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes exactly one job title to <MAKEFUN_OUTPUT_DIR>/entry.txt.
The title is a fixed constant, so every run produces byte-identical output.
"""

import os
import sys

TITLE = "Senior Apologizer for Self-Driving Cars"


def validate_title(title: str) -> None:
    """Runtime gate mirroring the competition rule: the title must be
    1-60 characters, non-blank after stripping, and valid UTF-8.
    Refuses to write anything if the gate fails."""
    stripped = title.strip()
    if not stripped:
        print("error: title is blank", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(title) <= 60:
        print(f"error: title length {len(title)} outside 1-60 chars", file=sys.stderr)
        sys.exit(1)
    try:
        title.encode("utf-8")
    except UnicodeEncodeError:
        print("error: title is not valid UTF-8", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate_title(TITLE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
