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


def speak_weather(curr_weather, location):
    content = (
        "Right now it's {} and {} Celcius in {}. "
        "The wind speed is {} km/h. "
        "The humidity is {}%.".format(
            curr_weather.sky_text,
            curr_weather.temperature,
            location,
            curr_weather.wind_speed,
            curr_weather.humidity,
        )
    )
    speak(content)
    return 0
