# Dan Doan 1986920
# function will do majority of work which is
# doing the math calculation and returns two number if a true boolean value is met
def function(num1, num2, num3, num4, num5, num6):
    for x in range(-10, 10):
        for y in range(-10, 10):
            if (((num1 * x) + (num2 * y)) == num3) and (num4 * x + num5 * y) == num6:
                return str(x) + " " + str(y)
    return "No solution"


# inputs and call
q1 = int(input())
q2 = int(input())
q3 = int(input())
q4 = int(input())
q5 = int(input())
q6 = int(input())
print(function(q1, q2, q3, q4, q5, q6))
