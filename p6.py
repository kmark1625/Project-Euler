def sumOfSquares(n):
	result = 0
	for i in range(1, n+1):
		result += i**2
	print "The sum of squares of %i is %i" % (n, result)
	return result

def squareOfSums(n):
	result = 0
	for i in range(1, n+1):
		result += i
	result = result**2
	print "The square of the sums of %i is %i" % (n, result)
	return result

def diffOfSum(n):
	return abs(sumOfSquares(n) - squareOfSums(n))

if __name__ == '__main__':
	input = int(raw_input("Please enter a number: "))
	print "The difference between the sum of squares and square of sums is %i" % diffOfSum(input)


