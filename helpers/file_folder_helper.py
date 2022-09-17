import os

from helpers import logging_helper

logger = logging_helper.get_logger(__name__)


def create_folder_if_not_exists(folder_path, exist_ok=True):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=exist_ok)
        # wait for the folder to be created
        while not os.path.exists(folder_path):
            pass
        logger.info(f'Created folder: {folder_path}')
    else:
        logger.info(f'Folder already exists: {folder_path}')


def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
        logger.info(f'Created file: {file_path}')
    else:
        logger.info(f'File already exists: {file_path}')
