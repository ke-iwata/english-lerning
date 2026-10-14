#!/usr/bin/env python3
"""Read text aloud, switching voices between English and Japanese.

Usage:
  scripts/speak.py "Hello. こんにちは。"        # speak the argument
  echo "text" | scripts/speak.py              # speak stdin
  scripts/speak.py --clean-markdown < msg.md  # strip markdown first (used by the Stop hook)

Backends (auto-detected):
  macOS   : `say`   (English voice: $VOICE_EN, default Samantha / Japanese: $VOICE_JA, default Kyoko)
  Windows : PowerShell System.Speech (picks an en-US / ja-JP voice if installed)
  Linux   : `spd-say` or `espeak-ng`

Env:
  VOICE_EN, VOICE_JA   voice names (macOS: `say -v ?` lists them)
  VOICE_RATE           words per minute (default 165; try 140 for slower English)
  VOICE_DRY_RUN=1      print the segments instead of speaking (for tests)
"""
import os
import platform
import re
import shutil
import subprocess
import sys

JA_RE = re.compile(r"[　-〿぀-ゟ゠-ヿ一-鿿＀-￯]")
RATE = os.environ.get("VOICE_RATE", "165")
VOICE_EN = os.environ.get("VOICE_EN", "Samantha")
VOICE_JA = os.environ.get("VOICE_JA", "Kyoko")


def clean_markdown(text: str) -> str:
    """Turn a chat message into something that sounds OK when read aloud."""
    out = []
    in_code = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if not s:
            out.append("")
            continue
        if s.startswith("|"):           # tables: read cells as a sentence
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            s = "、".join(c for c in cells if c) if JA_RE.search(s) else ", ".join(c for c in cells if c)
        s = re.sub(r"^-{3,}\s*(.*?)\s*-{3,}$", r"\1", s)   # --- section --- → section
        if re.fullmatch(r"[-*_]{3,}", s):
            continue
        s = re.sub(r"^#{1,6}\s*", "", s)
        s = re.sub(r"^>\s*", "", s)
        s = re.sub(r"^[-*+]\s+\[[ xX]\]\s*", "", s)   # task list
        s = re.sub(r"^[-*+]\s+", "", s)               # bullets
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
        s = re.sub(r"__(.+?)__", r"\1", s)
        s = re.sub(r"(?<!\w)[*_](.+?)[*_](?!\w)", r"\1", s)
        s = re.sub(r"`([^`]*)`", r"\1", s)
        s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"https?://\S+", "", s)
        s = s.replace("✗", "incorrect: ").replace("✓", "correct: ").replace("→", ", ")
        s = re.sub(r"[#*_~>|]", "", s)
        s = re.sub(r"\s+", " ", s).strip()
        if s:
            out.append(s)
    return "\n".join(out)


def segments(text: str):
    """Split text into (lang, chunk) runs so each gets the right voice."""
    cur_lang, buf = None, []
    for ch in text:
        if ch.isspace() or ch in ",.!?;:'\"()-/0123456789":
            buf.append(ch)
            continue
        lang = "ja" if JA_RE.match(ch) else "en"
        if cur_lang is None:
            cur_lang = lang
        if lang != cur_lang:
            chunk = "".join(buf).strip()
            if chunk:
                yield cur_lang, chunk
            buf, cur_lang = [], lang
        buf.append(ch)
    chunk = "".join(buf).strip()
    if chunk:
        yield cur_lang or "en", chunk


def speak_macos(lang: str, chunk: str):
    voice = VOICE_JA if lang == "ja" else VOICE_EN
    subprocess.run(["say", "-v", voice, "-r", RATE, chunk], check=False)


def speak_windows(lang: str, chunk: str):
    culture = "ja-JP" if lang == "ja" else "en-US"
    ps = (
        "Add-Type -AssemblyName System.Speech;"
        "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer;"
        f"$v = $s.GetInstalledVoices() | Where-Object {{ $_.VoiceInfo.Culture.Name -eq '{culture}' }} | Select-Object -First 1;"
        "if ($v) { $s.SelectVoice($v.VoiceInfo.Name) };"
        f"$s.Rate = [int](({RATE} - 165) / 20);"
        "$s.Speak([Console]::In.ReadToEnd())"
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], input=chunk, text=True, check=False)


def speak_linux(lang: str, chunk: str):
    if shutil.which("spd-say"):
        subprocess.run(["spd-say", "-w", "-l", "ja" if lang == "ja" else "en", "-r", "0", chunk], check=False)
    elif shutil.which("espeak-ng"):
        subprocess.run(["espeak-ng", "-v", "ja" if lang == "ja" else "en-us", "-s", RATE, chunk], check=False)
    elif shutil.which("espeak"):
        subprocess.run(["espeak", "-v", "ja" if lang == "ja" else "en-us", "-s", RATE, chunk], check=False)
    else:
        sys.stderr.write("speak.py: no TTS backend found (install espeak-ng or speech-dispatcher)\n")


def backend():
    sysname = platform.system()
    if sysname == "Darwin" and shutil.which("say"):
        return speak_macos
    if sysname == "Windows" or shutil.which("powershell.exe"):
        return speak_windows
    return speak_linux


def main() -> int:
    args = sys.argv[1:]
    clean = "--clean-markdown" in args
    args = [a for a in args if a != "--clean-markdown"]
    text = " ".join(args) if args else sys.stdin.read()
    if clean:
        text = clean_markdown(text)
    text = text.strip()
    if not text:
        return 0
    speak = backend()
    for lang, chunk in segments(text):
        if os.environ.get("VOICE_DRY_RUN"):
            print(f"[{lang}] {chunk}")
        else:
            speak(lang, chunk)
    return 0


if __name__ == "__main__":
    sys.exit(main())
