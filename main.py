from fastapi import FastAPI, BackgroundTasks
from services.downloader import Downloader
from config.settings import setup_logging
from tasks import download_video_task
from pydantic import BaseModel

class DownloadRequest(BaseModel):
  url: str

setup_logging()
app = FastAPI()

@app.get('/')
def show():
  print("Let's go,,,,")

@app.post('/download')
def download(req: DownloadRequest):
  print(f"Request looks like this #{req}")
  download_video_task.delay(req.url)
  return {"message": "Download started"}
