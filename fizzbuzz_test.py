import unittest
from fizzbuzz import fizzbuzz

class TestCase(unittest.TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, False)