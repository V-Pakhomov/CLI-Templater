from abc import ABCMeta
from typing import Any

from exceptions.steps import StepClassCreationError, StepDoesntExistError


class StepMeta(ABCMeta):

    steps: dict[str, 'StepMeta'] = dict()

    def __new__(mcls: type['StepMeta'],
                name: str,
                bases: tuple[type, ...],
                namespace: dict[str, Any],) -> 'StepMeta':
        cls = super().__new__(mcls, name, bases, namespace)

        step_type = namespace.get('type')

        if step_type is None:
            raise StepClassCreationError('You cant create step without type')

        if step_type in mcls.steps:
            raise StepClassCreationError(f'Step with same type already exists: {step_type}')

        mcls.steps[step_type] = cls

        return cls

    def __getitem__(cls, key: str) -> 'StepMeta':
        if key not in cls.steps:
            raise StepDoesntExistError(f'There is no step with such type: {key}')
        return cls.steps[key]