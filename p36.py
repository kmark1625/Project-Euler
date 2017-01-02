def main():
  sum = 0
  for i in range (1, 1000000):
    if is_double_base_palindrome(i):
      sum += i
  print sum

def is_double_base_palindrome(num):
  if is_palindrome(num) and is_palindrome(dec_to_binary(num)):
    return True
  else:
    return False

def dec_to_binary(num):
  return int(bin(num)[2:])

def is_palindrome(num):
  palindrome = True
  string_num = str(num)
  left_index = 0
  right_index = len(string_num) - 1
  while left_index < right_index:
    if string_num[left_index] != string_num[right_index]:
      palindrome = False
      break
    left_index += 1
    right_index -= 1
  return palindrome

def test_is_palindrome():
  assert is_palindrome(585) == True
  assert is_palindrome(1001001001) == True
  assert is_palindrome(58) == False
  assert is_palindrome(55) == True

def test_dec_to_binary():
  assert dec_to_binary(585) == 1001001001

def test_is_double_base_palindrome():
  assert is_double_base_palindrome(585) == True

def test():
  test_is_palindrome()
  test_dec_to_binary()
  test_is_double_base_palindrome()

if __name__ == '__main__':
  test()
  main()