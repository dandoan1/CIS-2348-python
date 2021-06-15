# Dan Doan 1986920
# will check for spaces, return the word(s) without spaces
def removal(main_word):
    newword = ""
    for x in main_word:
        if x == " ":
            pass
        else:
            newword += x
    return newword


# check from front to back if all letter matches, works with odd or even len() word(s)
def padlindrome(main):
    new = removal(main)
    corrects = (len(new) // 2)
    counter = 0
    for x in range(len(new) // 2):
        if new[x] == new[-x - 1]:
            counter += 1
    if counter == corrects:
        return True
    return False


# ask for input and print answers
word = input()
if padlindrome(word):
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
