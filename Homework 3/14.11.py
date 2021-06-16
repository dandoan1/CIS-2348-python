# Dan Doan 1986920
# first def will return the index of the nth biggest number in the list and then an unedited version of the given
# list
def indexnbiggest(count, givenlist):
    outputlist = []
    for i in givenlist:
        outputlist.append(i)
    for e in range(count):
        maxnum = max(givenlist)
        givenlist.remove(maxnum)
    maxnum = max(givenlist)
    index = outputlist.index(maxnum)
    return index, outputlist


# this def will find the largest number and its index, and will swap it with the nth position in the list
# then the nth position number will be swapped to the nth number index, then printing out the result
def selection_sort_descend_trace(givenlist1):
    thislist = []
    for e in givenlist1:
        thislist.append(e)
    counter = 0
    for i in range(len(thislist) - 1):
        index, newlist = indexnbiggest(counter, thislist)
        maxnum = newlist[index]
        maxnumlocation = newlist.index(maxnum)
        othernum = newlist[counter]
        newlist[counter] = maxnum
        newlist[maxnumlocation] = othernum
        thislist = newlist
        counter += 1
        # for x in thislist:
        # print(x, end="#)
        for o in thislist:
            print(o, end=" ")
        print()


if __name__ == "__main__":
    # this will get the input and then append the int version into a list for usage
    given = input()
    mylist = given.split(" ")
    otherlist = []
    for x in mylist:
        otherlist.append(int(x))
    selection_sort_descend_trace(otherlist)
