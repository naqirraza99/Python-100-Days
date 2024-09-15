print("------------------------Lesson 10 Day 3 Leap Year ------------------")
year = int(input())

# Determine if the given year is a leap year based on the following conditions:
# 1. A year is a leap year if it is divisible by 400.
# 2. A year is also a leap year if it is divisible by 4 but not divisible by 100.
# 3. If the year does not meet either of these conditions, it is not a leap year.

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not Leap Year")
