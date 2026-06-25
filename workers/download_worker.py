from workers.base_worker import BaseWorker
from services.downloader import Downloader

class DownloadWorker(BaseWorker):
  def execute(self, url: str, task_id, resolution: int, options: dict):
    d = Downloader(task_id, resolution)
    result = d.download_video(url)
    self.logger.info(f"Downloading: {url}, task_id: {task_id}")
    return result
