import os

import pytest
from homeworks.homework4.task1 import read_magic_number


def test_read_magic_number_true():
    """_Testing True result_"""
    test_file_1 = os.open("file_1.txt", os.O_CREAT | os.O_WRONLY)
    number = "2"
    encoded_number = str.encode(number)
    os.write(test_file_1, encoded_number)
    path = os.path.abspath("file_1.txt")
    assert read_magic_number(path)
    os.close(test_file_1)
    os.remove(path)


def test_read_magic_number_false():
    """_Testing False result_"""
    test_file_2 = os.open("file_2.txt", os.O_CREAT | os.O_WRONLY)
    number = "5"
    encoded_number = str.encode(number)
    os.write(test_file_2, encoded_number)
    path = os.path.abspath("file_2.txt")
    assert not read_magic_number(path)
    os.close(test_file_2)
    os.remove(path)


def test_read_magic_number_value_error():
    """_Testing ValueError result_"""
    test_file_3 = os.open("file_3.txt", os.O_CREAT | os.O_WRONLY)
    number = "t"
    encoded_number = str.encode(number)
    os.write(test_file_3, encoded_number)
    path = os.path.abspath("file_3.txt")
    with pytest.raises(ValueError):
        assert read_magic_number(path) == ValueError
    os.close(test_file_3)
    os.remove(path)
