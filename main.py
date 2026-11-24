"""One-Liner Marathon entry: a deadpan maintenance log.

The joke is written as a flat inspection report. Every clause sounds
routine until the last one quietly escalates: a passenger who has been
waiting since 2019 is now legally part of the building.
"""

import os
from pathlib import Path

ENTRY = (
    "Maintenance log: elevator inspected, cables fine, buttons fine, "
    "one passenger still waiting since 2019 and now legally part of "
    "the building."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 280 or not text.strip():
        raise ValueError("entry must be 1 to 280 non-whitespace characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
