# -*- coding: utf-8 -*-
import re

from elizabeth.core.intd import CURRENCY, CURRENCY_SYMBOLS
from tests.test_data import business, generic

from ._patterns import STR_REGEX


def test_str(business):
    assert re.match(STR_REGEX, str(business))


def test_copyright(business):
    result = business.copyright()
    assert '©' in result
    assert result is not None

    result_1 = business.copyright(date=False)
    assert '©' in result
    assert result_1 is not None

    result_args = business.copyright(minimum=1999, maximum=2010)
    date = result_args.split()[1].split('-')
    assert int(date[0]) >= 1999
    assert int(date[1]) <= 2010


def test_currency_sio(business):
    result = business.currency_iso()
    assert result in CURRENCY


def test_company_type(generic):
    result = generic.business.company_type()
    assert result in generic.business.data['company']['type']['title']

    result_2 = generic.business.company_type(abbr=True)
    assert result_2 in generic.business.data['company']['type']['abbr']


def test_company(generic):
    result = generic.business.company()
    assert result in generic.business.data['company']['name']


def test_price(generic):
    currencies  = CURRENCY_SYMBOLS[generic.business.locale]
    result = generic.business.price(minimum=100.00, maximum=1999.99)
    price, symbol = result.split(' ')
    assert float(price) >= 100.00
    assert float(price) <= 2000
    assert symbol in currencies
