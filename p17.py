"""
Project Euler Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

"""Translates a number to the english equivalent"""
ONES_DIGITS = {
  0: "",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine"
  }

TEENS = {
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen"
}

TWO_DIGITS = {
  1: "ten",
  2: "twenty",
  3: "thirty",
  4: "forty",
  5: "fifty",
  6: "sixty",
  7: "seventy",
  8: "eighty",
  9: "ninety"
}

def count_main():
  count = 0
  for i in range(1, 1001):
    word = num_to_word(i)
    count += count_letters(word)
  return count

"""Counts the number of letters in a word excluding - or spaces"""
def count_letters(word):
  return len(word) - word.count(' ') - word.count('-')

"""Returns the nth digit of a number.  Example the 3rd digit of 123 is 3."""
def nth_digit(num, n):
  num_as_string = str(num)
  return int(num_as_string[n-1])

def num_to_word(num):
  word = ""
  while num > 0:
    if num == 1000:
      word += "one thousand"
      num -= 1000
    elif num > 100:
      threes_digit = nth_digit(num, 1)
      word += ONES_DIGITS[threes_digit] + " hundred"
      num -= threes_digit*100
    elif num == 100:
      word += "one hundred"
      num -= 100
    elif num > 19:
      twos_digit = nth_digit(num, 1)
      if word.count("hundred") > 0:
        word += " and "
      word += TWO_DIGITS[twos_digit]
      num -= twos_digit*10
    elif num >= 10:
      if word.count("hundred") > 0:
        word += " and "
      word += TEENS[num]
      num -= num
    elif num > 0:
      if word.count('ty') > 0:
        word += "-"
      if word.count('hundred') > 0 and word.count('ty') == 0:
        word += " and "
      word += ONES_DIGITS[num]
      num -= num
  return word



def test_nth_digit():
  assert nth_digit(123, 1) == 1
  assert nth_digit(123, 2) == 2
  assert nth_digit(123, 3) == 3

def test_num_to_word():
  assert num_to_word(1) == "one"
  assert num_to_word(2) == "two"
  assert num_to_word(10) == "ten"
  assert num_to_word(11) == "eleven"
  assert num_to_word(15) == "fifteen"
  assert num_to_word(20) == 'twenty'
  assert num_to_word(23) == 'twenty-three'
  assert num_to_word(32) == 'thirty-two'
  assert num_to_word(81) == 'eighty-one'
  assert num_to_word(101) == 'one hundred and one'
  assert num_to_word(111) == 'one hundred and eleven'
  assert num_to_word(151) == 'one hundred and fifty-one'
  assert num_to_word(218) == 'two hundred and eighteen'
  assert num_to_word(323) == 'three hundred and twenty-three'
  assert num_to_word(832) == 'eight hundred and thirty-two'
  assert num_to_word(1000) == 'one thousand'

def test_count_letters():
  assert count_letters("one") == 3
  assert count_letters("twenty-three") == 11
  assert count_letters("one hundred and fifteen") == 20
  assert count_letters("three hundred ") == 12
  assert count_letters("three hundred and forty-two") == 23
  assert count_letters("one thousand") == 11

if __name__== '__main__':
  test_nth_digit()
  test_num_to_word()
  test_count_letters()
  print count_main()