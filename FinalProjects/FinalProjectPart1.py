# Dan Doan 1986920
import csv
from datetime import datetime


# class to make the dictionary for usage
class fullinventory:
    def __init__(self):
        self.main_dict = {}
        self.ID = ""
        self.manufacturer = ""
        self.item_type = ""
        self.price = ""
        self.service_date = ""
        self.damaged = ""

    # this def is to add the first csv to the dict
    def add_to_dict(self, ID="", manufacturer="", item_type="", price="", service_date="", damaged=""):
        self.main_dict[ID] = [ID, manufacturer, item_type, price, service_date, damaged]

    # this def adds prices to the dict
    def add_price(self, ID="", price=""):
        self.main_dict[ID][3] = price

    # this def add the date to the dict
    def add_date(self, ID="", date=""):
        self.main_dict[ID][4] = date


# calls the class and then open all the files
start = fullinventory()
with open("ManufacturerList.csv") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for x in lines:
        start.add_to_dict(ID=x[0], manufacturer=x[1], item_type=x[2], damaged=x[3])
with open("PriceList.csv") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for x in lines:
        start.add_price(x[0], x[1])
with open("ServiceDatesList.csv") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for x in lines:
        start.add_date(x[0], x[1])

# these blocks of code for fullinventory.csv
# get everyitem in the inventory list and then add them to the dictionary in the class
manufacturer_order_list = []
fullinventory_ordered_list = {}
# creating a list with the manufacturer ordered for usage
for x in start.main_dict:
    if start.main_dict[x][1] not in manufacturer_order_list:
        manufacturer_order_list.append(start.main_dict[x][1])
sorted_manufacturer_list = sorted(manufacturer_order_list)
# creating another dict ordered by manufacturer for usage
for manufacturer in sorted_manufacturer_list:
    for x in start.main_dict:
        if manufacturer == start.main_dict[x][1]:
            fullinventory_ordered_list[x] = start.main_dict[x]
# writing out the csv file, no spacing between with all the required infos
with open("FullInventory.csv", "w", newline="") as csvfile:
    csvfile = csv.writer(csvfile)
    for x in fullinventory_ordered_list:
        csvfile.writerow(fullinventory_ordered_list[x])

# these blocks for item type inventory list
# making a type list and a ordered id list
type_list = []
id_list = []
for x in start.main_dict:
    if start.main_dict[x][2] not in type_list:
        type_list.append(start.main_dict[x][2])
for x in start.main_dict:
    if x not in id_list:
        id_list.append(int(x))
# sorting ID for usage
sorted_id_list = sorted(id_list)
# making a dict with no type in it for later usage
no_type_dict = {}
for x in fullinventory_ordered_list:
    no_type_dict[x] = fullinventory_ordered_list[x][:2] + fullinventory_ordered_list[x][3:]
# checks for type, create a csv file with the name
# then checks for id, if both matches they write it down into the csv file
for type in type_list:
    with open("{}Inventory.csv".format(type.capitalize()), "w", newline="") as csvfile:
        csvfile = csv.writer(csvfile)
        for id in sorted_id_list:
            for y in start.main_dict:
                if type == start.main_dict[y][2] and str(id) == y:
                    csvfile.writerow(no_type_dict[y])

# these blocks for pastservicedatelist
# making a list with all the dates
dates_list = []
for x in start.main_dict:
    if start.main_dict[x][4] not in dates_list:
        dates_list.append(start.main_dict[x][4])
# using datetime to get todays date and then format it to the correct version
today = datetime.today()
d1 = today.strftime("%m/%d/%Y")
if d1[0] == "0":
    d1 = d1.replace("0", "", 1)
m1, d1, y1 = d1.split("/")
# making date1 for later comparison
date1 = datetime(int(y1), int(m1), int(d1))
# sorting the date by using datetime string to time conversion
# keylambda is something i googled since i did not know how to do this
dates_list.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
# making a past services date list, adding date into the list if it is in the past
past_service_dates = []
for dates in dates_list:
    m2, d2, y2 = dates.split("/")
    date2 = datetime(int(y2), int(m2), int(d2))
    if date1 > date2:
        past_service_dates.append(dates)
# opening and writing new lines into a file if the date matches the pastservicedate list above
with open("PastServiceDateInventory.csv", "w", newline="") as csvfile:
    csvfile = csv.writer(csvfile)
    for dates in past_service_dates:
        for x in start.main_dict:
            if dates == start.main_dict[x][4]:
                csvfile.writerow(start.main_dict[x])
# these blocks here for damagedlist.csv
# making a list with all the prices, someitems will have same prices which only one will be appended
prices_list = []
for x in start.main_dict:
    if start.main_dict[x][3] not in prices_list:
        prices_list.append(int(start.main_dict[x][3]))
# sorting prices low to high
prices_list.sort()
# check if it is "damaged" and prices have to match the sorted list, then writes them into the file
with open("DamagedInventory.csv", "w", newline="") as csvfile:
    csvfile = csv.writer(csvfile)
    for prices in prices_list:
        for x in start.main_dict:
            if str(prices) == start.main_dict[x][3] and start.main_dict[x][-1] == "damaged":
                csvfile.writerow(start.main_dict[x][0:-1])
