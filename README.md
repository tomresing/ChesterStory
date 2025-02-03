# ChesterStory

ChesterStory generates audio narrations and cat sound transformations using OpenAI's API. This project includes narrator scenes and cat scenes with dedicated scripts for each.

## Files overview

### Narrator scenes
- **narrator_scene1.py:** Generates the early morning narration for Chester.
- **narrator_scene2a.py:** Describes Chester in the bedroom with a game controller.
- **narrator_scene2b.py:** Continues the narration with Chester guarding the game session.
- **narrator_scene4.py:** Contains multiple narration texts for later scenes.  
  *Tip: Add your new scenes by appending text to `tts_texts` and file paths to `speech_file_paths`.*

### Cat scenes
- **cat_scene1.py:** Transforms text into feline sounds reflecting a sleepy mood.
- **cat_scene2.py:** Converts a phrase into a playful cat sound demonstration.
- **cat_scene3.py:** Generates a simple cat sound (e.g., a meow).
- **cat_scene4.py:** Produces cat sounds with a slightly inquisitive tone.

### Utility
- **audio_utils.py:** Provides a helper function `generate_audio` and defines system prompts for narrator and cat scenes.

### Legal
- **LICENSE:** Contains the Apache License 2.0.

## Environment setup

Before running any scripts, set your OpenAI API key as an environment variable and ensure you're using Python 3.7 or later:

- On Unix/Linux/Mac:
  ```sh
  export OPENAI_API_KEY=<your_api_key>
  ```
- On Windows:
  ```cmd
  set OPENAI_API_KEY=<your_api_key>
  ```

## Running the scripts

Each script generates an MP3 audio file in the `./sounds` folder. To run a script, use Python. For example:
```sh
python narrator_scene1.py
```
Repeat for any of the other scripts:
```sh
python narrator_scene2a.py
python narrator_scene2b.py
python narrator_scene4.py
python cat_scene1.py
python cat_scene2.py
python cat_scene3.py
python cat_scene4.py
```

## Add or modify scenes by updating **narrator_scene4.py** 

Modify the scenes by updating `tts_texts`

Add new scenes by appending  text to `tts_texts` and file paths to `speech_file_paths`

## Add scenes by adding a file

To add a scene or multiple scenes, create a new Python file (or update an existing one) and use the helper function from audio_utils. This ensures a consistent way to generate audio. Follow these steps:

1. Import generate_audio and the appropriate prompt (NARRATOR_SCENE_PROMPT or CAT_SCENE_PROMPT) from audio_utils.
2. Write your scene text(s) and specify corresponding output file paths.
3. Call generate_audio for each scene, either directly or within a loop if adding multiple scenes.
4. Run your new script to generate the audio file(s).

### Example: Single scene file

```python
# filepath: ./narrator_newscene.py
from audio_utils import generate_audio, NARRATOR_SCENE_PROMPT

tts_text = "Your new narrator scene text here."
speech_file_path = "./sounds/narrator_newscene.mp3"

generate_audio(tts_text, speech_file_path, NARRATOR_SCENE_PROMPT)
```

### Example: Multiple scenes in one file

```python
# filepath: ./narrator_sceneX.py
from audio_utils import generate_audio, NARRATOR_SCENE_PROMPT

tts_texts = [
    "Scene text 1",
    "Scene text 2",
    # ...existing code...
]

speech_file_paths = [
    "./sounds/scene1.mp3",
    "./sounds/scene2.mp3",
    # ...existing code...
]

for tts_text, speech_file_path in zip(tts_texts, speech_file_paths):
    generate_audio(tts_text, speech_file_path, NARRATOR_SCENE_PROMPT)
```

A similar approach applies for cat scenes using CAT_SCENE_PROMPT.

## Dependencies

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- Python standard libraries (`base64`)

Recommended Python version: 3.7+

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](./LICENSE) file for details.