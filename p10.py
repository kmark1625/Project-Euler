"""
Problem 10
==========

   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

   Find the sum of all the primes below two million.
  
   Answer: d915b2a9ac8749a6b837404815f1ae25

"""
from math import *
import time

# Solution to problem 10 of Project Euler
"""
Pseudo-code for isPrime():
if 2: return True
if divisible by 2: return True
else:
	loop through list of primes:
		return false if divisible
	loop through remaining numbers:
		return false if divisible
	return True
"""

def gen_prime():
	list_primes = [2]
	num = 3 # Placeholder
	while True:
		if isPrime(num, list_primes):
				list_primes.append(num)
				yield num
		num += 2

def isPrime(num, list_primes=[2]):
	lastPrime = list_primes[-1]
	if num == 2: return True
	elif num % 2 == 0: return False
	else:
		for i in list_primes:
			if i > sqrt(num): break
			if num%i==0: return False
		for i in range(lastPrime,int(sqrt(num))+1,2):
			if num%i==0: return False
		return True

def sum_of_primes():
	sum = 2
	primes = gen_prime()
	i = next(primes)
	while i < 2000000:
		sum += i
		i = next(primes)
	return sum
"""
	assert isPrime(2) == True
	assert isPrime(3) == True
	assert isPrime(4) == False
	assert isPrime(5) == True
	assert isPrime(9) == False
	assert isPrime(25) == False
	assert isPrime(29) == True
	print "test_isPrime passes"
"""

t1 = time.time()
print "Sum of Primes is %i" % sum_of_primes()
t2 = time.time()
print "Time : %r" % (t2-t1)
print isPrime(15)
