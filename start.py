import os

from helpers import logging_helper, command_helper

logger = logging_helper.get_logger(__name__)

working_directory = os.path.dirname(os.path.realpath(__file__))


def run_teamcity_docker():
    docker_compose_down_command = ['docker', 'compose', '-f', 'docker_compose/docker-compose-linux.yml', 'down']
    docker_compose_up_command = ['docker', 'compose', '-f', 'docker_compose/docker-compose-linux.yml', 'up', '-d',
                                 '--build']
    docker_compose_push_command = ['docker', 'compose', '-f', 'docker_compose/docker-compose-linux.yml', 'push']
    command_helper.run_commands(docker_compose_down_command)
    command_helper.run_commands(docker_compose_up_command)
    command_helper.run_commands(docker_compose_push_command)


def main():
    run_teamcity_docker()


if __name__ == '__main__':
    logger.info('Starting start.py')
    main()
