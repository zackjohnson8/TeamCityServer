"""
    Description: Use this script to automate the setup process for a new teamcity server, agent, and database.
"""
import os
from helpers import yaml_helper, logging_helper, file_folder_helper

logger = logging_helper.get_logger(__name__)

working_directory = os.path.dirname(os.path.realpath(__file__))


def create_teamcity_dir(data_dir='/teamcity/data', logs_dir='/teamcity/logs', agent_dir='/teamcity/agent'):
    directory_paths = [data_dir, logs_dir, agent_dir]
    for directory_path in directory_paths:
        os.makedirs(directory_path, exist_ok=True)


def main():
    teamcity_configs = yaml_helper.read_file(f'{working_directory}/configs', 'teamcity_configs.yml')

    # Create a teamcity home directory
    home_dir = teamcity_configs['teamcity']['home_dir']
    file_folder_helper.create_folder_if_not_exists(home_dir)

    # Create the Teamcity database directories
    database_directories = teamcity_configs['teamcity']['database']
    for database_directory in database_directories.values():
        if database_directory.startswith('/'):
            logger.error(f'Invalid directory path: {database_directory}. Please use a relative path. '
                         f'Change the path in the Teamcity configs file.')
        database_directory = os.path.join(home_dir, database_directory)
        file_folder_helper.create_folder_if_not_exists(database_directory)

    # Create the Teamcity server directories
    server_directories = teamcity_configs['teamcity']['server']
    for server_directory in server_directories.values():
        if server_directory.startswith('/'):
            logger.error(f'Invalid directory path: {server_directory}. Please use a relative path. '
                         f'Change the path in the Teamcity configs file.')
        server_directory = os.path.join(home_dir, server_directory)
        file_folder_helper.create_folder_if_not_exists(server_directory)

    # Create the Teamcity agent directories
    agent_directories = teamcity_configs['teamcity']['agent']
    for agent_directory in agent_directories.values():
        if agent_directory.startswith('/'):
            logger.error(f'Invalid directory path: {agent_directory}. Please use a relative path. '
                         f'Change the path in the Teamcity configs file.')
        agent_directory = os.path.join(home_dir, agent_directory)
        file_folder_helper.create_folder_if_not_exists(agent_directory)


if __name__ == '__main__':
    logger.info('Starting setup.py')
    main()
