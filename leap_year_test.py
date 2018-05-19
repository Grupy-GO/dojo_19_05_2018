import unittest
from leap_year import is_leap_year

class TestCase(unittest.TestCase):
    def test_1996(self):
        self.assertTrue(is_leap_year(1996))

    def test_2001(self):
        self.assertFalse(is_leap_year(2001))

    def test_1900(self):
        self.assertFalse(is_leap_year(1900))

    def test_2000(self):
        self.assertTrue(is_leap_year(2000))
