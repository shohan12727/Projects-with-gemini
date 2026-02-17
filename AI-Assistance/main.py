import time
import os
import speech_recognition as sr
import requests
# import pyttsx3
from dotenv import load_dotenv
from google import genai
import re
from gtts import gTTS



load_dotenv()


# Create the client once
chat_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Create a chat session for ongoing conversation
chat_session = chat_client.chats.create(model="gemini-2.5-flash")

# ---------------- INIT ----------------
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

# tts_engine = pyttsx3.init()

# ---------------- AUDIO ----------------
def get_audio():
    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Please speak now...")
        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=8
        )
    return audio

# ---------------- SPEECH → TEXT ----------------
def audio_to_text(audio):
    try:
        return recognizer.recognize_google(audio, language="en-US")
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"[Speech  error] {e}")
        return None

# ---------------- LLM QUERY ----------------
def query_gemini(text):
    if not text:
        return "I could not understand that."

    try:
        # Send text to the existing chat
        response = chat_session.send_message(text)
        return response.text

    except Exception as e:
        print("[Gemini Chat error]", e)
        return "The AI service is currently unavailable."



# ---------------- TEXT → SPEECH ----------------
def text_to_speech(text):
    try:
        gTTS(text)
        # tts.save('hello.mp3')
        # # Remove markdown formatting
        # clean_text = text.replace('**', '')
        # clean_text = clean_text.replace('*', '')
        # clean_text = clean_text.replace('#', '')
        # clean_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean_text)
        
        # # Reinitialize engine each time
        # engine = pyttsx3.init()
        # engine.say(clean_text)
        # engine.runAndWait()
        # engine.stop()  # Clean up
    except Exception as e:
        print(f"Error in text to speech: {e}")

# ---------------- MAIN LOOP ----------------
if __name__ == "__main__":
    print("Voice assistant started. Press Ctrl+C to exit.")

    while True:
        try:
            audio = get_audio()
            text = audio_to_text(audio)

            if not text:
                print("Speech not understood.")
                continue

            print("You said:", text)

            response = query_gemini(text)
            print("AI says:", response)

            text_to_speech(response)
            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\nShutting down...")
            break
