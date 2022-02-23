from homeworks.homework2.task1 import *

file_path = "tests/tests_homework1/data.txt"


def test_get_longest_diverse_words():
    """Testing that function find 10 longest words"""
    assert get_longest_diverse_words(file_path) == [
        "Nichtkämpfern",
        "Entscheidungsschlacht",
        "Schöpfungsmacht",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "politisch-strategischen",
        "Selbstverständlich",
        "résistance-Bewegungen",
        "unmißverständliche",
        "Bevölkerungsabschub",
    ]


def test_count_punctuation_chars():
    """Testing that function count every punctuation char"""
    assert count_punctuation_chars(file_path) == 5305


def test_get_rarest_char():
    """Testing that function find rarest symbol for document"""
    assert get_rarest_char(file_path) == ")"


def test_count_non_ascii_chars():
    """Testing that function count every non ascii char"""
    assert count_non_ascii_chars(file_path) == 2972


def test_get_most_common_non_ascii_char():
    """Testing that function find most common non ascii char"""
    assert get_most_common_non_ascii_char(file_path) == "ä"
