import unittest
from balance_parentheses import balanced_parentheses

class TestCase(unittest.TestCase):

    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_one(self):
        self.assertFalse(balanced_parentheses('{{)(}}'))

    def test_two(self):
        self.assertFalse(balanced_parentheses('({)}'))

    def test_three(self):
        self.assertTrue(balanced_parentheses('[({})]'))

    def test_four(self):
        self.assertTrue(balanced_parentheses('{}([])'))
    
    def test_five(self):
        self.assertTrue(balanced_parentheses('{()}[[{}]]'))

    def test_six(self):
        self.assertTrue(balanced_parentheses('(xˆ2)ˆ(yˆˆ3)'))
