"""
    Description: Use this script to automate the setup process for a new teamcity server, agent, and database.
"""
import os
from helpers import yaml_helper, logging_helper, file_folder_helper

logger = logging_helper.get_logger(__name__)

working_directory = os.path.dirname(os.path.realpath(__file__))


def main():
    teamcity_configs = yaml_helper.read_file(f'{working_directory}/configs', 'teamcity_configs.yml')

    # Create server, agents, and database directories
    server_directories = teamcity_configs['teamcity']['server'].values()
    database_directories = teamcity_configs['teamcity']['database'].values()
    agent_directories = teamcity_configs['teamcity']['agent'].values()
    file_folder_helper.create_directories(server_directories)
    file_folder_helper.create_directories(database_directories)
    file_folder_helper.create_directories(agent_directories)


if __name__ == '__main__':
    logger.info('Starting setup.py')
    main()
