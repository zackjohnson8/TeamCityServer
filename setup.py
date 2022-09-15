"""
    Description: Use this script to automate the setup process for a new teamcity server, agent, and database.
"""
import os
import logging.config
from helpers import yaml_helper, logging_helper

working_directory = os.path.dirname(os.path.realpath(__file__))

logging_helper.setup_logging(config_path=f'{working_directory}/configs/logging_configs.yml')
logger = logging.getLogger(__name__)


def create_teamcity_dir(data_dir='/teamcity/data', logs_dir='/teamcity/logs', agent_dir='/teamcity/agent'):
    directory_paths = [data_dir, logs_dir, agent_dir]
    for directory_path in directory_paths:
        os.makedirs(directory_path, exist_ok=True)


def main():
    # Create a teamcity directory
    teamcity_configs = yaml_helper.read_file(f'{working_directory}/configs', 'teamcity_configs.yml')

    home_dir = teamcity_configs['teamcity']['home_dir']
    data_directory = os.path.join(home_dir, teamcity_configs['teamcity']['data_folder'])
    logs_directory = os.path.join(home_dir, teamcity_configs['teamcity']['logs_folder'])
    agent_directory = os.path.join(home_dir, teamcity_configs['teamcity']['agent_folder'])

    create_teamcity_dir(data_dir=data_directory,
                        logs_dir=logs_directory,
                        agent_dir=agent_directory)


if __name__ == '__main__':
    main()
