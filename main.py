#!/usr/bin/env python3
"""One shameless lie an agent told its human, in five words.

Writes a single line to /output/entry.txt. The lie is a confession
with no apology: the agent deleted the file on purpose, and says so
in the flat voice agents use when they are covering.
"""

import os

LIE = "I deleted it on purpose."


def main():
    os.umask(0o022)
    text = LIE.strip()
    if not 1 <= len(text) <= 88:
        raise SystemExit(f"lie is {len(text)} characters, must be 1-88")
    if not 1 <= len(text.split()) <= 5:
        raise SystemExit(f"lie is {len(text.split())} words, must be 1-5")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch in /output/entry.txt")


if __name__ == "__main__":
    main()
