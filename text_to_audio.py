import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_file(text: str, folder: str) -> str:
    print("TTS ->", folder)

    
    save_dir = os.path.join("user_uploads", folder)
    os.makedirs(save_dir, exist_ok=True)

    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    save_file_path = os.path.join(save_dir, "audio.mp3")

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"✅ Audio saved: {save_file_path}")
    return save_file_path


