import playsound
import os
from gtts import gTTS

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")