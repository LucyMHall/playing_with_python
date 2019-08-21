import unittest

from fizzbuzzer import Fizzbuzzer

class TestFizzBuzzer(unittest.TestCase) :
    def test_fizz_output(self):
        """
        Test that when given a number divisible by 3 it returns Fizz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(3)
        self.assertEqual(result, "Fizz")

if __name__ == '__main__':
    unittest.main()
