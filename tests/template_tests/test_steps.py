import pytest

from models.template_components import Step
from exceptions.steps import StepClassCreationError, StepDoesntExistError


def test_new_step_without_type():
    with pytest.raises(StepClassCreationError, match='You cant create step without type'):
        type('NewStep', (Step,), {})

def test_new_step_with_repeated_type():
    type('NewStep', (Step,), {'type': 'step'})
    assert True
    with pytest.raises(StepClassCreationError, match='Step with same type already exists: step'):
        type('AnotherNewStep', (Step,), {'type': 'step'})

def test_step_getattr():
    s = type('AttrStep', (Step,), {'type': 'attr_test'})
    assert Step['attr_test'] is s

def test_get_non_existed_step():
    with pytest.raises(StepDoesntExistError, match='There is no step with such type: nonexistingtype'):
        Step['nonexistingtype']
