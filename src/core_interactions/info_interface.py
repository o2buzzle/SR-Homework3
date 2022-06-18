import asyncio
import time
import python_weather
from text_to_speech import tts

weather_client = python_weather.Client(format=python_weather.METRIC)


def _get_time():
    time_text = time.strftime("%H:%M:%S", time.localtime())
    return time_text

def _get_date():
    date_text = time.strftime("%d/%m/%Y", time.localtime())
    return date_text

def _get_weather(location):
    loop = asyncio.get_event_loop()
    weather = loop.run_until_complete(weather_client.find(location))
    curr_weather = weather.current
    return curr_weather

def interp(q):
    if q.startswith("time"):
        time = _get_time()
        tts.speak('It\'s {}'.format(time))
        return _get_time()
    elif q.startswith("date"):
        date = _get_date()
        tts.speak("Today is {}".format(date))
        return _get_date()
    elif q.startswith("weather"):
        location = q[8:]
        curr_weather = _get_weather(location)
        tts.speak_weather(curr_weather, location)
        return f"{curr_weather.temperature}°C, {curr_weather.sky_text}, {curr_weather.wind_speed}km/h, Humidity: {curr_weather.humidity}%"
    else:
        raise Exception("Unknown command")
