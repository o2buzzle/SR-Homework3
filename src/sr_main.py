import time
import speech_to_text
from text_to_speech import tts
import core_interactions
import speech_recognition as sr
import preprocess

r = sr.Recognizer()
m = sr.Microphone()

r.recognize_google


def perform_callback(r, audio):
    try:
        text = r.recognize_google(audio, language="en-US")
        prep_text = preprocess.preprocess(text[0])
        result = core_interactions.interpreter(prep_text)
        print(result)
        tts.speak(result)
    except Exception as e:
        print(e)
        print("...")


while True:
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(m)
        perform_callback(r, audio)
        time.sleep(1)
