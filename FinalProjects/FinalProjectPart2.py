# Dan Doan 1986920
import csv
from datetime import datetime


# class to make the dictionary for usage the same as part 1
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


# adding 2 def that returns either the correct item (first item that is wanted) or false
def returnhighestpriced(mydict, manufacturer):
    for key in mydict:
        if mydict[key][1] == manufacturer:
            return mydict[key]
    return False


# return the index of an item in the dictionary that was chosen based on the user input
def return2ndhighest(mydict, manufacturer):
    counter = 0
    for key in mydict:
        if mydict[key][1] == manufacturer:
            return counter
        else:
            counter += 1


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

# make inventory like part1
manufacturer_order_list = []
fullinventory_ordered_list = {}
for x in start.main_dict:
    if start.main_dict[x][1] not in manufacturer_order_list:
        manufacturer_order_list.append(start.main_dict[x][1])
sorted_manufacturer_list = sorted(manufacturer_order_list)
for manufacturer in sorted_manufacturer_list:
    for x in start.main_dict:
        if manufacturer == start.main_dict[x][1]:
            fullinventory_ordered_list[x] = start.main_dict[x]
# using datetime to remove any item that was expired
dates_list = []
for x in start.main_dict:
    if start.main_dict[x][4] not in dates_list:
        dates_list.append(start.main_dict[x][4])
today = datetime.today()
d1 = today.strftime("%m/%d/%Y")
if d1[0] == "0":
    d1 = d1.replace("0", "", 1)
m1, d1, y1 = d1.split("/")
date1 = datetime(int(y1), int(m1), int(d1))
dates_list.sort(key=lambda date: datetime.strptime(date, "%m/%d/%Y"))
past_service_dates = []
for dates in dates_list:
    m2, d2, y2 = dates.split("/")
    date2 = datetime(int(y2), int(m2), int(d2))
    if date1 > date2:
        past_service_dates.append(dates)
# deleting said items that was expired and/or damaged
for x in start.main_dict:
    if start.main_dict[x][4] in past_service_dates or start.main_dict[x][-1] == "damaged":
        del fullinventory_ordered_list[x]

# making a type list for usage and price list for usage
type_list = []
price_list = []
for x in fullinventory_ordered_list:
    if fullinventory_ordered_list[x][2] not in type_list:
        type_list.append(fullinventory_ordered_list[x][2])
for x in fullinventory_ordered_list:
    if x not in price_list:
        price_list.append(int(x))
sorted_price_list = sorted(price_list, reverse=True)
# making dictionaries for usage
price_ordered_list = {}
phone_list = {}
laptop_list = {}
tower_list = {}
# will enter all the nondamaged and nonexpired into the price ordered list in the correct price order (high to low)
for type in type_list:
    for id in sorted_price_list:
        for y in fullinventory_ordered_list:
            if type == fullinventory_ordered_list[y][2] and str(id) == y:
                price_ordered_list[y] = fullinventory_ordered_list[y]
# splitting up the items by type, inside it's ordered by price
for x in price_ordered_list:
    if price_ordered_list[x][2] == "phone":
        phone_list[x] = price_ordered_list[x]
    if price_ordered_list[x][2] == "laptop":
        laptop_list[x] = price_ordered_list[x]
    if price_ordered_list[x][2] == "tower":
        tower_list[x] = price_ordered_list[x]
# loops that breaks if q
while True:
    q = input("Enter the brand, follow by type with a space between, type q to quit:\n")
    if q == "q":
        break
    # search that input includes phone, laptop, or tower
    # then searches that atleast a manufacturer was given in the input also
    if q.find("phone") != (-1):
        for manufacturer in manufacturer_order_list:
            if q.find(manufacturer) != (-1):
                # if found, will run returnhighestprice to get the item with the highest price that matches the
                # manufacturer
                z = (returnhighestpriced(phone_list, manufacturer))
                # if false was return, there was no such item
                if not z:
                    print("\nNo such item in inventory\n")
                # else there was an item and then prints the result
                else:
                    print("\nYour item is: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(z[0], z[1], z[2], z[3]))
                # these try will make sure that there is an index+1 and index-1 exist if not nothing will be printed
                # if it does exist then it will print out the "may consider" line
                try:
                    index = return2ndhighest(phone_list, manufacturer)
                    a = list(phone_list.items())[index + 1]
                    # this line checks to make sure that the same manufacturer is not printed as a recommendation
                    # if it is the same manufacturer it raises an error which in turns print nothing
                    if a[1][1] == manufacturer:
                        raise ValueError
                    print("You may, also, consider: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(a[1][0], a[1][1],
                                                                                                      a[1][2], a[1][3]))
                except Exception:
                    pass
                try:
                    # same thing as the other try above
                    b = list(phone_list.items())[index - 1]
                    # make sure that it does not print the last item on the list if the first item matches the
                    # description of given
                    if index == 0:
                        raise ValueError
                    if b[1][1] == manufacturer:
                        raise ValueError
                    print("You may, also, consider: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(b[1][0], b[1][1],
                                                                                                      b[1][2], b[1][3]))
                except Exception:
                    pass
    # same as the above
    if q.find("laptop") != (-1):
        for manufacturer in manufacturer_order_list:
            if q.find(manufacturer) != (-1):
                z = (returnhighestpriced(laptop_list, manufacturer))
                if not z:
                    print("\nNo such item in inventory\n")
                else:
                    print("\nYour item is: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(z[0], z[1], z[2], z[3]))
                try:
                    index = return2ndhighest(laptop_list, manufacturer)
                    a = list(laptop_list.items())[index + 1]
                    if a[1][1] == manufacturer:
                        raise ValueError
                    print("You may, also, consider: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(a[1][0], a[1][1],
                                                                                                      a[1][2], a[1][3]))
                except Exception:
                    pass
                try:
                    b = list(laptop_list.items())[index - 1]
                    if index == 0:
                        raise ValueError
                    if b[1][1] == manufacturer:
                        raise ValueError
                    print("You may, also, consider: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(b[1][0], b[1][1],
                                                                                                      b[1][2], b[1][3]))
                except Exception:
                    pass
    # same as the above
    if q.find("tower") != (-1):
        for manufacturer in manufacturer_order_list:
            if q.find(manufacturer) != (-1):
                z = (returnhighestpriced(tower_list, manufacturer))
                if not z:
                    print("\nNo such item in inventory\n")
                else:
                    print("\nYour item is: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(z[0], z[1], z[2], z[3]))
                try:
                    index = return2ndhighest(tower_list, manufacturer)
                    a = list(tower_list.items())[index + 1]
                    if a[1][1] == manufacturer:
                        raise ValueError
                    print("You may, also, consider: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(a[1][0], a[1][1],
                                                                                                      a[1][2], a[1][3]))
                except Exception:
                    pass
                try:
                    b = list(tower_list.items())[index - 1]
                    if index == 0:
                        raise ValueError
                    if b[1][1] == manufacturer:
                        raise ValueError
                    print("You may, also, consider: ID= {}, Brand= {}, Type= {}, Price= ${}\n".format(b[1][0], b[1][1],
                                                                                                      b[1][2], b[1][3]))
                except Exception:
                    pass
