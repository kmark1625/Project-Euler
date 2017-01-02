"""Solves problem 13 of Project Euler"""
#Pseudo-code
"""
Reads in input as an array of length 50 strings reversed.
Define a variable result to hold an array with the resulting number.
Define a variable for the carry over digit.
Define a variable to hold the sum.
LOOP through 50
  Set sum to sum of all numbers in ith position plus the carryover
  Push the modulus of 10 to the result.
  Set the carry over digit to the sum divided by 10.
  Reset the sum
LOOP until carry over divided by 10 is zero.
  Push the carry modulus 10 to the result.
  Divide the carry by 10.
Print out the first 10 digits of the resulting array.
"""
def sum_of_large():
  num_array = parse_input("p13.txt")
  result = []
  carry = sum_special(num_array, result)
  result = handle_carry(result, carry)
  return last_10(result)

def sum_special(num_array, result, digits=50):
  sum = 0
  carry = 0
  for i in range(digits):
    for num in num_array:
      sum = sum + int(num[i])
    sum += carry
    carry = 0
    result.append(sum % 10)
    carry = sum / 10
    sum = 0
  return carry

def parse_input(filename):
  """Takes in a file full of numbers and returns an array of each number reversed."""
  result = []
  f = open(filename, "r")
  for line in f:
    result.append(line.strip()[::-1])
  return result

def last_10(number_as_array):
  result = ""
  last_index = len(number_as_array)-1
  for i in range(last_index, last_index-10, -1):
    result += str(number_as_array[i])
  return int(result)

def handle_carry(array, carry):
  while carry != 0:
    array.append(carry % 10)
    carry = carry / 10
  return array

def tests():
  # Testing last_10()
  array1 = [0,9,8,7,6,5,4,3,2,1]
  array2 = [15,17,19,18,17,16,15,14,13,0,9,8,7,6,5,4,3,2,1]
  assert last_10(array1) == 1234567890
  assert last_10(array2) == 1234567890
  # Testing handle_carry()
  assert handle_carry([], 12) == [2, 1]
  assert handle_carry([], 123) == [3, 2, 1]
  assert handle_carry([], 78) == [8, 7]
  # Testing sum_special()
  num_array = ["52", "52", "22"] # Answer is 126
  test_sum = []
  print sum_special(num_array,test_sum, 2)
  print test_sum
  assert test_sum == [2, 7]
  print "Tests pass"

def do_i_update(array):
  array.append(5)
  return None

tests()
print sum_of_large()
