import logging

from config import Config

CONFIG = Config()

logging.basicConfig(filename=CONFIG['Default']['LOG_PATH'], level=logging.INFO)
logger = logging.getLogger()
