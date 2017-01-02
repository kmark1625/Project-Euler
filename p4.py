def isPalindrome(n):
	"""Takes in an integer and determines whether it is a palindrome"""
	n = str(n)
	length = len(n)
	increment = 0
	isPalindrome = True
	# well written loop
	while increment < length/2 and isPalindrome:
		if n[increment] == n[length - 1 - increment]:
			increment +=1
		else:
			isPalindrome = False
	return isPalindrome

def largestPalindrome():
	"""Finds the largest palindrome made from the product of two 3-digit num	bers"""
	largest = 0
	for i in range(999, 100, -1):
		for j in range(i, 100, -1):
			if (isPalindrome(i*j) and i*j > largest):
				largest = i*j
	return largest


# Test cases for isPalindrome
def testPalindrome():
	assert isPalindrome(505) == True
	assert isPalindrome(50) == False
	assert isPalindrome(5) == True
	assert isPalindrome(2002) == True

# Test cases for largest Palindrome
def testLargestPalindrome():
	assert largestPalindrome() == 906609

if __name__ == '__main__':
	testPalindrome()
	testLargestPalindrome()
	print  largestPalindrome()
