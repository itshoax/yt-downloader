import logging

# Put an environment variable later, so we can classify in which environment we are running like dev, prod
def setup_logging():
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
