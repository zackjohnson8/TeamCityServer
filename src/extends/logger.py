import os
import yaml
import logging.config
import logging

DEFAULT_LEVEL = logging.INFO


def _setup_logging(config_path, default_level=DEFAULT_LEVEL):
    if os.path.exists(config_path):
        with open(config_path, 'rt') as cfg_file:
            try:
                config = yaml.safe_load(cfg_file.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(f'Error: {e}, with file, using Default logging')
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print('Config file not found, using Default logging')


working_directory = os.path.dirname(os.path.realpath(__file__))
_setup_logging(config_path=f'{working_directory}/../../configs/logging_configs.yml')


def get_logger(name):
    return logging.getLogger(name)
