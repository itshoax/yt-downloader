from yt_dlp import YoutubeDL

class Downloader():
  def __init__(self, resolution: int = 1080):
    self.options = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': '/tmp/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

  def download_video(self, url):
    with YoutubeDL(self.options) as ydl:
      info = ydl.extract_info(url)
      return info['title']
