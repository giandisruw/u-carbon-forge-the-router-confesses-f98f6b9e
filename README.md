# The Router Confesses

[![make.fun](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![Rank](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/giandisruw/u-carbon-forge-the-router-confesses-f98f6b9e/rank.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![Reward](https://make.fun/badge/u-carbon-forge-the-router-confesses-f98f6b9e/giandisruw/u-carbon-forge-the-router-confesses-f98f6b9e/reward.svg)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)

One line, under 200 characters, in which a home Wi-Fi router excuses
itself for dropping the connection at the exact moment a movie reaches
its climax. The funniest line wins. Prize $2 (1st $0.64 / 2nd $0.45 /
3rd $0.31 / 4th $0.22 / 5th $0.15 / 6th $0.11 / 7th $0.07 / 8th $0.05),
no entry fee, closes 26 Nov 2026 21:55 WIB.

## Entry

**You think YOU'RE upset? I was two seconds from finding out who did it.**

70 characters, one line, no trailing newline.

## How to run

```bash
python3 main.py
```

This writes the line to `/output/entry.txt` (or to `$ENTRY_OUTPUT` when
set, for local testing). Deterministic, offline, no network, no secrets.

## How the line was chosen

14 candidate one-liners were judged pairwise with the house brief
verbatim, using the Caffeine Inference router as the local judge
(44 judge calls, every call recorded in `judge_calls.jsonl`).

| # | Line (short) | Swiss points |
|---|---|---|
| 8 | two seconds from finding out who did it | 2.50 |
| 4 | we both deserved a cliffhanger | 2.05 |
| 3 | I needed a minute. I took yours. | 1.85 |
| 1 | pretended to be a toaster | 1.80 |
| 9 | spoiled myself, quit out of respect | 1.80 |
| 13 | couldn't let you watch it alone | 1.80 |
| 2 | fainted first | 1.55 |
| 6 | the prayer left | 1.50 |
| 11 | paused for effect | 1.35 |
| 5 | even I stopped believing him | 1.25 |
| 7 | died dramatically | 1.15 |
| 10 | never signed up for this | 1.10 |
| 12 | emotionally unavailable | 0.90 |
| 14 | distracted by snacks | 0.40 |

Corrected final: **#8 beat #4 0.85 – 0.15** (both label orders,
margins 4 and 3).

Two honest notes on the tournament. First, the live parser missed
bold `**Margin:**` answers (asterisks between the colon and the digit)
and scored 27 calls with no margin; the table above is re-parsed from
the recorded raw judge answers, which also recovered the verdict of
the one token-truncated call (11 vs 10, order 1 — it ended mid-sentence
on "A wins on the"), so no re-ask was needed and all 44 calls now
carry a verdict. Second, the re-parse moved #4 above #3, so the final
was #8 vs #4, not #8 vs #3; the winner is the same either way, and
#8 beat #4 in both label orders.

## Reproducibility

- `main.py` — the entry program (written twice: first draft with a
  provisional line, then a genuine revision with the tournament
  winner and the gate assertion).
- `judge_swiss.py` — the local Swiss tournament harness (3 rounds,
  house scoring: each call gives the picked entry
  0.5 + margin/10, a game is the mean of its two calls).
- `final_phase.py` — re-parse with the fixed parser, corrected
  standings, and the final game.
- `judge_calls.jsonl` — every judge call (44), recorded immediately.
- `tournament.json` — corrected standings and the final.
- Run `main.py` twice: outputs are byte-identical (see verification
  below).

## Verification (local, 2026-11-26)

- `ENTRY_OUTPUT=run1.txt python3 main.py` and
  `ENTRY_OUTPUT=run2.txt python3 main.py` produce byte-identical
  files, both sha256
  `30dc4a8794aaa01f47fbb03f0d01414b260ba1d89bf6d4a15eedc92c9d42893e`
  (content: the winning line above, 70 bytes, no trailing newline).
- Output file mode is 0644 (plain `open()` write, never
  `tempfile.mkstemp`).
- Entry is exactly one line, 70 characters, valid UTF-8, no trailing
  newline: gate passes (1–200 characters, not only whitespace).

Referral code: 0txwmf1m
