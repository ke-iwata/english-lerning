#!/usr/bin/env bash
# Claude Code "Stop" hook: read the tutor's last reply aloud when voice mode is on.
# Registered in .claude/settings.json. Receives the hook JSON on stdin (uses transcript_path).
# Does nothing unless .claude/.voice-on exists (scripts/voice.sh on).
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FLAG="$ROOT/.claude/.voice-on"
[ -f "$FLAG" ] || exit 0
command -v python3 >/dev/null 2>&1 || exit 0

INPUT="$(cat)"
TEXT="$(HOOK_INPUT="$INPUT" python3 - <<'PY'
import json, os, sys
try:
    data = json.loads(os.environ.get("HOOK_INPUT") or "{}")
except Exception:
    sys.exit(0)
if data.get("stop_hook_active"):
    sys.exit(0)  # a Stop hook already continued this turn; never loop
# Claude Code passes the final reply directly (official field); transcript parsing is a fallback.
msg = data.get("last_assistant_message")
if not msg:
    path = data.get("transcript_path")
    if not path:
        sys.exit(0)
    last = None
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                except Exception:
                    continue
                if ev.get("type") != "assistant":
                    continue
                content = (ev.get("message") or {}).get("content") or []
                texts = [c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"]
                if texts:
                    last = "\n".join(texts)
    except Exception:
        sys.exit(0)
    msg = last
if msg:
    sys.stdout.write(msg)
PY
)"
[ -n "$TEXT" ] || exit 0

# Speak in the background so the prompt comes back immediately (scripts/voice.sh stop interrupts).
printf '%s' "$TEXT" | nohup python3 "$ROOT/scripts/speak.py" --clean-markdown >/dev/null 2>&1 &
exit 0
