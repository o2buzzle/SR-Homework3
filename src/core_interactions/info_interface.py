import asyncio
import time
import python_weather
from text_to_speech import tts

weather_client = python_weather.Client(format=python_weather.METRIC)


def _get_time():
    time_text = time.strftime("%H:%M:%S", time.localtime())
    tts.speak('It\'s {}'.format(time_text))
    return time_text


def _get_date():
    date_text = time.strftime("%d/%m/%Y", time.localtime())
    tts.speak("Today is {}".format(date_text))
    return date_text


def _get_weather(location):
    loop = asyncio.get_event_loop()
    weather = loop.run_until_complete(weather_client.find(location))
    curr_weather = weather.current
    content = "Right now it\'s {} and {} Celcius in {}. " \
              "The wind speed is {} km/h. " \
              "The humidity is {}%.".format(curr_weather.sky_text, curr_weather.temperature, location, curr_weather.wind_speed, curr_weather.humidity)
    tts.speak(content)
    return f"{curr_weather.temperature}°C, {curr_weather.sky_text}, {curr_weather.wind_speed}km/h, Humidity: {curr_weather.humidity}%"


def interp(q):
    if q.startswith("time"):
        return _get_time()
    elif q.startswith("date"):
        return _get_date()
    elif q.startswith("weather"):
        return _get_weather(q[8:])
    else:
        raise Exception("Unknown command")
