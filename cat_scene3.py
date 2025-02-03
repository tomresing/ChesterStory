from audio_utils import generate_audio, CAT_SCENE_PROMPT

tts_text = """
Meeee-yawn
"""

speech_file_path = "./sounds/cat_scene3.mp3"
generate_audio(tts_text, speech_file_path, CAT_SCENE_PROMPT)