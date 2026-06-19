from workers.base_worker import BaseWorker
from services.downloader import Downloader

class DownloadWorker(BaseWorker):
  def execute(self, url: str, options: dict):
    d = Downloader()
    result = d.download_video(url)
    self.logger.info(f"Downloading: {url}")
    return result
