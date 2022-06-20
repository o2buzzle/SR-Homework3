import time
import text_to_speech, core_interactions, preprocess
import speech_recognition as sr
from io import StringIO
import sys


class TeeOut(StringIO):
    def write(self, s):
        StringIO.write(self, s)
        sys.__stdout__.write(s)


class TeeErr(StringIO):
    def write(self, s):
        StringIO.write(self, s)
        sys.__stderr__.write(s)


def perform_callback(r, audio):

    text = r.recognize_google(audio, language="en-US", show_all=False)
    prep_text = preprocess.preprocess(text[0])
    result = core_interactions.interpreter(prep_text)
    # print(result)
    text_to_speech.tts.speak(result)


def main(queue):
    out = TeeOut()
    err = TeeErr()

    sys.stdout = out
    sys.stderr = err

    r = sr.Recognizer()
    m = sr.Microphone()

    while True:
        with m as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(m)
            perform_callback(r, audio)
            queue.put(out.getvalue())
            queue.put(err.getvalue())
            time.sleep(1)


if __name__ == "__main__":
    main()
