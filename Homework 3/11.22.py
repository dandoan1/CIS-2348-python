#Dan Doan 1986920
given = input()
mylist = []
word = ""
for x in given:
    if x != " ":
        word+=x
    else:
        mylist.append(word)
        word = ""
mylist.append(word)
mydict = {}
for x in mylist:
    if x not in mydict:
        mydict[x]=1
    else:
        mydict[x]+=1
for x in mylist:
    if x in mydict:
        print(x, mydict[x])