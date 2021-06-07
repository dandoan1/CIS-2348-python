# Dan Doan 1986920
height = int(input("Enter wall height (feet):\n"))

width = int(input("Enter wall width (feet):\n"))

print("Wall area:", height * width, "square feet")

paint = float(('{:.2f}'.format((height * width) / 350)))
print("Paint needed:", paint, "gallons")
print("Cans needed:", round(paint), "can(s)")
amount = round(paint)
color = (input("\nChoose a color to paint the wall:\n"))
cost = {"red": 35, "blue": 25, "green": 23}
print("Cost of purchasing", color, "paint:", "$" + str((cost[color]) * amount), end="\n")
