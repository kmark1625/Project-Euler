import itertools

def pythagorean_generator():
	#Generates a pythagorean triplet
	sets = itertools.combinations(range(500),3)
	while True:
		a, b, c = next(sets)
		if (a**2 + b**2 == c**2):
			yield (a,b,c)

def find_1000():
	a,b,c=0,0,0
	sets = pythagorean_generator()
	while (a+b+c) < 2000:
		a,b,c = next(sets)
		print a,b,c
		if (a+b+c) == 1000:
			yield (a,b,c)


if __name__ == '__main__':
	a,b,c = next(find_1000())
	print "The answer is: %i, %i, %i" % (a,b,c)
	print "a*b*c = %i" % (a*b*c)

