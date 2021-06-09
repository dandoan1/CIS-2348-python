#Dan Doan 1986920
key = {"i": "!", "a": "@", "m": "M", "B": "8", "o": "."}


def checker(letter):
    for x in key:
        if letter == x:
            return key[x]
    return letter


def modifier(password):
    word = ""
    for x in password:
        word += checker(x)
    print(word + "q*s")


given = input()
modifier(given)
