from homeworks.homework9.task2 import SupressorAsClass, supressor


def test_SupressorAsClass_with_error():
    with SupressorAsClass(IndexError):
        [][1]


def test_SupressorAsClass_without_error():
    with SupressorAsClass(IndexError):
        [1][2]


def test_supressor_with_error():
    with supressor(IndexError):
        [][1]


def test_supressor_without_error():
    with supressor(IndexError):
        [][1]
