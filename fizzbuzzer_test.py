import unittest

from fizzbuzzer import Fizzbuzzer

class TestFizzBuzzer(unittest.TestCase) :

    def setUp(self) :
        self.fizzbuzzer = Fizzbuzzer()

    class TestEvaluate(unittest.TestCase) :

        def test_evaluate_output_for_3(self):
            """
            When given a number divisible by 3 it returns Fizz
            """
            self.assertEqual(self.fizzbuzzer.evaluate(3), "Fizz")

        def test_evaluate_output_for_5(self):
            """
            When given a number divisible by 5 it returns Buzz
            """
            self.assertEqual(self.fizzbuzzer.evaluate(5), "Buzz")

        def test_evaluate_output_for_6(self):
            """
            When given a number divisible by 3 but not 3 it returns Fizz
            """
            self.assertEqual(self.fizzbuzzer.evaluate(6), "Fizz")

        def test_evaluate_output_for_10(self):
            """
            When given a number divisible by 5 but not 5 it returns Buzz
            """
            self.assertEqual(self.fizzbuzzer.evaluate(10), "Buzz")

        def test_evaluate_output_for_15(self):
            """
            When given a number divisible by 5 and 3 it returns Fizzbuzz
            """
            self.assertEqual(self.fizzbuzzer.evaluate(15), "Fizzbuzz")

        def test_evaluate_output_for_nondivisible_number(self):
            """
            When given a number not divisible by 5 or 3 it returns the number
            """
            self.assertEqual(self.fizzbuzzer.evaluate(2), 2)

if __name__ == '__main__':
    unittest.main()
