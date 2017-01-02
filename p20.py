def factorial(n):
  if n == 0:
    return 1
  return n*factorial(n-1)

def test_factorial():
  assert factorial(5) == 120
  assert factorial(10) == 3628800

def sum_of_digits(n):
  number_to_sum = n
  array_of_digits = list(str(number_to_sum))
  array_of_digits = map(string_to_int, array_of_digits)
  return reduce(sum_two_ints, array_of_digits)

def string_to_int(string):
  return int(string)

def sum_two_ints(a,b):
  return a + b

def test_sum_of_digits():
  assert sum_of_digits(3628800) == 27

if __name__=='__main__':
  test_factorial()
  test_sum_of_digits()
  number_factorial = factorial(100)
  print sum_of_digits(number_factorial)
