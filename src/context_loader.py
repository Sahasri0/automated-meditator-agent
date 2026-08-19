from .config import CONTEXT_DIR

def load_context() -> dict[str, str]:
    return {
        "dream_life": (CONTEXT_DIR / "dream-life.md").read_text(encoding="utf-8"),
        "yearly_goals": (CONTEXT_DIR / "yearly-goals.md").read_text(encoding="utf-8"),
        "voice_tone": (CONTEXT_DIR / "voice-tone.md").read_text(encoding="utf-8"),
    }
