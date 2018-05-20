import unittest
from fizzbuzz import fizzbuzz, fizzbuzz_without_if_nathan, fizzbuzz_without_if_rayan

class TestCase(unittest.TestCase):
    def test_fizzbuzz_1(self):
        self.assertEqual(fizzbuzz(1), '1')
        self.assertEqual(fizzbuzz_without_if_nathan(1), '1')
        self.assertEqual(fizzbuzz_without_if_rayan(1), '1')

    def test_fizzbuzz_3(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz_without_if_nathan(3), 'Fizz')
        self.assertEqual(fizzbuzz_without_if_rayan(3), 'Fizz')

    def test_fizzbuzz_5(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz_without_if_nathan(5), 'Buzz')
        self.assertEqual(fizzbuzz_without_if_rayan(5), 'Buzz')
    
    def test_fizzbuzz_15(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz_without_if_nathan(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz_without_if_rayan(15), 'FizzBuzz')
