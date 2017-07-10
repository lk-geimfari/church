# -*- coding: utf-8 -*-
import json
import re

import pytest

from ._patterns import STR_REGEX


def test_str(structured):
    assert re.match(STR_REGEX, str(structured))


def test_css(structured):
    result = structured.css()
    assert isinstance(result, str)  # returns string
    assert ':' in result  # contains property assignments
    assert result[-1] == '}'  # closed at end
    assert result.split(' ')[1][0] == '{'  # opened after selector


def test_css_property(structured):
    result = structured.css_property()
    assert len(result.split(' ')) == 2  # contains one property assignment
    assert ':' in result  # contains any property assignments


def test_html_attribute_value(structured):
    result = structured.html_attribute_value('a', 'href')
    assert result[0:4] == 'http'
    with pytest.raises(NotImplementedError):
        structured.html_attribute_value('a', 'bogus')


def test_html(structured):
    result = structured.html()
    assert result[0] == '<'  # tag is enclosed
    assert result[-1] == '>'  # tag is enclosed


def depth(x):
    """Calculates depth of object."""
    if isinstance(x, dict) and x:
        return 1 + max(depth(x[a]) for a in x)
    if isinstance(x, list) and x:
        return 1 + max(depth(a) for a in x)
    return 0


def test_json(structured):
    result = structured.json(items=3, max_depth=4)
    assert isinstance(result, str)  # returns str
    data = json.loads(result)  # is valid JSON
    assert isinstance(data, (dict, list))  # root element is container
    assert len(data) == 3  # root container has three items
    r = structured.json(items=3, max_depth=4, _recursive=True)
    assert depth(r) <= 4  # maximum depth of three elements
