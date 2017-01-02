def main(n):
  sum = 1
  current_num = 1
  for i in range(1, n/2+1):
    for p in range(1,5): # 4 times
      current_num += i*2
      sum += current_num
  return sum


def test():
  assert main(5) == 101

if __name__ == '__main__':
  test()
  print main(1001)