import os

from src.extends import logger

logging = logger.get_logger(__name__)


def append_paths(string, append_to: list):
    for append in append_to:
        if append.startswith('/'):
            logging.error(f'Invalid directory path: {append}. Please use a relative path. '
                          f'Change the path in the Teamcity configs file.')
        append_to[append] = os.path.join(string, append_to[append])
    return append_to
