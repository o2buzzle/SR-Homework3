import os
import platform

# import power
import pyautogui


def _shutdown_system() -> None:
    if os.name == "nt":
        os.system("shutdown -s -t 0")
    elif os.name == "posix":
        os.system("shutdown -h now")


def _reboot_system() -> None:
    if os.name == "nt":
        os.system("shutdown -r -t 0")
    elif os.name == "posix":
        os.system("shutdown -r now")


# def _battery_status():
#    # check if a battery is present
#    if power.battery_present():
#        return power.battery_percentage()
#    else:
#        return None


def _screenshot():
    # take a screenshot
    pyautogui.screenshot(imageFilename="screenshot.png")
    # open the image
    if os.name == "nt":
        os.system("start screenshot.png")
    elif os.name == "posix":
        if platform.system() == "Darwin":
            os.system("open screenshot.png")
        elif platform.system() == "Linux":
            os.system("xdg-open screenshot.png")


def interp(q: str):
    # check if the query is a system command
    if q.startswith("shutdown"):
        _shutdown_system()
    elif q.startswith("reboot"):
        _reboot_system()
    elif q.startswith("screenshot"):
        _screenshot()
    #    elif q.startswith("battery"):
    #        return _battery_status()
    else:
        raise Exception("Unknown command")
