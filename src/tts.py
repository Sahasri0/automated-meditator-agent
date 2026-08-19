from pathlib import Path
from google import genai
from google.genai import types
from .config import GEMINI_TTS_MODEL, TTS_VOICE

def generate_audio(script: str, output_path: Path) -> Path:
    client = genai.Client()
    response = client.models.generate_content(
        model=GEMINI_TTS_MODEL,
        contents=(
            "Speak this meditation slowly, warmly, calmly, and reassuringly. "
            "Use natural pauses and a gentle morning meditation pace. "
            "Do not sound sleepy. Transcript:\n\n" + script
        ),
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=TTS_VOICE
                    )
                )
            ),
        ),
    )

    audio = response.candidates[0].content.parts[0].inline_data.data
    output_path.write_bytes(audio)
    return output_path
