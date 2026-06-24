from fastapi import FastAPI
from config.settings import setup_logging
from services.video_info import VideoInfo
from tasks import download_video_task
from pydantic import BaseModel

class DownloadRequest(BaseModel):
  url: str
  resolution: int = 1080

setup_logging()
app = FastAPI()

@app.get("/video")
def show(url: str, resolution: int):
  print(f"The url is {url}")
  video_info = VideoInfo()
  result = video_info.get_info(url)
  return { "data": result }

@app.post('/download')
def download(req: DownloadRequest):
  print(f"Request looks like this #{req}")
  download_video_task.delay(req.url, req.resolution)
  return {"message": "Download started"}
