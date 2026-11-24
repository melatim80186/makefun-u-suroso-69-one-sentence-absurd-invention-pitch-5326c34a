#!/usr/bin/env python3
"""make.fun entry: u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.

Writes the one-sentence absurd invention pitch to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "The Self-Untangling Headphones: pulled from your pocket, they perform "
    "a tiny interpretive dance until every knot unties itself in applause."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
