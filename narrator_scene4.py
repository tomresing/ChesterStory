from audio_utils import generate_audio, NARRATOR_SCENE_PROMPT

tts_texts = [
    "Later, Chester claims the ottoman for his reading nook. He finds a book already open—perfect to lounge on.",
    "He doesn’t need words to immerse himself in the story; the open book is the perfect makeshift pillow. After all, it’s the best place to pause and invite anyone around for some gentle company.",
    "As twilight settles, Chester closes his eyes, dreaming of polka-dot beds, gaming adventures, and the wonderful stories he’s napped upon. No matter the scene, Chester’s day is a peaceful tapestry of cozy spots, soft stretches, and contented purrs."
]

speech_file_paths = [
    "./sounds/narrator_scene4a.mp3",
    "./sounds/narrator_scene4b.mp3",
    "./sounds/narrator_scene5.mp3"
]

for tts_text, speech_file_path in zip(tts_texts, speech_file_paths):
    generate_audio(tts_text, speech_file_path, NARRATOR_SCENE_PROMPT)