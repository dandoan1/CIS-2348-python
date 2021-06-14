#Dan Doan 1986920
given = input()
mylist = []
num = ""
for x in given:
    if x != " ":
        num+=x
    else:
        mylist.append(num)
        num = ""
mylist.append(num)
newlist = []
for x in mylist:
    if int(x) >= 0:
        newlist.append(int(x))
newlist.sort()
for x in newlist:
    print(x, end=" ")