# Dan Doan 1986920
# input and list for usage
given = input()
mylist = []
word = ""
# making a list with input for usage
for x in given:
    if x != " ":
        word += x
    else:
        mylist.append(word)
        word = ""
mylist.append(word)
mydict = {}
# making a dict and then adding word from list into dict, if word is already there, increment by 1
for x in mylist:
    if x not in mydict:
        mydict[x] = 1
    else:
        mydict[x] += 1
# printing results
for x in mylist:
    if x in mydict:
        print(x, mydict[x])
