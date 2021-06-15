# Dan Doan 1986920
# getting dates and making sure its in the right format
import datetime

currentdate = datetime.datetime.now()
currentdate = (currentdate.strftime("%m %d, %Y"))
currentdate = currentdate.replace(",", "")
currentdate = currentdate.replace(" ", "/")
# removing first 0 of the month if they have it
if currentdate[0] == "0":
    currentdate = currentdate.replace("0", "", 1)
else:
    pass
# making present date for comparison
m1, d1, y1 = currentdate.split("/")
date1 = datetime.datetime(int(y1), int(m1), int(d1))
# two list for usage
correct_dates = []
finaldates = []
# dict and list for usage
months2num = {'January': "1", 'February': "2", 'March': "3", 'April': "4", 'May': "5", 'June': "6", 'July': "7",
              'August': "8", 'September': "9", 'October': "10", 'November': "11", 'December': "12"}
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
# open file,read, and if found full month and a comma then it will append to a list
with open("inputDates.txt") as text:
    for line in text:
        for x in months:
            if line.find(x) != (-1) and line.find(",") != (-1):
                e = line.replace(x, months2num[x])
                correct_dates.append(e)
# making correct format and then finally comparing the dates before adding the final solutions to the final list
for x in correct_dates:
    y = x.replace(",", "")
    z = y.replace(" ", "/")
    m2, d2, y2 = z.split("/")
    date2 = datetime.datetime(int(y2), int(m2), int(d2))
    if date2 < date1:
        finaldates.append(z)
# correct solutions are now in finaldates list
# appending correct dates to parsedDates.txt, will not remove any previous dates
for i in finaldates:
    f = open("parsedDates.txt", "a")
    f.write(i)
    f.close()
