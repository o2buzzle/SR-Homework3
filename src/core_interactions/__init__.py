from . import system_interface, browser_interface, media_interface, info_interface
from speech_to_text import stt


def interpreter(command: str):
    intent, command = command.split(" ", 1)
    if intent == "speak":
        command = stt.get_text()
        intent, command = command.split(" ", 1)

    if intent == "system":
        return system_interface.interp(command)
    elif intent == "browser":
        return browser_interface.interp(command)
    elif intent == "media":
        return media_interface.interp(command)
    elif intent == "info":
        return info_interface.interp(command)
