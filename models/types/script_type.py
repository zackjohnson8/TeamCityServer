from enum import Enum


class ScriptType(Enum):
    SETUP = 1
    START = 2
    STOP = 3
    RESET = 4
    CLEANUP = 5
    STATUS = 6
