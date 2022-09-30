import subprocess

from src.extends import logger

logging = logger.get_logger(__name__)


def run_commands(commands: list, wait: bool = True):
    popen = subprocess.Popen(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             universal_newlines=True)
    if wait:
        popen.wait()
    stdout, stderr = popen.communicate()
    if stderr:
        logging.error(stderr)
    else:
        logging.info(stdout)
