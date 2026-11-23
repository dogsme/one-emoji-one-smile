#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt: a big, open,
genuinely happy smile -- warm at first glance, readable by any
stranger of any age or background, with no irony, intimacy, or
in-joke attached.
"""

from pathlib import Path

EMOJI = "\U0001f604"  # 😄 grinning face with smiling eyes
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(EMOJI, encoding="utf-8")
    assert OUTPUT.read_text(encoding="utf-8") == EMOJI


if __name__ == "__main__":
    main()
