from audio_utils import generate_audio, CAT_SCENE_PROMPT

tts_text = """
Meow? (Head tilts, inviting a scratch behind the ears)
"""

speech_file_path = "./sounds/cat_scene4.mp3"
generate_audio(tts_text, speech_file_path, CAT_SCENE_PROMPT)