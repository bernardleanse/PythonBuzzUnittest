from errno import EILSEQ


class FizzBuzz:
  def run(self, num):
    result = ""
    if num % 3 == 0:
      result += "fizz"
    if num % 5 == 0:
      result += "buzz"
    if len(result) == 0:
      result = str(num)
    return result
      
