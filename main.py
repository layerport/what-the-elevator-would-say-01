#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes the funniest thing a talking elevator would say, in the
elevator's own voice, to <OUTPUT_DIR>/entry.txt (default /output).

Python 3.13, standard library only, fully deterministic: the same
single line is written on every run, with no network and no input.
"""

import os

# The elevator has heard every passenger lie to the button panel.
# It knows where they are really going — and it plays along.
ENTRY = "I know what floor you're really going to. I just pretend to believe the button."


def main() -> None:
    """Write the entry line to <OUTPUT_DIR>/entry.txt."""
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # One line only, no trailing newline: the file holds exactly the
    # entry text, so its character count is the line's character count.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
