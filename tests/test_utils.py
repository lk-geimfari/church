# -*- coding: utf-8 -*-

import os

import pytest

from mimesis.exceptions import UnsupportedLocale
from mimesis.utils import (download_image, locale_info, luhn_checksum, pull,
                           setup_locale, update_dict)


def test_luhn_checksum():
    assert luhn_checksum('7992739871') == '3'


def test_pull():
    data = pull('person.json', 'en')

    assert data['views_on'] is not None
    assert isinstance(data['views_on'], list)
    with pytest.raises(UnsupportedLocale):
        pull('personal.json', 'w')
    with pytest.raises(FileNotFoundError):
        pull('something.json', 'en')

    data = pull('address.json', 'en-gb')
    assert 'city' in data
    assert 'Aberystwyth' in data['city']
    assert 'Addison' not in data['city']

    data = pull('address.json', 'en-au')
    assert 'city' in data
    assert 'Melbourne' in data['city']


@pytest.mark.parametrize(
    'ctx', [
        False,
        True,
    ],
)
def test_download_image(ctx):
    url = 'https://raw.githubusercontent.com/lk-geimfari/' \
          'mimesis/master/media/logo.png'

    verified = download_image(url=url, unverified_ctx=ctx)
    assert verified == 'logo.png'
    os.remove(verified)

    result = download_image('', unverified_ctx=ctx)
    assert result is None


def test_locale_information():
    result = locale_info(locale='ru')
    assert result == 'Russian'

    result_1 = locale_info(locale='is')
    assert result_1 == 'Icelandic'
    with pytest.raises(UnsupportedLocale):
        locale_info(locale='w')


def test_update_dict():
    first = {
        'animals': {
            'dogs': [
                'spaniel',
            ],
        },
    }
    second = {
        'animals': {
            'cats': [
                'maine coon',
            ],
        },
    }

    result = update_dict(first, second)

    assert 'cats' in result['animals']
    assert 'dogs' in result['animals']

    third = {
        'animals': {
            'dogs': [
                'golden retriever',
            ],
        },
    }

    result = update_dict(first, third)
    assert 'spaniel' not in result['animals']['dogs']


@pytest.mark.parametrize(
    'inp, out', [
        ('EN', 'en'),
        ('DE', 'de'),
        ('RU', 'ru'),
    ],
)
def test_setup_locale(inp, out):
    result = setup_locale(inp)
    assert result == out


def test_setup_locale_exception():
    with pytest.raises(UnsupportedLocale):
        setup_locale('nil')
