import playsound
import os
from gtts import gTTS


def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("sound.mp3")
    try:
        playsound.playsound("sound.mp3")
    except:
        # Speech may not be fully supported on your platform.
        pass
    os.remove("sound.mp3")
