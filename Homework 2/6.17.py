# Dan Doan 1986920
# dict with good keys and def for usage
key = {"i": "!", "a": "@", "m": "M", "B": "8", "o": "."}


# checking if a letter matches a key then it returns the swapped letter or the normal letter if not swapped
def checker(letter):
    for x in key:
        if letter == x:
            return key[x]
    return letter


# calls on checker and then append whichever comes back
def modifier(password):
    word = ""
    for x in password:
        word += checker(x)
    print(word + "q*s")


# get input and modifier will print out result
given = input()
modifier(given)
