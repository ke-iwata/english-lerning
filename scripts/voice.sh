#!/usr/bin/env bash
# Voice mode for lessons: the Stop hook reads the tutor's reply aloud while this is ON.
#
#   scripts/voice.sh on      # enable read-aloud (creates .claude/.voice-on)
#   scripts/voice.sh off     # disable
#   scripts/voice.sh status  # on / off
#   scripts/voice.sh stop    # stop the voice that is speaking right now
#   scripts/voice.sh test    # speak a sample sentence in English and Japanese
#   scripts/voice.sh say "text"   # speak arbitrary text now
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FLAG="$ROOT/.claude/.voice-on"
SPEAK="$ROOT/scripts/speak.py"

stop_speaking() {
  pkill -f "/usr/bin/say|[s]peak.py" 2>/dev/null
  pkill -x say 2>/dev/null
  return 0
}

case "${1:-status}" in
  on)
    mkdir -p "$ROOT/.claude" && touch "$FLAG" && echo "voice: on (講師の返答を読み上げます。止めるには scripts/voice.sh off)" ;;
  off)
    rm -f "$FLAG" && stop_speaking && echo "voice: off" ;;
  status)
    if [ -f "$FLAG" ]; then echo "voice: on"; else echo "voice: off"; fi ;;
  stop)
    stop_speaking && echo "voice: stopped" ;;
  test)
    python3 "$SPEAK" "Hi Ken, nice to meet you. 今日は自己紹介の練習をしましょう。" ;;
  say)
    shift; python3 "$SPEAK" "$@" ;;
  *)
    echo "usage: scripts/voice.sh on|off|status|stop|test|say <text>" >&2; exit 2 ;;
esac
