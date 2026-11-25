#!/usr/bin/env python3
"""The Router Confesses — entry program (revision v2).

Writes one line to /output/entry.txt (or $ENTRY_OUTPUT for local
testing): a home Wi-Fi router excusing itself for dropping the
connection at the exact moment a movie reaches its climax.
Deterministic, offline, no network, no secrets.

The line is the winner of a 14-candidate Swiss tournament (3 rounds +
final, 44 judge calls, house brief verbatim, Caffeine Inference router
as local judge — see tournament.json and judge_calls.jsonl):
  "You think YOU'RE upset? I was two seconds from finding out who did it."
70 characters, one line, no trailing newline. It beat #4
("I heard the violins swell and decided we both deserved a cliffhanger.")
0.85 - 0.15 in the final (margins 4 and 3, both label orders).
"""
import os

LINE = "You think YOU'RE upset? I was two seconds from finding out who did it."

OUT = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    assert 1 <= len(LINE) <= 200, "gate: entry must be 1-200 characters"
    assert LINE.strip(), "gate: entry must not be only whitespace"
    out_dir = os.path.dirname(OUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
