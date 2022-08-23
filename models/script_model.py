from models.types.script_type import ScriptType


class ScriptModel:
    def __int__(self, description: str, script_type: ScriptType):
        self.description = description
        self.script_type = script_type
