import logging
import os

logger = logging.getLogger(__name__)


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger.info(f'Created folder: {folder_path}')
    else:
        logger.info(f'Folder already exists: {folder_path}')


def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
        logger.info(f'Created file: {file_path}')
    else:
        logger.info(f'File already exists: {file_path}')
