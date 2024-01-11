from enum import StrEnum, auto


class StepTypes(StrEnum):
    BUILD_TREE = auto()
    SHELL = auto()
    COMPOSITE = auto()
    IF_VARIABLE = auto()
    IMPORT = auto()
