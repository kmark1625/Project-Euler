import primes

def main():
  for i in range(3, 10000):
    if not primes.is_prime(i):
      has_goldbach()

def has_goldbach(num):
  pass

def test_has_goldbach():
  assert has_goldbach(9) == True
  assert has_goldbach(15) == True
  assert has_goldbach(21) == True
  assert has_goldbach(25) == True
  assert has_goldbach(27) == True
  assert has_goldbach(33) == True

def test():
  test_has_goldbach()

if __name__ == '__main__':
  test()
  main()