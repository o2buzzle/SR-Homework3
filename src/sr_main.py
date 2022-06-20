import time
import datetime
import speech_to_text
from text_to_speech import tts
import core_interactions
import speech_recognition as sr
import preprocess
from text_to_speech.tts import speak
r = sr.Recognizer()
m = sr.Microphone()

r.recognize_google


def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = time.strftime("%H:%M:%S", time.localtime())
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

def perform_callback(r, audio):
    try:
        text = r.recognize_google(audio, language="en-US")
        prep_text = preprocess.preprocess(text[0])
        result = core_interactions.interpreter(prep_text)
        print(result)
        tts.speak(result)
        return result
    except Exception as e:
        print(e)
        print("...")


# while True:
#     with m as source:
#         r.adjust_for_ambient_noise(source)
#         print("Listening...")
#         audio = r.listen(m)
#         perform_callback(r, audio)
#         time.sleep(1)
