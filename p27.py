def main():
  highest_consecutive = 0
  product_coefficients = 0
  for a in range(-999, 1000):
    for b in range(-999, 1000):
      current_consecutive = consecutive_primes(a,b)
      if current_consecutive > highest_consecutive:
        highest_consecutive = current_consecutive
        product_coefficients = a*b
  return product_coefficients


def consecutive_primes(a,b):
  '''Finds Consecutive primes of formula n**2 + a*n + b starting from n=0'''
  n = 0
  while True:
    quadratic = n**2 + a*n + b
    if not is_prime(quadratic):
      break
    n += 1
  return n

def is_prime(n):
  '''check if an integer n is prime'''
  n = abs(int(n))
  if n < 2:
    return False
  if n == 2:
    return True
  if not n & 1:
    return False
  for x in range(3, int(n**.5)+1, 2):
    if n % x == 0:
      return False
  return True

def test_is_prime():
   assert is_prime(2) == True
   assert is_prime(3) == True
   assert is_prime(4) == False
   assert is_prime(5) == True
   assert is_prime(6) == False
   assert is_prime(7) == True
   assert is_prime(8) == False
   assert is_prime(9) == False
   assert is_prime(10) == False
   assert is_prime(11) == True

def test_consecutive_primes():
  assert consecutive_primes(1, 41) == 40
  assert consecutive_primes(-79, 1601) == 80

def test():
  test_is_prime()
  test_consecutive_primes()

if __name__ == '__main__':
  test()
  print main()