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