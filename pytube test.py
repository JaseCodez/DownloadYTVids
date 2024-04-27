"""
Authors: Jason Phan
Created on: April 26th, '24
Last Updated: April 27th, '24

Convert a Youtube link and/or a Youtube playlist into mp3 and mp4 files in user's main download. 
"""


from pytube import YouTube, Playlist, Search
from pathlib import Path
from moviepy.editor import *


INVALID_FILE_NAME = '#%&{}\\<>*?/$!\'\":@+`|='
DOWNLOADS = str(Path.home() / "Downloads")


def slugify(value):
    return ''.join([x for x in value if x not in INVALID_FILE_NAME])


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
    print('Don\'t worry about the File Not Found part, idk why it keeps on saying that')
    path1 = os.path.join(DOWNLOADS, slugify(video.title) + '.mp4')

    try:
        vid = VideoFileClip(path1)
        audio = vid.audio
        path2 = os.path.join(DOWNLOADS, slugify(video.title) + '.mp3')
        audio.write_audiofile(path2)

        audio.close()
        vid.close()

    except OSError:
        print('Unfortunately, this video cannot be converted into an mp3 file for some reason idk how to fix this')
    os.remove(path1)


def convert_playlist_mp3(link: str) -> None:
    pl = Playlist(link)
    for video in pl.videos:
        convert_yt_to_mp3(video.embed_url)




