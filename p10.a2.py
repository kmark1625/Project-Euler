from math import *
from time import *

"""
Problem 10
==========

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
  
   Answer: d915b2a9ac8749a6b837404815f1ae25

"""
def isPrime(num):
	"""Returns True if a number is prime, otherwise returns False"""
	if num == 2: return True
	elif num%2==0: return False
	else:
		for i in range(3,int(sqrt(num)+1)):
			if num%i==0:
				return False
		return True
t1=time()
print isPrime(1999999)
t2=time()
print t2-t1, "seconds"
