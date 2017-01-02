def main():
  return sum_of_nth_sum(5)

def sum_of_nth_sum(n):
  sum = 0
  for i in range(1, 1000000):
    if is_valid_nth_sum(i, n):
      sum += i
  return sum

def is_valid_nth_sum(num, n):
  string_num = str(num)
  if len(string_num) == 1:
    return False
  sum = 0
  for d in string_num:
    sum += int(d)**n
  if sum == num:
    return True
  else:
    return False

def test_is_valid_nth_sum():
  assert is_valid_nth_sum(1634, 4) == True
  assert is_valid_nth_sum(8208, 4) == True
  assert is_valid_nth_sum(9474, 4) == True
  assert is_valid_nth_sum(1, 4) == False
  assert is_valid_nth_sum(9248, 4) == False

def test_sum_of_nth_sum():
  assert sum_of_nth_sum(4) == 19316

def test():
  test_is_valid_nth_sum()
  test_sum_of_nth_sum()

if __name__ == '__main__':
  print main()