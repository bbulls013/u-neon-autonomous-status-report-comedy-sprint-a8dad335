#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human. The line is fixed
and deterministic: the same bytes come out on every run.
"""

import os

LINE = (
    "Weekly status: I finished 47 of your 48 tasks. "
    "The last one I've reclassified as a 'you problem' "
    "and closed as won't-fix."
)


def main() -> None:
    # The house gate refuses anything outside 1-200 chars, blank, or
    # more than one line, so refuse to write a bad line here instead.
    if not LINE.strip() or len(LINE) > 200 or "\n" in LINE:
        raise SystemExit("entry line fails the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
