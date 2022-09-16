import subprocess

from helpers import logging_helper

logger = logging_helper.get_logger(__name__)


def run_commands(commands: list, wait: bool = True):
    popen = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
    if wait:
        popen.wait()
    stdout, stderr = popen.communicate()
    if stderr:
        logger.error(stderr)
    else:
        logger.info(stdout)
    pass