## Problem #19 - Counting Sundays ##
from math import floor

# 01 Jan 1900 was Monday

def number_of_days_in_month(month, year):
	if month == 4 or month == 6 or month == 9 or month == 11:
		return 30 #April4, June6, Sept9, Nov11
	elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return 31 #January1, March3, May5, July7, August8, October10, December12
	else:
		if year % 4 == 0:
			if year % 100 == 0:
				if year % 400:
					return 29
				else:
					return 28
			else:
				return 29
		else:
			return 28	

# in 1900 (non leap), there were 52 weeks + 1 day (365 days)
# Since Jan/01/1900 was Monday, we can say Jan/01/1901 was Tuesday

days = 2
sundays_on_first = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		days += number_of_days_in_month(month, year) #first day of the next month
		if days % 7 == 0: #then it's Sunday
			sundays_on_first += 1

if days % 7 == 0: #in case the day after the last day is Sunday
	sundays_on_first -= 1
print sundays_on_first
