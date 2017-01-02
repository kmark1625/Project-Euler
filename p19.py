"""Solves problem 19 of Project Euler"""
""" How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000) """
"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
"""

# Pseudo-code
"""
Set the first day of of the month of year 1900 to a Monday.
Iterate through 1900 to 2000 and add it to a counter variable if the first day of the month is a Sunday.
"""

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class Year:
  def __init__(self, year):
    self.count = 0
    self.year = year
    self.leap_year = self.is_leap_year()

  def is_leap_year(self):
    return ( (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0 )

  def setup_months(self, first_day_of_year):
    self.months = [Month(x) for x in MONTHS]
    first_day = first_day_of_year
    for month in self.months:
      month.set_first_day_of_month(first_day)
      first_day = DAYS[(DAYS.index(month.get_last_day_of_month()) + 1) % 7]

  def count_first_sundays(self):
    for month in self.months:
      if month.first_day_of_month == "Sunday":
        self.count += 1


class Month:
  def __init__(self, name, leap_year = False):
    self.name = name
    self.leap_year = leap_year
    self.number_of_days = self.determine_number_of_days()

  def determine_number_of_days(self):
    number_of_days = 31
    if self.name == "September" or self.name == "April" or self.name == "June" or self.name == "November":
      number_of_days = 30
    if self.name == "February":
      number_of_days = 28
    if self.name == "February" and self.leap_year:
      number_of_days = 29
    return number_of_days

  def set_first_day_of_month(self, day):
    self.first_day_of_month = day

  def get_last_day_of_month(self):
    first_day_index = DAYS.index(self.first_day_of_month)
    last_day_index = (first_day_index + (self.number_of_days - 1))% 7
    return DAYS[last_day_index]

def driver():
  total_count = 0
  year = Year(1900)
  year.setup_months("Monday")
  first_day_of_year = DAYS[(DAYS.index(year.months[-1].get_last_day_of_month()) + 1) % 7]
  print first_day_of_year
  for i in range(1901, 2001):
    year = Year(i)
    year.setup_months(first_day_of_year)
    year.count_first_sundays()
    total_count += year.count
    first_day_of_year = DAYS[(DAYS.index(year.months[-1].get_last_day_of_month()) + 1) % 7]
  return total_count



def test_leap_year():
  assert Year(2000).leap_year == True
  assert Year(2400).leap_year == True
  assert Year(1800).leap_year == False
  assert Year(1900).leap_year == False
  assert Year(2100).leap_year == False
  assert Year(2004).leap_year == True
  assert Year(2001).leap_year == False

def test_days_in_a_month():
  assert Month("January").number_of_days == 31
  assert Month("February").number_of_days == 28
  assert Month("February", True).number_of_days == 29
  assert Month("March").number_of_days == 31
  assert Month("April").number_of_days == 30
  assert Month("May").number_of_days == 31
  assert Month("June").number_of_days == 30
  assert Month("July").number_of_days == 31
  assert Month("August").number_of_days == 31
  assert Month("September").number_of_days == 30
  assert Month("October").number_of_days == 31
  assert Month("November").number_of_days == 30
  assert Month("December").number_of_days == 31

def test_last_day_of_month():
  month = Month("December")
  month.set_first_day_of_month("Tuesday")
  assert month.get_last_day_of_month() == "Thursday"
  month = Month("January")
  month.set_first_day_of_month("Friday")
  assert month.get_last_day_of_month() == "Sunday"

if __name__ == '__main__':
  test_leap_year()
  test_days_in_a_month()
  test_last_day_of_month()
  print driver()