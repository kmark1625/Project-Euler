def main():
  triagonal_array = [triangle(x) for x in range(1,1000000)]
  pentagonal_set = set()
  for i in range(1,1000000):
    val = pentagonal(i)
    pentagonal_set.add(val)
  hexagonal_set = set()
  for i in range(1,1000000):
    val = hexagonal(i)
    hexagonal_set.add(val)
  for i in range(285, 999999):
    print i
    if pentagonal_and_hexagonal(triagonal_array[i], pentagonal_set, hexagonal_set):
      print i
      print "FOUND!"
      print "Answer: " + str(triagonal_array[i])
      break
  print "Not found in this range"

def pentagonal_and_hexagonal(num, pentagonal_set, hexagonal_set):
  if num in pentagonal_set and num in hexagonal_set:
    return True
  else:
    return False

def triangle(n):
  return n*(n+1)/2

def pentagonal(n):
  return n*(3*n-1)/2

def hexagonal(n):
  return n*(2*n -1)

def test_triangle():
  assert triangle(1) == 1
  assert triangle(2) == 3
  assert triangle(3) == 6
  assert triangle(4) == 10
  assert triangle(5) == 15

def test_pentagonal():
  assert pentagonal(1) == 1
  assert pentagonal(2) == 5
  assert pentagonal(3) == 12
  assert pentagonal(4) == 22
  assert pentagonal(5) == 35

def test_hexagonal():
  assert hexagonal(1) == 1
  assert hexagonal(2) == 6
  assert hexagonal(3) == 15
  assert hexagonal(4) == 28
  assert hexagonal(5) == 45

def test_pentagonal_and_hexagonal():
  pass
  # assert pentagonal_and_hexagonal(40755) == True

def test():
  test_triangle()
  test_pentagonal()
  test_hexagonal()
  test_pentagonal_and_hexagonal()

if __name__ == '__main__':
  test()
  main()
