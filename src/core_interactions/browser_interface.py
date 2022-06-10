import webbrowser


def _launch_webpage(url):
    webbrowser.open(url)


def _google_search(query):
    return "https://www.google.com/search?q=" + query


def _youtube_search(query):
    return "https://www.youtube.com/results?search_query=" + query


def _bing_search(query):
    return "https://www.bing.com/search?q=" + query


def interp(q):
    if q.startswith("google"):
        _launch_webpage(_google_search(q[7:]))
    elif q.startswith("youtube"):
        _launch_webpage(_youtube_search(q[8:]))
    elif q.startswith("youtube"):
        _launch_webpage(_youtube_search(q[8:]))
    else:
        raise Exception("Unknown command")
