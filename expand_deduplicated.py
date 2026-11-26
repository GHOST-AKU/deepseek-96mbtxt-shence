#!/usr/bin/env python3
"""Restore the line-reference edition of the Shen Ce text file."""

from pathlib import Path
import re
import sys


REF = re.compile(r"^[ \t\u3000]*〔重复行#(\d{6,})〕$")


def split_line_ending(line: bytes) -> tuple[bytes, bytes]:
    if line.endswith(b"\r\n"):
        return line[:-2], b"\r\n"
    if line.endswith(b"\n") or line.endswith(b"\r"):
        return line[:-1], line[-1:]
    return line, b""


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(
            "Usage: python expand_deduplicated.py INPUT.txt [OUTPUT.txt]",
            file=sys.stderr,
        )
        return 2

    source = Path(sys.argv[1])
    if len(sys.argv) == 3:
        destination = Path(sys.argv[2])
    else:
        destination = source.with_name(source.stem.replace("_引用去重版", "_还原版") + ".txt")

    raw = source.read_bytes()
    bom = b"\xef\xbb\xbf" if raw.startswith(b"\xef\xbb\xbf") else b""
    lines = raw[len(bom):].splitlines(keepends=True)
    expanded: list[bytes] = []

    for line_number, line in enumerate(lines, start=1):
        content, ending = split_line_ending(line)
        match = REF.fullmatch(content.decode("utf-8"))
        if not match:
            expanded.append(line)
            continue

        target_line = int(match.group(1))
        if target_line < 1 or target_line >= line_number:
            raise ValueError(
                f"Invalid backward reference on line {line_number}: {target_line}"
            )

        target_content, _ = split_line_ending(expanded[target_line - 1])
        expanded.append(target_content + ending)

    restored = bom + b"".join(expanded)
    destination.write_bytes(restored)
    print(f"Restored {len(lines):,} lines to {destination} ({len(restored):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
