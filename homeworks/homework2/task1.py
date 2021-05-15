"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import OrderedDict
from typing import List

import nltk
from nltk import word_tokenize

nltk.download("punkt")


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        text_tokens = word_tokenize(text)
        d = {}

        for word in text_tokens:
            result = "".join(OrderedDict.fromkeys(word))
            d[result] = word

        longest_cases = sorted(d.keys(), key=len)[-11:-1]

        final = []
        for element in longest_cases:
            final.append(d[element])

        return final


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        punctuation_chars = string.punctuation
        count = 0

        for element in text:
            if element in punctuation_chars:
                count += 1
    return count


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        every_char = {}

        for element in text:
            if element in every_char:
                every_char[element] += 1
            else:
                every_char[element] = 1

    list_rarest_char = []
    for key, value in every_char.items():
        if value == 1:
            list_rarest_char.append(key)
    return list_rarest_char[-1]


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        count_char = 0

        for element in text:
            if not element.isascii():
                count_char += 1

    return count_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        non_ascii_dict = {}
        for element in text:
            if not element.isascii() and element in non_ascii_dict:
                non_ascii_dict[element] += 1
            else:
                non_ascii_dict[element] = 1

    list_non_ascii_dict = list(non_ascii_dict.items())
    list_non_ascii_dict.sort(key=lambda i: i[1])

    return str(list_non_ascii_dict[-1][0])
