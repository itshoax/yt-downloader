from fastapi import FastAPI, BackgroundTasks
from services.downloader import Downloader
from config.settings import setup_logging


setup_logging()
app = FastAPI()

@app.get('/')
def show():
  print("Let's go,,,,")

@app.post('/download')
def download(req, background_tasks: BackgroundTasks):
  d = Downloader()
  background_tasks.add_task(d.download_video())
  print(f"Request looks like this #{req}")
