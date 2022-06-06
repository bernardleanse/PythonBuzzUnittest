import unittest
from fizz_buzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
  def test_returns_fizz_for_three(self):
    fizz_buzz = FizzBuzz()
    self.assertEqual(fizz_buzz.run(3), "fizz")

  def test_returns_fizz_for_nine(self):
    fizz_buzz = FizzBuzz()
    self.assertEqual(fizz_buzz.run(9), "fizz")

  def test_returns_buzz_for_five(self):
    fizz_buzz = FizzBuzz()
    self.assertEqual(fizz_buzz.run(5), "buzz")

  def test_returns_fizzbuzz_for_fifteen(self):
    fizz_buzz = FizzBuzz()
    self.assertEqual(fizz_buzz.run(15), "fizzbuzz")


