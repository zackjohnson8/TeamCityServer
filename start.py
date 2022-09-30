import os
import sys

from src.helpers import yaml_helper, command_helper
from src.extends import logger
from src.handlers.argument_handler import ArgumentHandler
from src.models import script_model

logging = logger.get_logger(__name__)


def run_teamcity_docker(docker_hub_user: str):
    # Server build and push commands
    server_dockerfile_build_command = \
        ['docker', 'build', '-f',
         'docker/teamcity_server/dockerfile/teamcity_server.Dockerfile',
         '-t',
         f'{docker_hub_user}/teamcity-server', '.']
    server_dockerfile_push_command = \
        ['docker', 'push', f'{docker_hub_user}/teamcity-server']
    # Build and push the teamcity server docker image
    command_helper.run_commands(server_dockerfile_build_command)
    command_helper.run_commands(server_dockerfile_push_command)

    # Agent build and push commands
    agent_dockerfile_build_command = \
        ['docker', 'build', '-f',
         'docker/teamcity_agent/dockerfile/teamcity_agent.Dockerfile',
         '-t',
         f'{docker_hub_user}/teamcity-agent', '.']
    agent_dockerfile_push_command = \
        ['docker', 'push', f'{docker_hub_user}/teamcity-agent']
    # Build and push the teamcity agent docker image
    command_helper.run_commands(agent_dockerfile_build_command)
    command_helper.run_commands(agent_dockerfile_push_command)

    # Database build and push commands
    database_dockerfile_build_command = \
        ['docker', 'build', '-f',
         'docker/teamcity_database/dockerfile/teamcity_database.Dockerfile',
         '-t',
         f'{docker_hub_user}/teamcity-database', '.']
    database_dockerfile_push_command = \
        ['docker', 'push', f'{docker_hub_user}/teamcity-database']
    # Build and push the teamcity database docker image
    command_helper.run_commands(database_dockerfile_build_command)
    command_helper.run_commands(database_dockerfile_push_command)

    # Set environment variables for the docker-compose file
    teamcity_configs = yaml_helper.read_file('configs', 'teamcity_configs.yml')
    os.environ['DOCKER_HUB_USER'] = docker_hub_user
    os.environ['SERVER_DATA_VOLUME_DIR'] = os.path.abspath(teamcity_configs["teamcity"]["server"]["data_folder"])
    os.environ['SERVER_LOGS_VOLUME_DIR'] = os.path.abspath(teamcity_configs["teamcity"]["server"]["logs_folder"])
    os.environ['AGENT_CONF_VOLUME_DIR'] = os.path.abspath(teamcity_configs["teamcity"]["agent"]["conf_folder"])
    os.environ['AGENT_SYSTEM_VOLUME_DIR'] = os.path.abspath(teamcity_configs["teamcity"]["agent"]["system_folder"])
    os.environ['DATABASE_DATA_VOLUME_DIR'] = os.path.abspath(teamcity_configs["teamcity"]["database"]["data_folder"])

    # Docker stack deploy and status commands
    docker_stack_deploy_command = ['docker', 'stack', 'deploy', '--prune', '-c',
                                   'docker/docker_compose/docker-compose-linux.yml',
                                   'local-teamcity']
    docker_stack_status_command = ['docker', 'stack', 'services', 'local-teamcity']
    docker_stack_network_command = ['docker', 'network', 'inspect', 'local-teamcity_teamcity-network']
    # Deploy and check the status of the docker stack
    command_helper.run_commands(docker_stack_deploy_command)
    command_helper.run_commands(docker_stack_status_command)
    command_helper.run_commands(docker_stack_network_command)


def main(argv):
    model = script_model.ScriptModel("The start script for the teamcity docker stack.", script_model.ScriptType.START)
    argument_handler = ArgumentHandler(model)
    args = argument_handler.parse_args(argv)
    run_teamcity_docker(args.username)


if __name__ == '__main__':
    logging.info('Starting start.py')
    main(sys.argv[1:])
