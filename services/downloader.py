from yt_dlp import YoutubeDL

class Downloader():
  URL = 'https://www.youtube.com/watch?v=YrE1Qg-Aw0Q&list=PLT98CRl2KxKGj-VKtApD8-zCqSaN2mD4w'
  def __init__(self):
    self.options = {
      'format': 'best',
      'outtmpl': '/tmp/%(title)s.%(ext)s'
    }

  def download_video(self, url=URL):
    with YoutubeDL(self.options) as ydl:
      info = ydl.extract_info(url)
      return info['title']
