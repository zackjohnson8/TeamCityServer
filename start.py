import os

from helpers import yaml_helper, logging_helper, path_helper, command_helper

logger = logging_helper.get_logger(__name__)

working_directory = os.path.dirname(os.path.realpath(__file__))


def run_teamcity_docker():
    teamcity_configs = yaml_helper.read_file(f'{working_directory}/configs', 'teamcity_configs.yml')
    home_dir = teamcity_configs['teamcity']['home_dir']
    teamcity_server_configs = path_helper.append_paths(home_dir, teamcity_configs['teamcity']['server'])
    teamcity_agent_configs = path_helper.append_paths(home_dir, teamcity_configs['teamcity']['agent'])
    teamcity_database_configs = path_helper.append_paths(home_dir, teamcity_configs['teamcity']['database'])

    # Setup custom network
    network_create_command = ['docker', 'network', 'create', 'teamcity-network']
    command_helper.run_commands(network_create_command)

    # Run the Postgre dockerfiles
    # Create commands for remove, building, running, and pushing docker images
    database_datafile_remove_command = ['docker', 'rm', '-f', 'postgre-db']
    database_dockerfile_build_command = \
        ['docker', 'build', '-f',
         f'{working_directory}/teamcity_database/dockerfile/teamcity_database.Dockerfile',
         '-t',
         'zackjohnson8/teamcity-database', '.']
    database_dockerfile_run_command = \
        ['docker', 'run', '-it', '-d', '--name', 'postgre-db', '--restart=unless-stopped', '--network=teamcity-network',
         '-e', 'POSTGRES_PASSWORD=mysecretpassword',
         '-e', 'POSTGRES_USER=teamcity',
         '-e', 'POSTGRES_DB=teamcity',
         '-v', f'{teamcity_database_configs["data_folder"]}:/var/lib/postgresql/data',
         '-p', '5432:5432',
         'zackjohnson8/teamcity-database']
    database_dockerfile_push_command = \
        ['docker', 'push', 'zackjohnson8/teamcity-database']

    command_helper.run_commands(database_datafile_remove_command)
    command_helper.run_commands(database_dockerfile_build_command)
    command_helper.run_commands(database_dockerfile_run_command)
    command_helper.run_commands(database_dockerfile_push_command)

    # Run Dockerfiles
    # Create commands for remove, building, running, and pushing docker images
    server_dockerfile_remove_command = ['docker', 'rm', '-f', 'server']
    server_dockerfile_build_command = \
        ['docker', 'build', '-f',
         f'{working_directory}/teamcity_server/dockerfile/teamcity_server.Dockerfile',
         '-t',
         'zackjohnson8/teamcity-server', '.']
    server_dockerfile_run_command = \
        ['docker', 'run', '-it', '-d', '--name', 'server', '--restart=unless-stopped', '--network=teamcity-network',
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
    # Create commands for remove, building, running, and pushing docker images
    agent_dockerfile_remove_command = ['docker', 'rm', '-f', 'agent']
    agent_dockerfile_build_command = ['docker', 'build', '-f',
                                      f'{working_directory}/teamcity_agent/dockerfile/teamcity_agent.Dockerfile',
                                      '-t',
                                      'zackjohnson8/teamcity-agent', '.']
    agent_dockerfile_run_command = ['docker', 'run', '-it', '-d', '--name', 'agent', '--restart=unless-stopped',
                                    '--network=teamcity-network',
                                    '-e', 'SERVER_URL=http://10.0.0.194:8111',
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
    logger.info('Starting start.py')
    main()
