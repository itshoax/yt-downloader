from yt_dlp import YoutubeDL
from redis import Redis
import json

r = Redis()

class Downloader():
  def __init__(self, task_id: int, resolution: int = 1080):
    self.options = {
      'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
      'outtmpl': '/tmp/%(title)s.%(ext)s',
      'merge_output_format': 'mp4',
      'progress_hooks': [self._on_progress],
    }
    self.task_id = task_id

  def download_video(self, url):
    with YoutubeDL(self.options) as ydl:
      info = ydl.extract_info(url)
      return info.get('title')

  def _on_progress(self, d):
    progress = {'status': 'finished' }
    print(f"Inside the progress hook {d}")
    if d['status'] == 'finished':
      r.set(f'progress:{self.task_id}', json.dumps(progress))
      return

    if d['status'] == 'downloading':
      print("The status is not coming here")
      progress = {
        'status': 'downloading',
        'percent': d.get('_percent_str', '0%'),
        'speed': d.get('_speed_str', ''),
        'eta': d.get('_eta_str', ''),
      }

      r.set(f'progress:{self.task_id}', json.dumps(progress))
