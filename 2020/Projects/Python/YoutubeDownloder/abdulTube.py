import pytube
import os

link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()
video_name = stream.default_filename
os.rename(video_name, 'newvideo.mp4')
