def main():
  gen = get_fib()
  counter = 3
  while True:
    fib_num = str(next(gen))
    if len(fib_num) == 1000:
      return counter
    counter += 1

def get_fib():
  a = 1
  b = 1
  while True:
    c = a + b
    a = b
    b = c
    yield c

def test():
  print "Hello World!"

if __name__ == '__main__':
  test()
  print main()