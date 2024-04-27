from pytube import YouTube, Playlist, Search
from pathlib import Path
import os
from moviepy.editor import *
from time import sleep
import unicodedata
import re



DOWNLOADS = str(Path.home() / "Downloads")


def slugify(value):
    return ''.join([x for x in value if x not in '\''])


def download_playlist(link: str) -> None:
    pl = Playlist(link)
    for video in pl.videos:
        video.streams.get_highest_resolution().download(DOWNLOADS)


def download_video(link: str) -> None:
    video = YouTube(link)
    video.streams.get_highest_resolution().download(DOWNLOADS)


def download_search(search_name: str, amount_videos: int) -> None:
    s = Search(search_name)
    for i in range(amount_videos):
        s.results[i].streams.get_highest_resolution().download(DOWNLOADS)


def convert_yt_to_mp3(link: str) -> None:
    video = YouTube(link)
    video.streams.first().download(DOWNLOADS)

    path1 = os.path.join(DOWNLOADS, slugify(video.title) + '.mp4')

    vid = VideoFileClip(path1)
    audio = vid.audio
    path2 = os.path.join(DOWNLOADS, slugify(video.title) + '.mp3')
    audio.write_audiofile(path2)

    audio.close()
    vid.close()

    os.remove(path1)


def convert_playlist_mp3(link: str) -> None:
    pl = Playlist(link)
    for video in pl.videos:
        video.streams.first().download(DOWNLOADS)

        path1 = os.path.join(DOWNLOADS, slugify(video.title) + '.mp4')

        vid = VideoFileClip(path1)
        audio = vid.audio
        path2 = os.path.join(DOWNLOADS, slugify(video.title) + '.mp3')
        audio.write_audiofile(path2)
        audio.close()
        vid.close()

        os.remove(path1)




