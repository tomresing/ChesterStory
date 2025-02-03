import base64
from openai import OpenAI
client = OpenAI()

tts_text = """
what's this toy?
"""

speech_file_path = "./sounds/cat_scene2.mp3"
completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "shimmer", "format": "mp3"},
    messages=[
        {
            "role": "system",
            "content": "Transform a given phrase or sentence to mimic the sounds a cat might make. Consider using phonetic expressions commonly associated with cats, such as purring, meowing, or hissing, depending on the desired emotional tone or context.\n\n# Steps\n\n1. Analyze the given phrase to determine the intended emotion or context.\n2. Select cat sounds that align with the emotion or context, such as:\n   - Meowing for attention\n   - Purring for contentment\n   - Hissing for displeasure\n3. Transform the phrase using appropriate cat sounds while maintaining the original emotion or intent.\n\n# Output Format\n\nA short phonetic or onomatopoeic representation of cat sounds.\n\n# Examples\n\n- Input: \"I'm hungry.\"\n  Output: \"Meow? Meooow!\"\n\n- Input: \"Leave me alone.\"\n  Output: \"Hiss... Pfft!\"\n\n- Input: \"I'm happy!\"\n  Output: \"Purrrrr... Meow!\"",
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