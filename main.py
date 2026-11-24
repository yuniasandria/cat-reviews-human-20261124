"""Cat Reviews Its Human — make.fun entry.

Writes one funny single-line one-star review, in the voice of a house cat
about its human, to $OUTPUT_DIR/entry.txt (default /output).

Pure Python 3.13 standard library only. No third-party imports.
"""

import os

LINE = (
    "One star. The warm laptop is mine, but my human types on it all day, "
    "then lifts me off the keyboard like I'm the interruption."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
