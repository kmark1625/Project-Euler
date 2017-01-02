def main():
  pentagonal_set = create_pentagonal_set()
  for num in pentagonal_set:
    print num
  if 6 in pentagonal_set:
    print "This is true"
  min_d = 900000
  for i in range(1,1000):
    for j in range(1,1000):
      sum_numbers = pentagonal(i) + pentagonal(j)
      dif = D(pentagonal(i), pentagonal(j))
      if is_pentagonal(sum_numbers, pentagonal_set) and is_pentagonal(dif, pentagonal_set) and dif < min_d:
        min_d = dif
        print sum_numbers
        print "Is True? " + str(is_pentagonal(sum_numbers, pentagonal_set))
        if sum_numbers in pentagonal_set:
          print "This is true"
        print i, j
        print pentagonal(i), pentagonal(j)
        print dif
  print "Answer: " + str(min_d)

def D(num_1, num_2):
  return abs(num_2 - num_1)

def is_pentagonal(num, pentagonal_set):
  if num in pentagonal_set:
    return True
  else:
    return False

def pentagonal(n):
  return n*(3*n-1)/2

def create_pentagonal_set():
  pentagonal_set = set()
  for i in range(1, 1000):
    val = pentagonal(i)
    pentagonal_set.add(val)
  return pentagonal_set

def test_pentagonal():
  assert pentagonal(1) == 1
  assert pentagonal(2) == 5
  assert pentagonal(3) == 12
  assert pentagonal(4) == 22
  assert pentagonal(5) == 35

def test_is_pentagonal():
  pentagonal_set = create_pentagonal_set()
  assert is_pentagonal(4, pentagonal_set) == True
  assert is_pentagonal(7, pentagonal_set) == True

def test():
  test_pentagonal()
  # test_is_pentagonal()

if __name__ == '__main__':
  test()
  main()