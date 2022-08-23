import argparse
from models.script_model import ScriptModel
from models.types.script_type import ScriptType


class ArgumentHandler(argparse.ArgumentParser):
    """
     TODO
    """
    def __init__(self, script_model: ScriptModel):
        # These are the arguments that will be parsed from the command line. These arguments will override the
        # configuration file.
        super().__init__(description=script_model.description)
        if script_model.script_type == ScriptType.SETUP:
            self.add_argument('-h', '--home', help='Path to the home directory where teamcity is installed. '
                                                   'Use to override the value in the teamcity configuration file.')
            self.add_argument('-d', '--data', help='Path to the directory where teamcity data is stored. '
                                                   'Use to override the value in the teamcity configuration file.')
            self.add_argument('-l', '--logs', help='Path to the directory where teamcity logs are stored. '
                                                   'Use to override the value in the teamcity configuration file.')
            self.add_argument('-a', '--agent', help='Path to the directory where teamcity agent configuration is '
                                                    'stored. Use to override the value in the teamcity '
                                                    'configuration file.')
        elif script_model.script_type == ScriptType.START:
            # TODO: Add arguments for starting the service
            # self.add_argument('-s', '--start', action='store_true', help='Start the service')
            pass
        elif script_model.script_type == ScriptType.STOP:
            # TODO: Add arguments for stopping the service
            # self.add_argument('-s', '--stop', action='store_true', help='Stop the service')
            pass
        elif script_model.script_type == ScriptType.RESET:
            # TODO: Add arguments for resetting the service
            # self.add_argument('-s', '--reset', action='store_true', help='Reset the service')
            pass
        elif script_model.script_type == ScriptType.CLEANUP:
            # TODO: Add arguments for cleaning up the environment
            # self.add_argument('-s', '--cleanup', action='store_true', help='Cleanup the environment')
            pass
        elif script_model.script_type == ScriptType.STATUS:
            # TODO: Add arguments for getting the status of the service
            # self.add_argument('-s', '--status', action='store_true', help='Status of the service')
            pass
        else:
            raise Exception('Invalid script type')
