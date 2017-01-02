import itertools

def main():
  array = list(itertools.permutations("0123456789", 10))
  array.sort()
  return array[999999]

def test():
  print "Hello World!"

if __name__ == '__main__':
  test()
  print main()