from abc import ABC, abstractmethod


class BaseTemplateComponent(ABC):
    @classmethod
    @abstractmethod
    def by_dict(cls, data: dict) -> "BaseTemplateComponent":
        ...

    @abstractmethod
    def to_dict(self) -> dict:
        ...

    @abstractmethod
    def is_valid(self) -> bool:
        ...
