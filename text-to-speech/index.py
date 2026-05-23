import gradio as gr
from gtts import gTTS
import tempfile

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

def text_to_speech(text: str, language: str, slow: bool):
    if not text.strip():
        raise gr.Error("Please enter some text first.")
    lang_code = LANGUAGES[language]
    tts = gTTS(text=text, lang=lang_code, slow=slow)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    tmp.close()
    return tmp.name

theme = gr.themes.Default(
    primary_hue="slate",
    secondary_hue="gray",
    neutral_hue="gray",
    font=gr.themes.GoogleFont("Inter"),
).set(
    button_primary_background_fill="#1f2937",
    button_primary_background_fill_hover="#374151",
    button_primary_text_color="#ffffff",
    body_background_fill="#f9fafb",
    block_background_fill="#ffffff",
    block_border_color="#e5e7eb",
    block_border_width="1px",
    block_shadow="0 1px 3px rgba(0,0,0,0.06)",
    input_background_fill="#ffffff",
    input_border_color="#d1d5db",
    input_border_width="1px",
    checkbox_background_color_selected="#1f2937",
    checkbox_border_color_selected="#1f2937",
)

custom_css = """
    .gradio-container { max-width: 1000px !important; margin: 40px auto !important; }
    footer { display: none !important; }
"""

with gr.Blocks(title="Text to Speech") as demo:
    gr.HTML("<h2 style='font-size:1.4rem;font-weight:600;color:#111827;margin-bottom:4px'>🔊 Text to Speech</h2><p style='color:#6b7280;font-size:0.88rem;margin-bottom:20px'>Type text, pick a language, and hear it spoken aloud.</p>")

    with gr.Row(equal_height=True):
        # Left column — input
        with gr.Column(scale=3):
            text_input = gr.Textbox(
                label="Your text",
                placeholder="Type or paste text here...",
                lines=6,
                max_lines=10,
            )
            with gr.Row(equal_height=True):
                lang_dropdown = gr.Dropdown(
                    choices=list(LANGUAGES.keys()),
                    value="English",
                    label="Language",
                    scale=3,
                )
                slow_checkbox = gr.Checkbox(
                    label="Slow mode",
                    value=False,
                    scale=1,
                )
            convert_btn = gr.Button("Generate Speech ▶", variant="primary", size="lg")

        # Right column — output
        with gr.Column(scale=2):
            audio_output = gr.Audio(label="Output", type="filepath")
            gr.Examples(
                label="Try an example",
                examples=[
                    ["Hello! How are you doing today?", "English", False],
                    ["আমি বাংলায় কথা বলতে পারি।", "Bengali", False],
                    ["Bonjour, comment ça va?", "French", True],
                    ["こんにちは、元気ですか？", "Japanese", False],
                ],
                inputs=[text_input, lang_dropdown, slow_checkbox],
            )

    convert_btn.click(
        fn=text_to_speech,
        inputs=[text_input, lang_dropdown, slow_checkbox],
        outputs=audio_output,
    )

if __name__ == "__main__":
    demo.launch(theme=theme, css=custom_css)