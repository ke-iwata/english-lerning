#!/usr/bin/env python3
"""Build the files to upload to a Claude Project (for voice-mode lessons in the Claude app).

Output (dist/claude-project/):
  00-project-instructions.md   paste into the Project's "instructions" field
  01-curriculum.md             lesson list (ids, titles, can-do) for Claude to pick lessons
  level1-foundation.md ...     lessons grouped by level (upload as project knowledge)
  lessons-all.md               every lesson in one file (alternative to the level files)
  progress-pack.md             learner profile + recent session records (re-upload after each lesson)

Run: python3 scripts/build_pack.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS = ROOT / "lessons"
PROGRESS = ROOT / "progress"
OUT = ROOT / "dist" / "claude-project"
RECENT_SESSIONS = 5

LEVEL_SLUG = {1: "level1-foundation", 2: "level2-everyday-work", 3: "level3-meetings", 4: "level4-practice"}


def strip_front_matter(text: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    index = json.loads((LESSONS / "index.json").read_text(encoding="utf-8"))

    # 00: project instructions (voice-mode tutor prompt)
    instr = (ROOT / "prompts" / "voice-tutor-instructions.md").read_text(encoding="utf-8")
    sep = instr.find("\n---\n")
    body = instr[sep + 5:] if sep >= 0 else instr
    (OUT / "00-project-instructions.md").write_text(body.strip() + "\n", encoding="utf-8")

    # 01: curriculum
    lines = ["# Curriculum — Business English 30 (24 lessons × 30 min)", ""]
    for lv in index["levels"]:
        lines.append(f"## Level {lv['level']}: {lv['name']} / {lv['name_en']} ({lv['cefr']})")
        lines.append(lv["description"])
        lines.append("")
        for l in index["lessons"]:
            if l["level"] == lv["level"]:
                lines.append(f"- Lesson {l['id']}: {l['title']} / {l['title_en']} — Can-do: {l['can_do']} — 相手役: {l['partner']}")
        lines.append("")
    (OUT / "01-curriculum.md").write_text("\n".join(lines), encoding="utf-8")

    # level files + all-in-one
    all_parts = []
    for lv in index["levels"]:
        parts = [f"# Level {lv['level']}: {lv['name']} / {lv['name_en']}", ""]
        for l in index["lessons"]:
            if l["level"] == lv["level"]:
                md = strip_front_matter((LESSONS / l["file"]).read_text(encoding="utf-8")).strip()
                parts.append(md)
                parts.append("\n\n---\n")
        text = "\n".join(parts)
        (OUT / f"{LEVEL_SLUG[lv['level']]}.md").write_text(text, encoding="utf-8")
        all_parts.append(text)
    (OUT / "lessons-all.md").write_text("\n\n".join(all_parts), encoding="utf-8")

    # progress pack
    prof = (PROGRESS / "profile.md").read_text(encoding="utf-8")
    sessions = sorted(p for p in (PROGRESS / "sessions").glob("*.md") if p.name != "TEMPLATE.md")
    recent = sessions[-RECENT_SESSIONS:]
    pack = ["# Progress pack(学習者プロファイルと最近のレッスン記録)", "",
            "Claude(講師)はレッスンの前にこれを読み、前回の宿題・弱点・本人の状況を踏まえて進めてください。", "",
            prof.strip(), "", "---", "", f"# 最近のレッスン記録(直近 {len(recent)} 回)", ""]
    if not recent:
        pack.append("(まだ記録はありません。初回のレッスンです。)")
    for p in recent:
        pack.append(p.read_text(encoding="utf-8").strip())
        pack.append("\n---\n")
    (OUT / "progress-pack.md").write_text("\n".join(pack), encoding="utf-8")

    for p in sorted(OUT.iterdir()):
        print(f"{p.relative_to(ROOT)}  ({p.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
