from pytube import YouTube

link = "https://www.youtube.com/watch?v=DRmHO74l-mU"
yt = YouTube(link)
ys = yt.stream.get_highest_resolution()
ys.download