#!/usr/bin/env python3
"""Read-only structural metrics; no edits and no model-token claims."""
import argparse
import hashlib
import json
from pathlib import Path
import re


def measure(path):
    raw = Path(path).read_bytes()
    text = raw.decode("utf-8")
    fence = None
    list_items = 0
    sections = []
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, tail = marker.groups()
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1] and not tail.strip():
                fence = None
            continue
        if fence is not None:
            continue
        if re.match(r"^(?:[-+*]|[0-9]+[.)]) +", line):
            list_items += 1
        heading = re.match(r"^(#{1,6}) +(.+)$", line)
        if heading:
            sections.append(heading.group(2))
    return {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw), "lines": len(text.splitlines()),
            "whitespace_words": len(text.split()), "top_level_list_items": list_items,
            "sections": sections}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()
    try:
        result = {"current": measure(args.file)}
        if args.baseline is not None:
            before = measure(args.baseline)
            result["baseline"] = before
            result["byte_change"] = result["current"]["bytes"] - before["bytes"]
            result["byte_reduction_percent"] = (
                round((1 - result["current"]["bytes"] / before["bytes"]) * 100, 2)
                if before["bytes"] else None)
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
