def main():
  sum = 0
  for i in range(1,100000):
    if is_factorial_sum(i):
      sum += i
  return sum

def is_factorial_sum(num):
  sum = 0
  string_num = str(num)
  if len(string_num) == 1:
    return False
  for d in string_num:
    sum += factorial(int(d))
  if sum == num:
    return True
  else:
    return False

def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n-1)

def test_factorial():
  assert factorial(5) == 120

def test_is_factorial_sum():
  assert is_factorial_sum(145) == True

def test():
  test_factorial()
  test_is_factorial_sum()

if __name__ == '__main__':
  test()
  print main()