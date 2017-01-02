def main():
  highest = 0
  for i in range(1, 10000000):
    if is_pandigital_prime(i):
      highest = i
  print highest

def is_pandigital_prime(num):
  if is_prime(num) and is_pandigital(num):
    return True
  else:
    return False

def is_pandigital(num):
  string_num = str(num)
  length = len(string_num)
  digits = set()
  for i in range(1, length + 1):
    digits.add(i)
  digits_num = set()
  for d in string_num:
    digits_num.add(int(d))
  if length == len(digits) and digits == digits_num:
    return True
  else:
    return False

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

def test_is_pandigital():
  assert is_pandigital(2143) == True

def test_is_pandigital_prime():
  assert is_pandigital_prime(2143) == True

def test():
  test_is_prime()
  test_is_pandigital()
  test_is_pandigital_prime()

if __name__ == '__main__':
  test()
  main()