# Dan Doan 1986920
# getting given and list for usage
given = input()
mylist = []
# num string for usage
num = ""
# taking input and making them into a list
for x in given:
    if x != " ":
        num += x
    else:
        mylist.append(num)
        num = ""
mylist.append(num)
# new list for non negative num
newlist = []
for x in mylist:
    if int(x) >= 0:
        newlist.append(int(x))
# sorting smallest to biggest
newlist.sort()
# printing out results with spacing
for x in newlist:
    print(x, end=" ")
