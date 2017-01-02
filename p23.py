import itertools

def main():
  array_of_abundant = set()
  for i in range(1, 28124):
    if is_abundant(i):
      array_of_abundant.add(i)
  result_sum = 0
  print "checkpoint"

  for i in range(1, 28124):
    sum_found = False
    for abundant in array_of_abundant:
      if abundant > i:
        break
      complement = i - abundant
      if complement in array_of_abundant:
        sum_found = True
        break
      else:
        array_of_abundant.add(abundant)
    if not (sum_found):
      result_sum += i
      # print i
  return result_sum

def sum_of_proper_divisors(n):
  sum = 0
  for i in range(1,n):
    if n % i == 0:
      sum += i
  return sum

def is_abundant(n):
  return sum_of_proper_divisors(n) > n

def test():
  test_sum_of_proper_divisors()

def test_sum_of_proper_divisors():
  assert sum_of_proper_divisors(220) == 284
  assert sum_of_proper_divisors(284) == 220

if __name__ == '__main__':
  test()
  print main()