from exceptions.base import CliTemplaterError


class TemplateError(CliTemplaterError):
    ...


class TemplateDoesntExistError(TemplateError):
    ...
