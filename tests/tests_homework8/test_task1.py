import pytest

from homeworks.homework8.task1 import KeyValueStorage


def test_KeyValueStorage_as_element():
    storage = KeyValueStorage("key_value_storage")
    assert storage["name"] == "kek"


def test_KeyValueStorage_as_attribute():
    storage = KeyValueStorage("key_value_storage")
    assert storage.song == "shadilay"
    assert storage.power == 9001


def test_KeyValueStorage_with_error():
    with pytest.raises(ValueError):
        assert KeyValueStorage("error_file")
