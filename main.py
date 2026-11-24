"""Make the AI Judge Laugh: Developer Excuses — one-liner entry.

Writes a single funny developer excuse to /output/entry.txt, no trailing
newline. The line follows the winning pattern for this blind-judge format:
one specific dev detail, a concrete number, and a second beat that flips
the excuse back on the developer.
"""

import pathlib

ENTRY = "It worked on my machine for four minutes, then crashed production for eleven hours. So technically, it worked."

assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"


def main() -> None:
    out_dir = pathlib.Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
