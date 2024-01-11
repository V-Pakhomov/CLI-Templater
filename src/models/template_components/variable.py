from typing import Optional

from .base import BaseTemplateComponent


class Variable(BaseTemplateComponent):
    def __init__(self, name: str, default_value: Optional[str], required: bool) -> None:
        self.name = name
        self.default_value = default_value
        self.required = required
        self.value: Optional[str] = None

    def set_value(self, value: Optional[str]) -> None:
        self.value = value or self.default_value

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'default_value': self.default_value,
            'required': self.required,
        }

    @classmethod
    def by_dict(cls, data: dict) -> 'Variable':
        return Variable(
            name=data['name'],
            default_value=data.get('default_value'),
            required=data.get('required', False),
        )

    def is_valid(self) -> bool:
        raise NotImplementedError