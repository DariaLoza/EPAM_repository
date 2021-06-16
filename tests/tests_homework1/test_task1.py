from homeworks.homework2.task1 import *


def test_get_longest_diverse_words():
    """Testing that function find 10 longest words"""
    assert get_longest_diverse_words("homeworks/homework2/data.txt") == [
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
    assert count_punctuation_chars("homeworks/homework2/data.txt") == 5305


def test_get_rarest_char():
    """Testing that function find rarest symbol for document"""
    assert get_rarest_char("homeworks/homework2/data.txt") == ")"


def test_count_non_ascii_chars():
    """Testing that function count every non ascii char"""
    assert count_non_ascii_chars("homeworks/homework2/data.txt") == 2972


def test_get_most_common_non_ascii_char():
    """Testing that function find most common non ascii char"""
    assert get_most_common_non_ascii_char("homeworks/homework2/data.txt") == "ä"
