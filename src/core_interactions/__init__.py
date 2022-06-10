from . import system_interface, browser_interface, media_interface, info_interface


def interpreter(command: str):
    intent, command = command.split(" ", 1)
    if intent == "system":
        return system_interface.interp(command)
    elif intent == "browser":
        return browser_interface.interp(command)
    elif intent == "media":
        return media_interface.interp(command)
    elif intent == "info":
        return info_interface.interp(command)
