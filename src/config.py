from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
CONTEXT_DIR = ROOT / "context"
SCRIPTS_DIR = ROOT / "scripts"
AUDIO_DIR = ROOT / "audio"

GEMINI_TEXT_MODEL = os.getenv("GEMINI_TEXT_MODEL", "gemini-2.5-flash")
GEMINI_TTS_MODEL = os.getenv("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")
TTS_VOICE = os.getenv("GEMINI_TTS_VOICE", "Kore")
TARGET_MIN_WORDS = int(os.getenv("TARGET_MIN_WORDS", "1200"))
TARGET_MAX_WORDS = int(os.getenv("TARGET_MAX_WORDS", "1400"))

for directory in (SCRIPTS_DIR, AUDIO_DIR):
    directory.mkdir(parents=True, exist_ok=True)
