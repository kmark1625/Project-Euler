def main():
  print num_circular_primes(1000000)

def num_circular_primes(max_num):
  count = 0
  for i in range(1,max_num):
    if is_circular_prime(i):
      count += 1
  return count

def is_circular_prime(num):
  circular = True
  rotations = circular_rotations(num)
  for num in rotations:
    if not is_prime(num):
      circular = False
      break;
  return circular


def circular_rotations(num):
  rotations = []
  rotations.append(num)
  string_num = str(num)
  for i in range(1, len(string_num)):
    last_char = string_num[-1]
    string_num = string_num[:-1]
    string_num = last_char + string_num
    rotations.append(int(string_num))
  return rotations


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

def test_circular_rotations():
  assert circular_rotations(197) == [197, 719, 971]
  assert circular_rotations(2193) == [2193, 3219, 9321, 1932]

def test_is_circular_prime():
  assert is_circular_prime(197) == True
  assert is_circular_prime(3) == True
  assert is_circular_prime(37) == True
  assert is_circular_prime(19) == False

def test_num_circular_primes():
  assert num_circular_primes(100) == 13

def test():
  test_is_prime()
  test_circular_rotations()
  test_is_circular_prime()
  test_num_circular_primes()

if __name__ == '__main__':
  test()
  main()