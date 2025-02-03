import base64
from openai import OpenAI
client = OpenAI()

tts_text = """
His world is simple—sunbeams, cozy nooks, and just the right amount of mischief to keep life interesting. But he can’t rest too long; the day still holds promise.
"""

speech_file_path = "./sounds/narrator_scene3b.mp3"
completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "shimmer", "format": "mp3"},
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that can generate audio from text. Speak in the accent of a Washington, DC native and enunciate like you're talking to a child.",
        },
        {
            "role": "user",
            "content": tts_text,
        }
    ],
)

mp3_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open(speech_file_path, "wb") as f:
    f.write(mp3_bytes)
print(f"Audio saved to {speech_file_path}")