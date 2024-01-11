from abc import abstractmethod

from .step_meta import StepMeta
from .step_types import StepTypes
from ..base import BaseTemplateComponent


class Step(BaseTemplateComponent, metaclass=StepMeta):
    type: str = ''

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @classmethod
    def by_dict(cls, data: dict) -> 'Step':
        step_type = data['type']

        try:
            return Step[step]
        except:
            raise
