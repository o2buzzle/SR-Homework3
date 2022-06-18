import os
import webbrowser
import yt_dlp

YTDL_OPTS = {
    "default_search": "ytsearch",
}

YOUTUBE_DL = yt_dlp.YoutubeDL(params=YTDL_OPTS)


def _search_youtube(q: str) -> str:
    """
    Searches YouTube for the query q and returns the URL of the first result.
    """
    return YOUTUBE_DL.extract_info(q, download=False)["entries"][0]["webpage_url"]


def _play_youtube(q: str) -> None:
    """
    Searches YouTube for the query q and plays the first result.
    """
    url = _search_youtube(q)
    webbrowser.open(url)
    return "Opening webpage"


def interp(q: str) -> None:
    if q.startswith("play"):
        return _play_youtube(q[5:])
    elif q.startswith("search"):
        return _play_youtube(q[7:])
    else:
        raise Exception("Unknown command")
