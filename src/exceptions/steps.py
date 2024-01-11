from exceptions.base import CliTemplaterError

class StepError(CliTemplaterError):
    pass

class StepClassCreationError(StepError):
    pass

class StepDoesntExistError(StepError):
    pass
