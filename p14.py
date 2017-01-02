"""Solves Problem 14 of Project Euler"""
""" Less than one million, which has longest chain?"""
"""
   n = n/2 (n is even)
   n = 3n + 1 (n is odd)
"""
LIMIT = 1000000

def greatest():
  number_with_longest_chain = 0
  longest_chain = 0
  i = 1
  while i < LIMIT:
    current_chain = iterative_chain(i)
    if current_chain > longest_chain:
      longest_chain = current_chain
      number_with_longest_chain = i
    i += 1
  return number_with_longest_chain

def iterative_chain(n):
  if n == 1: # Base case
    return 1
  if n%2 == 0:
    return 1 + iterative_chain(n/2)
  else:
    return 1 + iterative_chain(3*n + 1)
  end

def test_iterative_chain():
  assert iterative_chain(1) == 1
  assert iterative_chain(13) == 10
  print "test_iterative_chain passes"

if __name__ == '__main__':
  test_iterative_chain()
  print greatest()
