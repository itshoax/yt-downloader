from config.celery_config import celery_app
from workers.download_worker import DownloadWorker

@celery_app.task(bind=True)
def download_video_task(self, url, resolution):
  worker = DownloadWorker()
  task_id = self.request.id
  result = worker.execute(url, task_id, resolution, {})
  return result
