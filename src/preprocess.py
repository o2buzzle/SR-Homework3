keyword = {
    "help":["help"],
    "media":["play me", "play","song", "music", "video" ],
    "browser":["search","google", "bing", "youtube","define"],
    "info":["show", "show me"],
    "system":["shutdown","shut the computer down", "screenshot"]
}
command_key = {
    "media":["play"],
    "browser":["google", "bing", "youtube"],
    "info":["date", "time", "weather"],
    "system":["shutdown", "screenshot", "reboot"]
}
default_command = {
    "media":"play",
    "browser":"google",
    "info":"time",
    "system":"screenshot"
}
def preprocess(text):
    text = text.lower()
    intent = None
    command = None
    for key in keyword:
        for word in keyword[key]: 
            if word in text:
                intent =  key
                if intent!= "system":
                    text = text.replace(word, "")
                for cmd in command_key[key]:
                    if cmd in text:
                        text = text.replace(cmd,"")
                        command = cmd
                        break
    if intent == "media":
        command = "play"
    if (intent is not None and intent!="system"):
        while (text[0]==" "):
            text= text[1:]
    if intent == "system":
        text = ""
    if intent == None or (intent=="browser" and command ==None):
        intent = "browser"
        command = "google"
    return f'{intent} {command} {text}'
if __name__ == '__main__':
    print(preprocess("what is a lamp"))
