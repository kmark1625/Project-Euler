def main():
  seq = set()
  for a in range(2,101):
    for b in range(2,101):
      seq.add(a**b)
  return len(seq)


def test():
  print "Hello World!"

if __name__ == '__main__':
  test()
  print main()