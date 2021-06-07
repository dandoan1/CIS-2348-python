# Dan Doan 1986920
from datetime import date
import math

month, day, year = input("Please enter the current month, day and year with spacing between:").split()
bdmonth, bdday, bdyear = input("Please enter your birthday with the same format as above:").split()

dates = (date(int(year), int(month), int(day)) - date(int(bdyear), int(bdmonth), int(bdday)))

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
if bdday == day and bdmonth == month:
    print("Happy Birthday!")
else:
    pass
