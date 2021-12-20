from __future__ import unicode_literals
import youtube_dl
import subprocess
import glob
import os

ydl_opts = {
    'format': 'bestvideo+bestaudio'
}
def mv(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if len(glob.glob("*.mkv"))>=1:
        x=glob.glob("*.mkv")
        for i in range(len(x)):
            os.rename(x[i],x[i].replace(" ",""))
        y=glob.glob("*.mkv")
        for j in range(len(y)):
            y1=y[j].replace(".mkv","") 
            subprocess.run(f"ffmpeg -i {y[j]} {y1}.mp4")
        for i in range(len(y)):
            os.remove(y[i])

    elif len(glob.glob("*.webm"))>=1:
        x=glob.glob("*.webm")
        for i in range(len(x)):
            os.rename(x[i],x[i].replace(" ",""))
        y=glob.glob("*.webm")
        for j in range(len(y)):
            y1=y[j].replace(".webm","") 
            subprocess.run(f"ffmpeg -i {y[j]} {y1}.mp4")
        for i in range(len(y)):
             os.remove(y[i])

