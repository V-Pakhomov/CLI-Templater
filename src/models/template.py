from pathlib import Path
from typing import List

import yaml

from .template_components.base import BaseTemplateComponent
from config import Config
from exceptions.templates import TemplateDoesntExistError
from .template_components import Step, Variable


class Template(BaseTemplateComponent):
    def __init__(
        self,
        name: str,
        description: str,
        steps: List[Step],
        variables: List[Variable],
    ):
        self.name = name
        self.description = description
        self.variables = variables
        self.steps = steps

    def apply(self):
        pass

    @classmethod
    def by_name(cls, template_name: str) -> 'Template':
        script_path = Path(Config.templates_dir, template_name, 'script.yaml')

        if not script_path.exists():
            raise TemplateDoesntExistError

        with open(script_path) as f:
            return cls.by_dict(yaml.safe_load(f))

    @classmethod
    def by_dict(cls, data: dict) -> 'Template':
        # TODO add keyerror checking
        name = data['name']
        description = data.get('description', '')

        variables_data = data.get('variables', dict())
        variables = [Variable.by_dict({'name': name} | vd) for name, vd in variables_data.items()]

        steps_data = data.get('steps', dict())
        steps = [Step.by_dict(sd) for sd in steps_data]

        return Template(name=name, description=description, variables=variables, steps=steps)

    def to_dict(self) -> dict:
        # TODO либо везде списки либо везде дикты
        return {
            'name': self.name,
            'description': self.description,
            'variables': [v.to_dict() for v in self.variables],
            'steps': [s.to_dict() for s in self.steps],
        }

    def is_valid(self) -> bool:
        raise NotImplementedError
