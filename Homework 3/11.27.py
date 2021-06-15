#Dan Doan 1986920
import datetime
x = datetime.datetime.now()
x = (x.strftime("%B %d, %Y"))
print(x)
correct_dates = []
months2num = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7,
          'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
test = "March 1, 1990"
with open("inputDates.txt") as text:
    for line in text:
        for x in months:
            if line.find(x) !=(-1) and line.find(",") !=(-1):
                correct_dates.append(line)
print(correct_dates)
