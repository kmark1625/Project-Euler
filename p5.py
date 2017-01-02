from fractions import gcd

def smallestDiv():
	"""Finds smallest number that is evenly divisible from 1 through 20"""
	return reduce(lambda x,y: lcm(x,y), range(1,21))

def lcm(a,b):
	return (a*b) / gcd(a,b)

if __name__ == '__main__':
	print smallestDiv()
