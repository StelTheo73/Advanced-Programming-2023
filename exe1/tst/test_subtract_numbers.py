import unittest
from unittest.mock import patch

from src.subtract_numbers import subtract_numbers

class TestSubtractNumbers(unittest.TestCase):

    @patch("builtins.print")
    def test_positive_result(self, mock_print):
        subtract_numbers(1, 5)
        mock_print.assert_called_once_with("NEGATIVE")

    @patch("builtins.print")
    def test_negative_result(self, mock_print):
        subtract_numbers(5, 1)
        mock_print.assert_called_once_with("POSITIVE")

if __name__ == '__main__':
    unittest.main()
