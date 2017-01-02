def sumOfEvenFib(n):
	"""Solves for sum of even numbers in the fibbonaci sequence less than n"""
	fib = [1,2]
	counter = 1
	sum = 2
	go = True
	while go:
		counter += 1
		candidate = fib[counter-2] + fib[counter-1]
		if candidate < n:
			fib.append(candidate)
			if candidate % 2 ==0:
				sum += candidate
		else:
			go = False
	return sum

# Refactor by adding generator function to create fibbonaci sequence


def test_cases():
	assert sumOfEvenFib(4000000) == 4613732

if __name__ == '__main__':
	test_cases()
	print sumOfEvenFib(4000000)