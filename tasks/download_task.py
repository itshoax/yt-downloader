from config.celery_config import celery_app
from workers.download_worker import DownloadWorker

@celery_app.task(bind=True)
def download_video_task(self, url, resolution):
  worker = DownloadWorker()
  task_id = self.request.id
  print(f"task_id is this: {task_id}")
  result = worker.execute(url, task_id, resolution, {})
  print(f"result is this: {result}")
  return { 'task_id': task_id, 'status': 'downloading' }
