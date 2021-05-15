from unittest import TestCase

import mock
from homeworks.homework4.task2 import count_dots_on_i


def test_count_dots_on_i_without_monkey_patch():
    """Testing test_count_dots_on_i without monkey patch"""
    assert count_dots_on_i("https://example.com/") == 59


class FetchTests(TestCase):
    def test_count_dots_on_i_with_monkey_patch(self):
        """Testing test_count_dots_on_i with monkey patch"""
        with mock.patch("urllib.request.urlopen") as mock_request:
            url = "smith"

            mock_request.return_value.response = "Avicii"

            self.assertTrue(self, count_dots_on_i(url) == 3)

    def test_count_dots_no_i_with_monkey_patch(self):
        """Testing test_count_dots_on_i without i"""
        with mock.patch("urllib.request.urlopen") as mock_request:
            url = "smith"

            mock_request.return_value.response = "Dasha"

            self.assertTrue(self, count_dots_on_i(url) == 0)
