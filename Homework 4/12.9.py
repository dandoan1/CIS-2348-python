# Dan Doan 1986920
# will make a list with continuous stream of input while the input is not "-1"
mylist = []
while True:
    e = input()
    if e != "-1":
        mylist.append(e)
    else:
        break
# making a new list with the given input from the list splitting up the spaces
newlist = []
for x in mylist:
    newlist.append((x.split(" ")))
# ask the machine to try and check if the second spot every single time is an interger, if it encounter an error
# it will set such error to "-1" for later usage
for x in newlist:
    try:
        x[1] = int(x[1])
    except:
        x[1] = "-1"
# printing the final newlist with the name, followed by the age/number incremented by one (reasons it turned into -1
# earlier and not 0)
for x in newlist:
    print(x[0], int(x[1]) + 1)
