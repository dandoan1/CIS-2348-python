# Dan Doan 1986920
# did not use import csv since not needed here (for my method atleast)
# a counter with a dictionary to check for all words and adds one if there is already a match
def counter(mylist):
    mydict = {}
    for items in mylist:
        if items not in mydict:
            mydict[items] = 1
        else:
            mydict[items] += 1
    return mydict


# get input
given = input()
# list for usage
mylist2 = []
# opening the file and then adding words to the list everytime a comma is met
with open(given) as text:
    for word in text:
        newword = ""
        for letters in word:
            if letters != ",":
                newword += letters
            else:
                mylist2.append(newword)
                newword = ""
    mylist2.append(newword)
# stripping the \n from the last word
mylist2[-1] = mylist2[-1].strip()
# calling function on the list and then printing result
mydict2 = (counter(mylist2))
for each in mydict2:
    print(each, mydict2[each])
