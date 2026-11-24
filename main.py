#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun entry.

Writes exactly one job title to <MAKEFUN_OUTPUT_DIR>/entry.txt.
The title is a fixed constant, so every run produces byte-identical output.
"""

import os

TITLE = "Senior Apologizer for Self-Driving Cars"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
