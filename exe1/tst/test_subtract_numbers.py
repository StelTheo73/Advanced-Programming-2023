import unittest
from unittest.mock import patch, call

from src.subtract_numbers import subtract_numbers, main

class TestSubtractNumbers(unittest.TestCase):

    @patch("builtins.print")
    def test_positive_result(self, mock_print):
        subtract_numbers(1, 5)
        mock_print.assert_called_once_with("NEGATIVE")

    @patch("builtins.print")
    def test_negative_result(self, mock_print):
        subtract_numbers(5, 1)
        mock_print.assert_called_once_with("POSITIVE")

    @patch("builtins.print")
    def test_zero_result(self, mock_print):
        subtract_numbers(5, 5)
        mock_print.assert_called_once_with("ZERO")

    @patch("src.subtract_numbers.subtract_numbers")
    @patch("builtins.input", side_effect=[5, 4, "y"])
    @patch("builtins.print")
    def test_main(self, mock_print, mock_input, mock_subtract_numbers):
        main()
        mock_subtract_numbers.assert_called_with(5, 4)
        mock_print.assert_called_once_with("Quiting...")

    @patch("builtins.input", side_effect=["foo", 0, 0, "y"])
    @patch("builtins.print")
    def test_main_exception(self, mock_print, mock_input):
        main()
        mock_print.assert_has_calls([
            call("Invalid input. Please enter a number."),
            call("ZERO"),
            call("Quiting...")
        ])

    @patch("builtins.input", side_effect=[0, 0, "n", 0, 0, "y"])
    @patch("builtins.print")
    def test_exit(self, mock_print, mock_input):
        main()

        mock_print.assert_has_calls([
            call("ZERO"),
            call("ZERO"),
            call("Quiting..."),
        ])

if __name__ == '__main__':
    unittest.main()
