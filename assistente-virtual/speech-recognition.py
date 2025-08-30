import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound
import pyjokes
import pyaudio
import webbrowser

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(f"You said: {said}")
        except Exception as e:
            print("Exception: " + str(e))

    return said

def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

while True:
    text = get_audio().lower()

    if "youtube" in text:
        speak("Opening YouTube.")
        url = f"https://www.youtube.com"
        webbrowser.get().open(url)