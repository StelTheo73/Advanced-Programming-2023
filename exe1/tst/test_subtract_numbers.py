""" Unittest for subtract_numbers. """

import unittest
from unittest.mock import patch, call

from src.subtract_numbers import subtract_numbers, main

class TestSubtractNumbers(unittest.TestCase):

    @patch("builtins.print")
    def test_positive_result(self, mock_print):
        """ Test positive result. """
        subtract_numbers(1, 5)
        mock_print.assert_called_once_with("NEGATIVE")

    @patch("builtins.print")
    def test_negative_result(self, mock_print):
        """ Test negatove result. """
        subtract_numbers(5, 1)
        mock_print.assert_called_once_with("POSITIVE")

    @patch("builtins.print")
    def test_zero_result(self, mock_print):
        """ Test zero result. """
        subtract_numbers(5, 5)
        mock_print.assert_called_once_with("ZERO")

    @patch("src.subtract_numbers.subtract_numbers")
    @patch("builtins.input", side_effect=[5, 4, "y"])
    @patch("builtins.print")
    def test_main(self, mock_print, mock_input, mock_subtract_numbers):
        """ Test main. """
        main()
        mock_subtract_numbers.assert_called_with(5, 4)
        mock_print.assert_called_once_with("Quitting...")

    @patch("builtins.input", side_effect=["foo", 0, 0, "y"])
    @patch("builtins.print")
    def test_main_exception(self, mock_print, mock_input):
        """ Test that exception is raised when an invalid number is given. """
        main()
        mock_print.assert_has_calls([
            call("Invalid input. Please enter a number."),
            call("ZERO"),
            call("Quitting...")
        ])

    @patch("builtins.input", side_effect=[0, 0, "n", 0, 0, "y"])
    @patch("builtins.print")
    def test_exit(self, mock_print, mock_input):
        """ Test that program terminates in "y" is given. """
        main()

        mock_print.assert_has_calls([
            call("ZERO"),
            call("ZERO"),
            call("Quitting..."),
        ])

if __name__ == '__main__':
    unittest.main()

# Coverage --> Run from exe1 folder :
# $ coverage run -m unittest ./tst/test_subtract_numbers.py
# $ coverage report -m
# $ coverage html
