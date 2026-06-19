import logging

logger = logging.getLogger(__name__)

class BaseWorker():
  def execute(self, *args, **kwargs):
    raise NotImplementedError("Method execute is not implemented in child class")

  def on_success(self, result):
    logger.info(f"Success: {result}")

  def on_failure(self, exc):
    logger.error(f"Failure: {exc}")
