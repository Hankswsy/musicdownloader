from __future__ import unicode_literals
import youtube_dl

'''class MyLogger(object):
    def debug(self, msg):
        print(msg)
        
    def warning(self, msg):
        #print(msg)
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')'''

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
def music(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])