from fastapi import FastAPI
from config.settings import setup_logging
from services.video_info import VideoInfo
from tasks import download_video_task
from pydantic import BaseModel
import json
from redis import Redis

r = Redis()

class DownloadRequest(BaseModel):
  url: str
  resolution: int = 1080

setup_logging()
app = FastAPI()

@app.get("/video")
def show(url: str):
  print(f"The url is {url}")
  video_info = VideoInfo()
  result = video_info.get_info(url)
  return { "data": result }

@app.post('/download')
def download(req: DownloadRequest):
  print(f"Request looks like this #{req}")
  result = download_video_task.delay(req.url, req.resolution)
  return {"message": "Download started", 'task_id': result.task_id }

@app.get('/download_status/{task_id}')
def download_status(task_id: str):
  progress = r.get(f'progress:{task_id}')
  if not progress:
    return { 'status': 'pending' }
  return json.loads(progress)
