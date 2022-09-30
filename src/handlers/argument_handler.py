import argparse
from src.models.script_model import ScriptModel
from src.models.types.script_type import ScriptType


class ArgumentHandler(argparse.ArgumentParser):
    def __init__(self, script_model: ScriptModel):
        # These are the arguments that will be parsed from the command line. These arguments will override the
        # configuration file.
        super().__init__(description=script_model.description)
        if script_model.script_type == ScriptType.SETUP:
            pass
        elif script_model.script_type == ScriptType.START:
            self.add_argument('-u', '--username', action='store', required=True, help='The username of your docker '
                                                                                      'hub account')
            pass
        else:
            raise Exception('Invalid script type')
