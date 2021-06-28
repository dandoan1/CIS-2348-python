# Dan Doan 1986920

# most of these are the same as the zybooks examples, i just changed some variables name to my liking to make it
# more understandable for me
# i do know how the code works but it'll probably take me a whole week to code it out by myself

# make num call global variable to print for later
num_calls = 0


# main partition function
def partition(user_ids, i, k):
    # get the middle ID
    mid_id = i + (k - i) // 2
    # name it the pivot
    pivot = user_ids[mid_id]
    # set low and high as given by the call
    low = i
    high = k
    while True:
        # check that the low element is "less" than the pivot
        # if true then it will add one into low, which in turn would ignore the the low
        # because later low will be swapped (if its not actually lower than pivot)
        while user_ids[low] < pivot:
            low = low + 1
        # same thing but checks for high instead, if pivot is less than the high element,
        # it will ignore, otherwise it will be used to swap later
        while pivot < user_ids[high]:
            high = high - 1
        # will stop the loop if low is somehow equals or bigger than high(would only happen in the later runs)
        if low >= high:
            break
        # this else statement will swaps the element inside the user_id list, using the low and high, like i said before
        # it will only swap if its "false" based on the two while statement up top if that make sense
        else:
            temp = user_ids[low]
            user_ids[low] = user_ids[high]
            user_ids[high] = temp
            low = low + 1
            high = high - 1
    # return the high element to quicksort for usage
    return high


def quicksort(user_ids, i, k):
    # call to use global numcalls for requirement
    global num_calls
    num_calls += 1
    # checks that low is not the same as high, if yes it return the list (mostly for later to check if the list is done)
    if i >= k:
        return
    # call on partition to sort the initial list, then make the high element into x
    x = partition(user_ids, i, k)
    # call on this quicksort again, but with a new high element every time until the i=> k statement is true
    # for sorting the "low" part of the list by calling partition and changing the high element everytime
    quicksort(user_ids, i, x)
    # call on this function again, but for the "high" part of the list this time
    quicksort(user_ids, x + 1, k)
    return


if __name__ == "__main__":
    # sorting userid to correct format
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    # Initial call to quicksort, with base low as 0 and high as the list -1 because of given "-1"
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort, global from before
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
