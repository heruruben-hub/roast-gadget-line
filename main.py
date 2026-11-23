"""Roast the fridge's ice maker: nightly drama, three cubes of payoff."""

import os

PART_ONE = "My fridge's ice maker sounds like it's choking every night at 2 a.m.,"
PART_TWO = "then spits out three cubes like it's proud of itself."


def main() -> None:
    line = PART_ONE + " " + PART_TWO
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    encoded = line.encode("utf-8")
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
