import re

import pytest

from mimesis import config
from mimesis.builtins import USASpecProvider
from mimesis.enums import Gender
from mimesis.exceptions import (UndefinedField, UndefinedSchema,
                                UnsupportedField)
from mimesis.schema import Field, Schema

from .test_providers import patterns

# def test_str(_):
#     assert re.match(patterns.STR_REGEX, str(_))


@pytest.mark.parametrize(
    'locale', config.LIST_OF_LOCALES,
)
def test_field(locale):
    filed = Field(locale)
    result = filed('full_name')
    assert result
    assert isinstance(result, str)

    with pytest.raises(UnsupportedField):
        filed('unsupported_field')

    with pytest.raises(UndefinedField):
        filed()


def test_field_with_custom_providers():
    field = Field(providers=[USASpecProvider])
    assert field('ssn')
    assert field('usa_provider.ssn')


@pytest.fixture
def _():
    return Field('en')


@pytest.fixture
def valid_schema(_):
    return lambda: {
        'id': _('uuid'),
        'name': _('word'),
        'version': _('version', key=str.lower, pre_release=True),
        'timestamp': _('timestamp'),
        'mime_type': _('mime_type'),
        'zip_code': _('postal_code'),
        'owner': {
            'email': _('email', key=str.lower),
            'token': _('token'),
            'creator': _('full_name', gender=Gender.FEMALE),
            'billing': {
                'ethereum_address': _('ethereum_address'),
            },
        },
        'defined_cls': {
            'title': _('person.title'),
            'title2': _('text.title'),
        },
    }


def test_fill(_, valid_schema):
    result = Schema(schema=valid_schema).create(iterations=2)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)

    with pytest.raises(UndefinedSchema):
        Schema(schema=None).create()  # type: ignore


def test_field_with_key(_):
    usual_result = _('age')
    assert isinstance(usual_result, int)

    result_on_key = _('age', key=lambda v: float(v))
    assert isinstance(result_on_key, float)
