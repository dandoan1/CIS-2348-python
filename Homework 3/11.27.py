# Dan Doan 1986920
# def print menu for calling many times later
def printmenu():
    print("""\nMENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit
""")


# function for getting the input choices, then doing whichever action the user pick
# looping back to menu after, q to break the loop
def choice():
    printmenu()
    chosen = input("Choose an option:\n")
    while True:
        if chosen not in "aduroq":
            chosen = input("Choose an option:\n")
        if chosen == "q":
            break
        if chosen == "a":
            jer6 = input("Enter a new player's jersey number:")
            rate6 = input("Enter the player's rating:")
            iniroster[int(jer6)] = int(rate6)
            orderlist.append(int(jer6))
            orderlist.sort()
            printmenu()
            chosen = input("Choose an option:\n")
        if chosen == "o":
            print("\nROSTER")
            for y in orderlist:
                print("Jersey number: {}, Rating: {}".format(y, iniroster[y]))
            printmenu()
            chosen = input("Choose an option:\n")
        if chosen == "d":
            delete = input("Enter a jersey number:")
            iniroster.pop(int(delete))
            orderlist.remove(int(delete))
            printmenu()
            chosen = input("Choose an option:\n")
        if chosen == "u":
            num = input("Enter a jersey number:")
            newrate = input("Enter a new rating for player:")
            iniroster[int(num)] = int(newrate)
            printmenu()
            chosen = input("Choose an option:\n")
        if chosen == "r":
            rating = input("Enter a rating:\n")
            print("ABOVE {}".format(rating))
            for y in orderlist:
                if iniroster[y] > int(rating):
                    print("Jersey number: {}, Rating: {}".format(y, iniroster[y]))
            printmenu()
            chosen = input("Choose an option:\n")


# making the initial roster with the given 10 input
iniroster = {}
jer1 = int(input("Enter player 1's jersey number:\n"))
rate1 = int(input("Enter player 1's rating:\n"))
jer2 = int(input("\nEnter player 2's jersey number:\n"))
rate2 = int(input("Enter player 2's rating:\n"))
jer3 = int(input("\nEnter player 3's jersey number:\n"))
rate3 = int(input("Enter player 3's rating:\n"))
jer4 = int(input("\nEnter player 4's jersey number:\n"))
rate4 = int(input("Enter player 4's rating:\n"))
jer5 = int(input("\nEnter player 5's jersey number:\n"))
rate5 = int(input("Enter player 5's rating:\n"))
iniroster[jer1] = rate1
iniroster[jer2] = rate2
iniroster[jer3] = rate3
iniroster[jer4] = rate4
iniroster[jer5] = rate5
# making a list with the jersey number for ordering later
orderlist = []
for x in iniroster:
    orderlist.append(x)
orderlist.sort()
# printing out initial roster
print("\nROSTER")
for x in orderlist:
    print("Jersey number: {}, Rating: {}".format(x, iniroster[x]))
# calling main function
choice()
