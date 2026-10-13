#!/usr/bin/env python3
"""Validate that every lesson in lessons/index.json exists and follows the template.

Run: python3 scripts/check_lessons.py
Exit code 1 if any problem is found.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"

REQUIRED_HEADINGS = [
    "## 1. Warm-up (3 min)",
    "## 2. Vocabulary & Idioms (7 min)",
    "## 3. Key Expressions (7 min)",
    "## 4. Role-play (10 min)",
    "## 5. Wrap-up (3 min)",
]
REQUIRED_SUBHEADINGS = [
    "### Words",
    "### Idioms & Collocations",
    "### Quick check",
    "### Scenario",
    "### Roles",
    "### Model dialogue",
    "### Your turn",
    "### Self-check",
    "### Homework",
    "### Next lesson",
]


def main() -> int:
    problems = []
    index = json.loads((LESSONS / "index.json").read_text(encoding="utf-8"))
    ids = [l["id"] for l in index["lessons"]]
    if ids != sorted(ids) or len(set(ids)) != len(ids):
        problems.append("index.json: lesson ids must be unique and sorted")

    for lesson in index["lessons"]:
        path = LESSONS / lesson["file"]
        if not path.exists():
            problems.append(f"{lesson['file']}: missing")
            continue
        text = path.read_text(encoding="utf-8")

        fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not fm:
            problems.append(f"{lesson['file']}: missing front matter")
        else:
            m = re.search(r'^id:\s*"?(\d+)"?', fm.group(1), re.M)
            if not m or m.group(1) != lesson["id"]:
                problems.append(f"{lesson['file']}: front matter id does not match index.json ({lesson['id']})")

        if not re.search(rf"^# Lesson {lesson['id']}:", text, re.M):
            problems.append(f"{lesson['file']}: missing '# Lesson {lesson['id']}: ...' title")

        pos = -1
        for h in REQUIRED_HEADINGS:
            i = text.find("\n" + h + "\n")
            if i < 0:
                problems.append(f"{lesson['file']}: missing heading '{h}'")
            elif i < pos:
                problems.append(f"{lesson['file']}: heading out of order '{h}'")
            else:
                pos = i
        for h in REQUIRED_SUBHEADINGS:
            if ("\n" + h + "\n") not in text:
                problems.append(f"{lesson['file']}: missing subheading '{h}'")
        if "講師用メモ" not in text:
            problems.append(f"{lesson['file']}: missing tutor notes")

        for tag in ("details", "summary"):
            if text.count(f"<{tag}") != text.count(f"</{tag}>"):
                problems.append(f"{lesson['file']}: unbalanced <{tag}> tags")

    # orphan lesson files
    known = {l["file"] for l in index["lessons"]}
    for p in sorted(LESSONS.glob("[0-9][0-9]-*.md")):
        if p.name not in known:
            problems.append(f"{p.name}: not listed in index.json")

    if problems:
        print("Lesson check FAILED:")
        for p in problems:
            print("  -", p)
        return 1
    print(f"OK: {len(index['lessons'])} lessons validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
