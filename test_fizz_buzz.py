import unittest
from fizz_buzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
  def test_returns_fizz_for_three(self):
    fizz_buzz = FizzBuzz()
    self.assertEqual(fizz_buzz.run(3), "fizz")
