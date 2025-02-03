import base64
from openai import OpenAI
client = OpenAI()

tts_text = """
Though he can’t press all the buttons at once, Chester believes he can conquer the virtual realm if only someone hands him the thumbsticks. For now, he’ll settle for being the guardian of the game session.
"""

speech_file_path = "./sounds/narrator_scene2b.mp3"
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