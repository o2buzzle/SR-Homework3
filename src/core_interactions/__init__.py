from . import system_interface, browser_interface, media_interface, info_interface
from speech_to_text import stt


def interpreter(command: str):
    intent, command = command.split(" ", 1)
    if intent == "system":
        return system_interface.interp(command)
    elif intent == "browser":
        return browser_interface.interp(command)
    elif intent == "media":
        return media_interface.interp(command)
    elif intent == "info":
        if("time" in command):
            time = info_interface.interp(command)
            content = "It's {}".format(time)
            return content
        elif("date" in command):
            date = info_interface.interp(command)
            content = "Today is {}".format(date)
            return content
        elif("weather" in command):
            location, curr_weather = info_interface.interp(command)
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
            return content

