#Dan Doan 1986920
import csv
def counter(list):
    dict = {}
    for items in list:
        if items not in dict:
            dict[items] = 1
        else:
            dict[items]+=1
    return dict
given = input()
list = []
with open(given) as text:
    for word in text:
        newword = ""
        for letters in word:
            if letters != ",":
                newword += letters
            else:
                list.append(newword)
                newword = ""
    list.append(newword)
list[-1]= list[-1].strip()
dict = (counter(list))
for each in dict:
    print(each, dict[each])