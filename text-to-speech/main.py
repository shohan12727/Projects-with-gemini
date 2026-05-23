import gradio as gr
from gtts import gTTS
import tempfile
import os

LANGUAGES = {
    "English": "en",
    "Bengali": "bn",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Japanese": "ja",
    "Chinese": "zh",
}

def text_to_speech(text: str, language: str, slow: bool) -> str:
    """Convert text to speech and return path to audio file."""
    if not text.strip():
        raise gr.Error("Please enter some text!")

    lang_code = LANGUAGES[language]
    tts = gTTS(text=text, lang=lang_code, slow=slow)

    # Save to a temp file
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    tmp.close()
    return tmp.name


with gr.Blocks(title="Text to Speech", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🔊 Text to Speech\nConvert any text to speech using Google TTS.")

    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Enter Text",
                placeholder="Type something here...",
                lines=5,
            )
            with gr.Row():
                lang_dropdown = gr.Dropdown(
                    choices=list(LANGUAGES.keys()),
                    value="English",
                    label="Language",
                )
                slow_checkbox = gr.Checkbox(label="Slow Speed", value=False)
            convert_btn = gr.Button("🎙️ Convert to Speech", variant="primary")

        with gr.Column(scale=1):
            audio_output = gr.Audio(label="Generated Audio", type="filepath")
            gr.Markdown("### Tips\n- Supports 9 languages\n- Toggle **Slow Speed** for clearer pronunciation\n- Click ▶ to play or download the audio")

    convert_btn.click(
        fn=text_to_speech,
        inputs=[text_input, lang_dropdown, slow_checkbox],
        outputs=audio_output,
    )

    gr.Examples(
        examples=[
            ["Hello! Welcome to the text to speech demo.", "English", False],
            ["আমি বাংলায় কথা বলতে পারি।", "Bengali", False],
            ["Bonjour, comment ça va?", "French", True],
        ],
        inputs=[text_input, lang_dropdown, slow_checkbox],
    )

if __name__ == "__main__":
    demo.launch()