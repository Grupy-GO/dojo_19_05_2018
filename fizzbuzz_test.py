import unittest
from fizzbuzz import fizzbuzz

class TestCase(unittest.TestCase):
    def test_fizzbuzz_1(self):
        self.assertEqual(fizzbuzz(1), '1')

    def test_fizzbuzz_3(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')

    def test_fizzbuzz_5(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
    
    def test_fizzbuzz_15(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
