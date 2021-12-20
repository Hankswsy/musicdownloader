import dmusic
import dmv
import os
import glob
import shutil

def hint():
    print("1 純音樂")
    print("2 影片")
    print("3 離開")
    
if __name__=="__main__":
    url=""
    while True:
        hint()
        x = int(input("請輸入要使用的功能代號:"))
        if x==1:
            url = input("請輸入網址")
            dmusic.music(url)
            fname="music"
            if not os.path.exists(fname):
                os.mkdir("music")  
                x=glob.glob("*.mp3")
                for i in range(len(x)):
                    shutil.move(x[i],"./music") 
            else:
                x=glob.glob("*.mp3")
                for i in range(len(x)):
                    shutil.move(x[i],"./music")

        elif x==2:
            url = input("請輸入網址")
            dmv.mv(url)
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
        elif x==3:
            break
    
    
    
    



