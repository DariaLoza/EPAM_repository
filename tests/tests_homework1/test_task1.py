import homeworks.homework2.task1


def test_get_longest_diverse_words():
    """Testing that function find 10 longest words consisting from largest amount of unique symbols"""
    assert homeworks.homework2.task1.get_longest_diverse_words("data.txt") == [
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
    assert homeworks.homework2.task1.count_punctuation_chars("tests/tests_homework1/data.txt") == 5305


def test_get_rarest_char():
    """Testing that function find rarest symbol for document"""
    assert homeworks.homework2.task1.get_rarest_char("tests/tests_homework1/data.txt") == ")"


def test_count_non_ascii_chars():
    """Testing that function count every non ascii char"""
    assert homeworks.homework2.task1.count_non_ascii_chars("tests/tests_homework1/data.txt") == 2972


def test_get_most_common_non_ascii_char():
    """Testing that function find most common non ascii char for document"""
    assert homeworks.homework2.task1.get_most_common_non_ascii_char("tests/tests_homework1/data.txt") == "ä"
