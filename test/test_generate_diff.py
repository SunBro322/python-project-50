import pytest
from gendiff.generate_diff import generate_diff


def test_generate_diff_json():
    assert generate_diff('file1.json', 'file2.json') == \
           '''{
    "- follow": false,
    "host": "hexlet.io",
    "- proxy": "123.234.53.22",
    "- timeout": 50,
    "+ timeout": 20,
    "+ verbose": true
}'''
