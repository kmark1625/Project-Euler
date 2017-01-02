import p3

"""
Problem 7 Project Euler
What is the 10,001st prime number?
"""
# Pseudo-code
"""
nthPrime(number)
Declare a variable to hold the current list of primes.
Declare a variable to hold the size of the list of primes.
Declare a variable to hold current number
WHILE count is less than 10001
  Call isPrime on the number and pass list of current primes

isPrime(number, current primes)
  IF number is equal to 2 its prime
  Otherwise, check if the number is evenly divisible by any of the previous primes
"""


def nthPrime(bound):
  list_primes = []
  current_number=1
  while len(list_primes) < bound:
    current_number +=1
    if isPrime(current_number, list_primes):
      list_primes.append(current_number)
  return current_number

def isPrime(number, list_primes=[]):
  if number == 2:
    return True
  else:
    for prime in list_primes:
      if number % prime == 0:
        return False
    return True

def testNthPrime():
  assert nthPrime(5) == 11
  assert nthPrime(6) == 13

if __name__ == '__main__':
  testNthPrime()
  print nthPrime(10001)
