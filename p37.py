def main():
  sum = 0
  for i in range(1, 1000000):
    if is_truncatable_prime(i):
      sum += i
  print sum

def is_truncatable_prime(num):
  truncatable = True
  if len(str(num)) == 1:
    return False
  left_truncations = left_truncate(num)
  right_truncations = right_truncate(num)
  truncations = left_truncations + right_truncations
  for num in truncations:
    if not is_prime(num):
      truncatable = False
      break
  return truncatable

def left_truncate(num):
  string_num = str(num)
  truncations = [num]
  for i in range(1, len(string_num)):
    string_num = string_num[1:]
    truncations.append(int(string_num))
  return truncations

def right_truncate(num):
  string_num = str(num)
  truncations = [num]
  for i in range(1, len(string_num)):
    string_num = string_num[:-1]
    truncations.append(int(string_num))
  return truncations

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

def test_left_truncate():
  assert left_truncate(3797) == [3797, 797, 97, 7]

def test_right_truncate():
  assert right_truncate(3797) == [3797, 379, 37, 3]

def test_is_truncatable_prime():
  assert is_truncatable_prime(3797) == True

def test():
  test_is_prime()
  test_left_truncate()
  test_right_truncate()
  test_is_truncatable_prime()

if __name__ == '__main__':
  test()
  main()