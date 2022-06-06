import unittest

class TestFizzBuzz(unittest.TestCase):
  def test_returns_fizz_for_three_multiples(self):
    self.assertEqual(FizzBuzz.fb(3), "Fizz")
