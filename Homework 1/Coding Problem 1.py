# Dan Doan 1986920

from datetime import date
import math

# splitting up the date into separate variables for printing usage later
month, day, year = input("Please enter the current month, day and year with spacing between:").split()
bdmonth, bdday, bdyear = input("Please enter your birthday with the same format as above:").split()
# setting up dates differences
dates = (date(int(year), int(month), int(day)) - date(int(bdyear), int(bdmonth), int(bdday)))
# printing infos
print("\nBirthday Calculator")
print("Current day")
print("Month:", month)
print("Day:", day)
print("Year:", year)
print("Birthday")
print("Month:", bdmonth)
print("Day:", bdday)
print("Year:", bdyear)
print("You are", math.floor(dates.days / 365), "years old.")
# saying hbd if it is their birtday (month and day matches)
if bdday == day and bdmonth == month:
    print("Happy Birthday!")
else:
    pass
