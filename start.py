import logging.config
import os

from helpers import logging_helper, command_helper

# /home/locallinux/PycharmProjects/TeamCityProject
working_directory = os.path.dirname(os.path.realpath(__file__))

logging_helper.setup_logging(config_path=f'{working_directory}/configs/logging_configs.yml')
logger = logging.getLogger(__name__)


def run_teamcity_docker():
    # Run Dockerfiles
    # Create commands for building, running, and pushing docker images
    server_dockerfile_build_command = ['docker', 'build', '-f',
                                       f'{working_directory}/teamcity_server/dockerfile/teamcity_server.Dockerfile',
                                       '-t',
                                       'zackjohnson8/teamcity-server', '.']
    server_dockerfile_run_command = ['docker', 'run', '-it', '-d', '--name', 'server', '-p', '8111:8111',
                                     'zackjohnson8/teamcity-server']
    server_dockerfile_push_command = ['docker', 'push', 'zackjohnson8/teamcity-server']

    # Docker build, run, and push commands
    command_helper.run_commands(server_dockerfile_build_command)
    command_helper.run_commands(server_dockerfile_run_command)
    command_helper.run_commands(server_dockerfile_push_command)

    # # Agent Dockerfile
    # agent_dockerfile_build_command = ['docker', 'build', '-f',
    #                                   f'{working_directory}/teamcity_agent/dockerfile/teamcity_agent.Dockerfile',
    #                                   '-t',
    #                                   'zackjohnson8/teamcity-agent', '.']
    # agent_dockerfile_run_command = ['docker', 'run', 'd', 'zackjohnson8/teamcity-agent']
    # agent_dockerfile_push_command = ['docker', 'push', 'zackjohnson8/teamcity-agent']
    #
    # popen = subprocess.Popen(agent_dockerfile_build_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                          universal_newlines=True)
    # popen.wait()
    # stdout, stderr = popen.communicate()
    # if stderr:
    #     logger.error(stderr)
    # else:
    #     logger.info(stdout)
    #
    # #  Run TeamCity Server
    # popen = subprocess.Popen(agent_dockerfile_run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                          universal_newlines=True)
    # popen.wait()
    # stdout, stderr = popen.communicate()
    # if stderr:
    #     logger.error(stderr)
    # else:
    #     logger.info(stdout)
    #
    # # Push to Dockerhub
    # popen = subprocess.Popen(agent_dockerfile_push_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                          universal_newlines=True)
    # popen.wait()
    # stdout, stderr = popen.communicate()
    # if stderr:
    #     logger.error(stderr)
    # else:
    #     logger.info(stdout)

    # # Agent Dockerfile
    # agent_dockerfile_build_command = ['docker', 'build', '-f',
    #                                   f'{working_directory}/teamcity_agent/dockerfile/teamcity_agent.Dockerfile',
    #                                   '-t', 'zackjohnson8/teamcity-agent', '.']
    # agent_dockefile_run_command = ['docker', 'run', 'd', 'zackjohnson8/teamcity-agent']
    # agent_dockerfile_push_command = ['docker', 'push', 'zackjohnson8/teamcity-agent']
    # popen = subprocess.Popen(agent_dockerfile_build_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                          universal_newlines=True)
    # print(popen.communicate())


def main():
    run_teamcity_docker()


if __name__ == '__main__':
    main()
