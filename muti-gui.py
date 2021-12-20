import threading
import tkinter as tk
from tkinter.filedialog import askdirectory
import youtube_dl
import glob
import shutil
import os
import subprocess
from threading import Thread

def GUI():
    def selectpath():
        path_ = askdirectory()
        path.set(path_)
    
    def clickurl():
        def download():
            t = threading.Thread(target=download1)
            t.start()
            
        def download1():
            if s1.get() == 0:
                if s2.get() == 0:
                    ydl_opts = {
                                'format': 'bestaudio',
                                'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                                }],
                                #'logger': MyLogger(),
                                #'progress_hooks': [my_hook],
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url.get()])
                    fname=path.get()
                    if not os.path.exists(fname):
                        os.mkdir("music")  
                        x=glob.glob("*.mp3")
                        for i in range(len(x)):
                            shutil.move(x[i],fname) 
                    else:
                        x=glob.glob("*.mp3")
                        for i in range(len(x)):
                            shutil.move(x[i],fname)
                elif s2.get() == 1:
                    ydl_opts = {
                                'format': 'worstaudio',
                                'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                                }],
                                #'logger': MyLogger(),
                                #'progress_hooks': [my_hook],
                    }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url.get()])
                    fname=path.get()
                    if not os.path.exists(fname):
                        os.mkdir("music")  
                        x=glob.glob("*.mp3")
                        for i in range(len(x)):
                            shutil.move(x[i],fname) 
                    else:
                        x=glob.glob("*.mp3")
                        for i in range(len(x)):
                            shutil.move(x[i],fname)

            elif s1.get() == 1:
                if s2.get() == 0:
                    ydl_opts = {
                            'format': 'bestvideo+bestaudio'
                        }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url.get()])

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
                        fname="mv"
                        if not os.path.exists(fname):
                            os.mkdir("mv")  
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv") 
                        else:
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv")

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
                        fname="mv"
                        if not os.path.exists(fname):
                            os.mkdir("mv")  
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv") 
                        else:
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv")
                if s2.get() == 1:
                    ydl_opts = {
                            'format': 'worstvideo+worstaudio'
                        }
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url.get()])

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
                        fname="mv"
                        if not os.path.exists(fname):
                            os.mkdir("mv")  
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv") 
                        else:
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv")

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
                        fname="mv"
                        if not os.path.exists(fname):
                            os.mkdir("mv")  
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv") 
                        else:
                            x=glob.glob("*.mp4")
                            for i in range(len(x)):
                                shutil.move(x[i],"./mv") 

        labelmsg.config(text="")
        if url.get() == "":
            labelmsg.config(text="網址欄位必須輸入")
        
        else:
            durl = url.get()
            label3 = tk.Label(frame3, text="下載選項")
            radio1 = tk.Radiobutton(frame3, text="音樂", variable=s1, value=0)
            radio2 = tk.Radiobutton(frame3, text="影片", variable=s1, value=1)
            label3.grid(row=0, column=1, sticky="w" )
            radio1.grid(row=1, column=1, sticky="w")
            radio2.grid(row=2, column=1, sticky="w")

            label4 = tk.Label(frame3, text="下載品質")
            radio3 = tk.Radiobutton(frame3, text="高", variable=s2, value=0)
            radio4 = tk.Radiobutton(frame3, text="低", variable=s2, value=1)
            label4.grid(row=4, column=1, sticky="w" )
            radio3.grid(row=5, column=1, sticky="w")
            radio4.grid(row=6, column=1, sticky="w")

            btndown = tk.Button(frame3, text="下載", command=download)
            btndown.grid(row=7, column=1, sticky="s")
            #btndown.config(state="disabled")
            btndown.config(state="normal")

    win = tk.Tk()
    win.geometry("450x320")
    win.title("Youtube DL")

    video = tk.IntVar()
    url = tk.StringVar()
    path = tk.StringVar()
    filename = tk.StringVar()
    s1 = tk.IntVar()
    s2 = tk.IntVar()

    frame1 = tk.Frame(win, width=450)
    frame1.pack()

    label1 = tk.Label(frame1, text="Youtube 網址")
    entryurl = tk.Entry(frame1, textvariable=url)
    entryurl.config(width=40)
    label1.grid(row=0, column=0, sticky="e")
    entryurl.grid(row=0, column=1)

    label2 = tk.Label(frame1, text="存檔路徑:")
    entrypath = tk.Entry(frame1, textvariable=path)
    entrypath.config(width=40)
    btnpath = tk.Button(frame1, text = "路徑選擇", command=selectpath)
    btnpath.grid(row=1, column=1, sticky="e")
    label2.grid(row=1, column=0, pady=6, sticky="e")
    entrypath.grid(row=1, column=1)

    frame2 = tk.Frame(win)
    btnurl = tk.Button(frame2, text = "確定", command=clickurl)
    btnurl.grid(row=0, column=2)
    frame2.pack()

    labelmsg = tk.Label(win, text="", fg="red")
    labelmsg.pack()

    frame3 = tk.Frame(win)
    frame3.pack()

    win.mainloop()


if __name__ == '__main__':
    GUI()