from config.celery_config import celery_app
from config.settings import setup_logging

__all__ = ['celery_app', 'setup_logging']
