from urllib.request import urlopen
from json import loads

from src.config.loggingConfig import controller_log as logger

def fetch_json(url):
    logger.debug(f"requesting resource: {url}")
    try:
        with urlopen(url) as fi:
            return loads(fi.read())
    except Exception as e:
        logger.error("Failed to acquire resource %s\n\t%s", url, e)
        return {}
