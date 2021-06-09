def removal(word):
    newword = ""
    for x in word:
        if x == " ":
            pass
        else:
            newword+=x
    return newword
def padlindrome(word):
    new = removal(word)
    corrects = (len(new)//2)
    counter = 0
    for x in range (len(new)//2):
        if new[x] == new[-x-1]:
            counter +=1
    if counter == corrects:
        return True
    return False

word = input()
if (padlindrome(word)):
    print (word + " is a palindrome")
else:
    print (word + " is not a palindrome")
