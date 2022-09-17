import os

from helpers import logging_helper

logger = logging_helper.get_logger(__name__)


def append_paths(string, append_to: list):
    for append in append_to:
        if append.startswith('/'):
            logger.error(f'Invalid directory path: {append}. Please use a relative path. '
                         f'Change the path in the Teamcity configs file.')
        append_to[append] = os.path.join(string, append_to[append])
    return append_to
