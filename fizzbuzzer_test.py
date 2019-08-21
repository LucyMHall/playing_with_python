import unittest

from fizzbuzzer import Fizzbuzzer

class TestFizzBuzzer(unittest.TestCase) :
    def test_fizz_output_for_3(self):
        """
        When given a number divisible by 3 it returns Fizz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(3)
        self.assertEqual(result, "Fizz")

    def test_buzz_output_for_5(self):
        """
        When given a number divisible by 5 it returns Buzz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(5)
        self.assertEqual(result, "Buzz")
    def test_fizz_output_for_6(self):
        """
        When given a number divisible by 3 but not 3 it returns Fizz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(6)
        self.assertEqual(result, "Fizz")
    def test_buzz_output_for_10(self):
        """
        When given a number divisible by 5 but not 5 it returns Buzz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(10)
        self.assertEqual(result, "Buzz")
    def test_fizzbuzz_output_for_15(self):
        """
        When given a number divisible by 5 and 3 it returns Fizzbuzz
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(15)
        self.assertEqual(result, "Fizzbuzz")
    def test_output_for_nondivisible_number(self):
        """
        When given a number not divisible by 5 or 3 it returns the number
        """
        fizzbuzzer = Fizzbuzzer()
        result = fizzbuzzer.evaluate(2)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
