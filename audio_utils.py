import base64
from openai import OpenAI

client = OpenAI()

# Prompts for different scene types
CAT_SCENE_PROMPT = (
    "Transform a given phrase or sentence to mimic the sounds a cat might make. "
    "Consider using phonetic expressions commonly associated with cats, such as purring, meowing, or hissing, "
    "depending on the intended emotion or context.\n\n"
    "# Steps\n\n"
    "1. Analyze the given phrase to determine the intended emotion or context.\n"
    "2. Select cat sounds that align with the emotion or context, such as:\n"
    "   - Meowing for attention\n"
    "   - Purring for contentment\n"
    "   - Hissing for displeasure\n"
    "3. Transform the phrase using appropriate cat sounds while maintaining the original emotion or intent.\n\n"
    "# Output Format\n\n"
    "A short phonetic or onomatopoeic representation of cat sounds.\n\n"
    "# Examples\n\n"
    "- Input: \"I'm hungry.\"\n  Output: \"Meow? Meooow!\"\n\n"
    "- Input: \"Leave me alone.\"\n  Output: \"Hiss... Pfft!\"\n\n"
    "- Input: \"I'm happy!\"\n  Output: \"Purrrrr... Meow!\""
)

NARRATOR_SCENE_PROMPT = (
    "You are a helpful assistant that can generate audio from text. Speak in the accent of a Washington, DC native "
    "and enunciate like you're talking to a child."
)

def generate_audio(tts_text: str, speech_file_path: str, system_prompt: str, voice: str = "shimmer", model: str = "gpt-4o-audio-preview") -> None:
    completion = client.chat.completions.create(
        model=model,
        modalities=["text", "audio"],
        audio={"voice": voice, "format": "mp3"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": tts_text},
        ],
    )
    mp3_bytes = base64.b64decode(completion.choices[0].message.audio.data)
    with open(speech_file_path, "wb") as f:
        f.write(mp3_bytes)
    print(f"Audio saved to {speech_file_path}")