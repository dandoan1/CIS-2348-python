#Dan Doan 1986920
def function(q1, q2, q3, q4, q5, q6):
    for x in range(-10,10):
        for y in range(-10,10):
            if ((((q1 * x) + (q2 * y)) == q3)) and (q4*x + q5*y)==q6:
                return (str(x)+" "+str(y))
    return "No solution"
q1 =int(input())
q2 =int(input())
q3 =int(input())
q4 =int(input())
q5 =int(input())
q6 =int(input())
print(function(q1,q2,q3,q4,q5,q6))
