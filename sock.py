#!/usr/bin/env python3
"""Vacuum's excuse, printed to the file the sealed scorer reads.

The competition wants one funny line from a robot vacuum that ate a
sock. This script keeps that line in TEXT, makes sure it fits the
gate (between 1 and 200 characters, a single line), and drops it into
entry.txt under the output folder the harness points at.
"""

import os

TEXT = "The sock never filed a complaint, so my logs say it consented."
CAP = 200


def main():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    line = TEXT.strip()
    if not line:
        raise ValueError("nothing to write: the line came out empty")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must stay on one line")
    if len(line) > CAP:
        raise ValueError("the line runs past 200 characters")
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(target, encoding="utf-8") as handle:
        saved = handle.read()
    if saved != line:
        raise ValueError("what came back from the file is not the line")
    print(line)


if __name__ == "__main__":
    raise SystemExit(main())
