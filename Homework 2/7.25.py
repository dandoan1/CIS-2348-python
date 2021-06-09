#Dan Doan 1986920
def exact_change(user_total):
    remaining = user_total
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    while remaining > 100 or remaining == 100:
        remaining -= 100
        num_dollars += 1
    while remaining > 25 or remaining == 25:
        remaining -= 25
        num_quarters += 1
    while remaining > 10 or remaining == 10:
        remaining -= 10
        num_dimes += 1
    while remaining > 5 or remaining == 5:
        remaining -= 5
        num_nickels += 1
    while remaining > 1 or remaining == 1:
        remaining -= 1
        num_pennies += 1
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__=="__main__":
    input_val = int(input())
    if input_val == 0 or input_val < 0:
        print("no change")
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if num_dollars == 0:
        pass
    elif num_dollars == 1:
        print(num_dollars, "dollar")
    else:
        print(num_dollars, "dollars")
    if num_quarters == 0:
        pass
    elif num_quarters == 1:
        print(num_quarters, "quarter")
    else:
        print(num_quarters, "quarters")
    if num_dimes == 0:
        pass
    elif num_dimes == 1:
        print(num_dimes, "dime")
    else:
        print(num_dimes, "dimes")
    if num_nickels == 0:
        pass
    elif num_nickels == 1:
        print(num_nickels, "nickel")
    else:
        print(num_nickels, "nickels")
    if num_pennies == 0:
        pass
    elif num_pennies == 1:
        print(num_pennies, "penny")
    else:
        print(num_pennies, "pennies")
