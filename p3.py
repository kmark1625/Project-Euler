def isPrime(n):
	"""Determines whether a number is prime"""
	prime = True
	for i in range(2, n/2 + 1):
		if (n % i == 0):
			prime = False
	return prime

def largestPrimeFactor(n):
	"""Determines the largest prime factor"""
	largest=1
	target = n
	i = 2
	while i < target:
		if (n % i == 0):
			target = n / i
			print "Target = %r" % target
			if isPrime(i):
				largest=i
				print "Current largest: %r" % largest
		i += 1
	return "The largest prime is: %r" % largest

if __name__ == '__main__':
	print largestPrimeFactor(600851475143)
