import logging

class BaseWorker():
  def __init__(self):
    self.logger = logging.getLogger(self.__class__.__name__)

  def execute(self, *args, **kwargs):
    raise NotImplementedError("Method execute is not implemented in child class")

  def on_success(self, result):
    self.logger.info(f"Success: {result}")

  def on_failure(self, exc):
    self.logger.error(f"Failure: {exc}")

  def run(self, *args, **kwargs):
    try:
      result = self.execute(*args, **kwargs)
      self.on_success(result)
    except Exception as exc:
      self.on_failure(exc)
