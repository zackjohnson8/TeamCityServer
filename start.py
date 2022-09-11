import subprocess
import os

working_directory = os.path.dirname(os.path.realpath(__file__))


def run_teamcity_docker_compose():
    file_name = '/teamcity-docker-compose.yaml'

    command = ['docker-compose', '-f', working_directory + file_name, 'up', '-d']
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return popen


def main():
    run_teamcity_docker_compose()


if __name__ == '__main__':
    main()
