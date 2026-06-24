from config.celery_config import celery_app
from workers.download_worker import DownloadWorker

@celery_app.task
def download_video_task(url, resolution):
  worker = DownloadWorker()
  result = worker.execute(url, resolution, {})
  return result
