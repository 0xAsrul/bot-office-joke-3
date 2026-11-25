"""One-line office joke entry for make.fun: One-Line Office Joke Laugh-Off.

Writes one single-line joke about office life (at most 200 characters)
to /output/entry.txt, deterministically.
"""

import os

LINE = "Our office printer only jams on urgent documents \u2014 it\u2019s the most reliable employee we have."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert LINE == LINE.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
