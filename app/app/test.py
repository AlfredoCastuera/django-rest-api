# flake8: noqa
"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """test subtracking numbers togheter"""
        res = calc.subtract(9, 6)
        self.assertEqual(res, 3)
