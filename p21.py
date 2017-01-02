# Project Euler Problem 21

def main():
  # Loop through 1 to 10000 through i
    # Determine sum of proper divisors and store as variable.
    # If sum of proper divisors of variable equals i, increment sum
  sum = 0
  for i in range(1, 10000):
    candidate = sum_of_proper_divisors(i)
    if sum_of_proper_divisors(candidate) == i and candidate != i:
      sum += i
  return sum

def sum_of_proper_divisors(n):
  sum = 0
  for i in range(1,n):
    if n % i == 0:
      sum += i
  return sum

def tests():
  test_sum_of_proper_divisors()

def test_sum_of_proper_divisors():
  assert sum_of_proper_divisors(220) == 284
  assert sum_of_proper_divisors(284) == 220

if __name__ == '__main__':
  tests()
  print main()