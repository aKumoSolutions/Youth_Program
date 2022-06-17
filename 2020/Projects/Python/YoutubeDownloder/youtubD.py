import pytube
import os
from os import path

def download():
    link = input("Enter the youtube link you want to donwload: ")
    name = input("Name the vidoe: ")
    yt = pytube.YouTube(link)
    if yt.views >= 1000000:
        if path.exists('overmil'):
            stream = yt.streams.get_highest_resolution()
            stream.download('overmil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")
        else:
            os.mkdir('overmil')
            stream = yt.streams.get_highest_resolution()
            stream.download('overmil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")
    else:
        if path.exists('undermil'):
            print("This video has less than million views, it's in undermil")
            stream = yt.streams.get_highest_resolution()
            stream.download('undermil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")
        else:
            os.mkdir('undermil')
            print("This video has less than million views, it's in undermil")
            stream = yt.streams.get_highest_resolution()
            stream.download('undermil')
            video_name = stream.default_filename
            os.rename(video_name, name + ".mp4")

download()