import os
import subprocess


def run_teamcity_docker_compose():
    directory = os.path.dirname(os.path.realpath(__file__))
    file_name = '/teamcity-docker-compose.yaml'

    command = ['docker-compose', '-f', directory + file_name, 'up', '-d']
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return popen


def create_teamcity_dir():
    data_dir_path = f'teamcity/datadir'
    logs_dir_path = f'teamcity/logs'
    agent_dir_path = f'teamcity/agent_conf'
    directory_paths = [data_dir_path, logs_dir_path, agent_dir_path]
    for directory_path in directory_paths:
        os.makedirs(directory_path, exist_ok=True)


def main():
    # Create a teamcity directory and upgrade the folder privileges
    create_teamcity_dir()

    # Run the docker-compose for TeamCity
    run_teamcity_docker_compose()


if __name__ == '__main__':
    main()
