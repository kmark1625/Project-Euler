from math import *
from time import *

# Solves problem 12 of Project Euler
def triangle(num):
	"""Returns a list of length num of triangle numbers"""
	result = []
	total = 0
	for i in range(1,num+1):
		total +=i
		result.append(total)
	return result

def triangle(num):
	# Continue until num divisors is > 500
	total = 0
	i = 1
	while True:
		total += i
		if num_divisors(total) > num:
			return total
		i += 1

def num_divisors(num):
	"""Returns the number of divisors num has.  Also takes in the current factor that 	  it is on"""
	list = []
	list.append(1)
	if num != 1 : list.append(num)
	if isPrime(num): return len(list)
	i = 2
	temp = num
	while i <= temp:
		if num % i == 0:
			list.append(i)
			if list.count(num/i) == 0: list.append(num/i)
		i += 1
		temp = int(num/i)
	return len(set(list))

def isPrime(num, list_primes=[2]):
	lastPrime = list_primes[-1]
	if num == 2: return True
	elif num % 2 == 0: return False
	else:
		for i in list_primes:
			if i > sqrt(num): break
			if num%i==0: return False
		for i in range(lastPrime,int(sqrt(num))+1):
			if num%i==0: return False
		return True

def test_num_divisors():
	assert num_divisors(1) == 1
	assert num_divisors(2) == 2
	assert num_divisors(3) == 2
	assert num_divisors(4) == 3
	assert num_divisors(5) == 2
	assert num_divisors(6) == 4
	assert num_divisors(10000) == 25
	print "test_num_divisors passes"

def test_primes():
	assert isPrime(2) == True
	assert isPrime(4) == False
	assert isPrime(5) == True
	assert isPrime(15) == False
	assert isPrime(17) == True
	print "test_primes passes"

print triangle(500)