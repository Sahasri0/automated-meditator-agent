import os
from datetime import date
from .config import SCRIPTS_DIR, AUDIO_DIR, TARGET_MIN_WORDS, TARGET_MAX_WORDS
from .context_loader import load_context
from .meditation_chain import generate_script
from .tts import generate_audio
from .gmail import send_meditation

def validate_script(script: str):
    words = len(script.split())
    if not TARGET_MIN_WORDS <= words <= TARGET_MAX_WORDS:
        raise ValueError(
            f"Script word count {words} is outside "
            f"{TARGET_MIN_WORDS}-{TARGET_MAX_WORDS}."
        )
    return words

def main():
    today = date.today().isoformat()
    context = load_context()
    script = generate_script(context)
    words = validate_script(script)

    script_path = SCRIPTS_DIR / f"{today}.md"
    script_path.write_text(script + "\n", encoding="utf-8")

    audio_path = AUDIO_DIR / f"meditation-{today}.wav"
    generate_audio(script, audio_path)

    recipient = os.environ["MEDITATION_EMAIL"]
    send_meditation(
        audio_path,
        f"Your meditation for {today}",
        f"Your personalized meditation is ready. Script length: {words} words.",
        recipient,
    )
    print(f"Completed meditation for {today}: {words} words")

if __name__ == "__main__":
    main()
