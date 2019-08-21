import unittest

from fizzbuzzer import Fizzbuzzer

class TestFizzBuzzer(unittest.TestCase) :
    def test_fizz_output_for_3(self):
        """
        Test that when given a number divisible by 3 it returns Fizz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(3)
        self.assertEqual(result, "Fizz")

    def test_buzz_output_for_5(self):
        """
        Test that when given a number divisible by 5 it returns Buzz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(5)
        self.assertEqual(result, "Buzz")
    def test_fizz_output_for_6(self):
        """
        Test that when given a number divisible by 3 but not 3 it returns Fizz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(6)
        self.assertEqual(result, "Fizz")

if __name__ == '__main__':
    unittest.main()
