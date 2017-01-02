"""
Project Euler Problem 16
What is the sum of the digits of 2^1000
"""

"""Computes the sum of digits of 2^n"""
def sum_of_digits(n):
  number_to_sum = 2 ** n
  array_of_digits = list(str(number_to_sum))
  array_of_digits = map(string_to_int, array_of_digits)
  return reduce(sum_two_ints, array_of_digits)

def string_to_int(string):
  return int(string)

def sum_two_ints(a,b):
  return a + b

def test_sum_of_digits():
  assert sum_of_digits(15) == 26

if __name__ == '__main__':
  test_sum_of_digits()
  print sum_of_digits(1000)

