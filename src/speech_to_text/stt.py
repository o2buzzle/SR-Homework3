from text_to_speech import tts
import speech_recognition as sr
import time


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: ", end="")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="en-US")
            print(text)
            return text
        except:
            print("...")
            return 0


def get_text():
    print("Please speak something")
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            tts.speak("I can't hear you, please try again")
    time.sleep(2)
    return ""
