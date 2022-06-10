import asyncio
import time
import python_weather

weather_client = python_weather.Client(format=python_weather.METRIC)


def _get_time():
    return time.strftime("%H:%M:%S", time.localtime())


def _get_date():
    return time.strftime("%d/%m/%Y", time.localtime())


def _get_weather(location):
    loop = asyncio.get_event_loop()
    weather = loop.run_until_complete(weather_client.find(location))
    curr_weather = weather.current

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
