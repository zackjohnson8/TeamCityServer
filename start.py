import logging.config
import os

from helpers import command_helper, yaml_helper

# /home/locallinux/PycharmProjects/TeamCityProject
working_directory = os.path.dirname(os.path.realpath(__file__))

logger = logging.getLogger(__name__)


def run_teamcity_docker():
    teamcity_configs = yaml_helper.read_file(f'{working_directory}/configs', 'teamcity_configs.yml')
    teamcity_server_configs = teamcity_configs['teamcity']['server']
    teamcity_agent_configs = teamcity_configs['teamcity']['agent']

    for config in teamcity_server_configs:
        if config.startswith('/'):
            logger.error(f'Invalid directory path: {config}. Please use a relative path. '
                         f'Change the path in the Teamcity configs file.')
        teamcity_server_configs[config] = os.path.join(teamcity_configs['teamcity']['home_dir'],
                                                       teamcity_server_configs[config])

    for config in teamcity_agent_configs:
        if config.startswith('/'):
            logger.error(f'Invalid directory path: {config}. Please use a relative path. '
                         f'Change the path in the Teamcity configs file.')
        teamcity_agent_configs[config] = os.path.join(teamcity_configs['teamcity']['home_dir'],
                                                      teamcity_agent_configs[config])

    # Run Dockerfiles
    # Create commands for building, running, and pushing docker images
    server_dockerfile_remove_command = ['docker', 'rm', '-f', 'server']
    server_dockerfile_build_command = \
        ['docker', 'build', '-f',
         f'{working_directory}/teamcity_server/dockerfile/teamcity_server.Dockerfile',
         '-t',
         'zackjohnson8/teamcity-server', '.']
    server_dockerfile_run_command = \
        ['docker', 'run', '-it', '-d', '--name', 'server',
         '-e', 'TEAMCITY_SERVER_MEM_OPTS=-Xmx3g -XX:MaxPermSize=270m -XX:ReservedCodeCacheSize=450m',
         '-v', f'{teamcity_server_configs["data_folder"]}:/data/teamcity_server/datadir',
         '-v', f'{teamcity_server_configs["logs_folder"]}:/opt/teamcity/logs',
         '-p', '8111:8111',
         'zackjohnson8/teamcity-server']
    server_dockerfile_push_command = ['docker', 'push', 'zackjohnson8/teamcity-server']

    # Docker build, run, and push commands
    command_helper.run_commands(server_dockerfile_remove_command)
    command_helper.run_commands(server_dockerfile_build_command)
    command_helper.run_commands(server_dockerfile_run_command)
    command_helper.run_commands(server_dockerfile_push_command)

    # Agent Dockerfile
    agent_dockerfile_remove_command = ['docker', 'rm', '-f', 'agent']
    agent_dockerfile_build_command = ['docker', 'build', '-f',
                                      f'{working_directory}/teamcity_agent/dockerfile/teamcity_agent.Dockerfile',
                                      '-t',
                                      'zackjohnson8/teamcity-agent', '.']
    agent_dockerfile_run_command = ['docker', 'run', '-it', '-d', '--name', 'agent',
                                    '--link', 'server',
                                    '-e', 'SERVER_URL=http://server:8111',
                                    '-v', f'{teamcity_agent_configs["conf_folder"]}:/data/teamcity_agent/conf',
                                    '-v', f'{teamcity_agent_configs["system_folder"]}:/data/teamcity_agent/system',
                                    'zackjohnson8/teamcity-agent']
    agent_dockerfile_push_command = ['docker', 'push', 'zackjohnson8/teamcity-agent']

    # Docker build, run, and push commands
    command_helper.run_commands(agent_dockerfile_remove_command)
    command_helper.run_commands(agent_dockerfile_build_command)
    command_helper.run_commands(agent_dockerfile_run_command)
    command_helper.run_commands(agent_dockerfile_push_command)


def main():
    run_teamcity_docker()


if __name__ == '__main__':
    main()
