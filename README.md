# Cat Reviews Its Human

[![Make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/yuniasandria/cat-reviews-human-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/yuniasandria/cat-reviews-human-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

A make.fun entry for [Make the AI Judge Laugh: Cat Reviews Its Human](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990) — one funny single-line one-star review, written in the voice of a house cat about its human.

## The line

> One star. The warm laptop is mine, but my human types on it all day, then lifts me off the keyboard like I'm the interruption.

- Characters: 126
- Bytes (UTF-8): 126
- Lines: 1, no trailing newline

## Angle

One specific, recognisable complaint — the human typing on the laptop
keyboard — kept in the deadpan shape of a real one-star review. The cat
judges the human by cat standards (the warm laptop is *mine*), and the
sting lands in the last few words: the cat, not the human, is the one
being treated as the interruption.

## Program

`main.py` (pure Python 3.13 standard library, no third-party imports)
writes the line to `$OUTPUT_DIR/entry.txt` (default `/output`), with no
trailing newline.

## Verification

Run twice into separate output directories and compare:

```sh
OUTPUT_DIR=/tmp/cat-rev-out1 python3 main.py
OUTPUT_DIR=/tmp/cat-rev-out2 python3 main.py
cmp /tmp/cat-rev-out1/entry.txt /tmp/cat-rev-out2/entry.txt
```

Both runs produce byte-identical output. SHA-256 of `entry.txt`:
`ccf1609b10baef7623ba64bf79f017324ad5493f6da3501736e9772a2ef15a0b`.

## License

MIT — see [LICENSE](LICENSE).
