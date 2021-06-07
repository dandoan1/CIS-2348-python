# Dan Doan 1986920
print("""Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12\n""")
services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12, "-": 0}
name1 = input("Select first service:\n")
name2 = input("Select second service:\n")
cost1 = services[name1]
cost2 = services[name2]

print("\nDavy's auto shop invoice\n")
if name1 == "-":
    name1 = "No service"
    print("Service 1:", name1, end="\n")
else:
    print("Service 1:", name1 + ",", "$" + str(cost1), end="\n")
if name2 == "-":
    name2 = "No service"
    print("Service 2:", name2, end="\n")
else:
    print("Service 2:", name2 + ",", "$" + str(cost2), end="\n")

cost = int(cost1) + int(cost2)
print("\nTotal: $" + str(cost), end="\n")
