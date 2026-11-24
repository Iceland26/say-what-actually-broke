"""Say What Actually Broke: print one honest line of software error copy.

The line names the real failure (an expired certificate), when it
happened (3am), and why nobody caught it (the on-call engineer was
asleep) — and lands the joke by blaming the rota design, not the human.
"""

import os

LINE = (
    "The certificate expired at 3am and the on-call engineer "
    "was asleep, as designed."
)


def main() -> None:
    # The gate allows at most 200 characters; fail loudly in
    # development rather than ever shipping an over-long line.
    assert 0 < len(LINE) <= 200, "entry line must be 1-200 characters"
    print(LINE)
    # The program/v1 harness reads the entry from /output/entry.txt
    # when that directory exists; locally there is no /output, so the
    # printed line above is the whole behaviour. A read-only /output
    # must never crash the program: the printed line still counts.
    if os.path.isdir("/output"):
        try:
            with open("/output/entry.txt", "w", encoding="utf-8") as fh:
                fh.write(LINE)
        except OSError:
            pass


if __name__ == "__main__":
    main()
