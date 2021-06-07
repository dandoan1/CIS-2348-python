# Dan Doan 1986920
lemon = (float(input("Enter amount of lemon juice (in cups):\n")))

water = (float(input("Enter amount of water (in cups):\n")))

agave = (float(input("Enter amount of agave nectar (in cups):\n")))

serving = (float(input("How many servings does this make?\n")))

print("\nLemonade ingredients - yields", '{:.2f}'.format(serving), "servings")
print('{:.2f}'.format(lemon), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar")

many = float(input("\nHow many servings would you like to make?\n"))

print("\nLemonade ingredients - yields", '{:.2f}'.format(many), "servings")
print('{:.2f}'.format(many / 3), "cup(s) lemon juice")
print('{:.2f}'.format(many / .375), "cup(s) water")
print('{:.2f}'.format(many / 2.4), "cup(s) agave nectar")

print("\nLemonade ingredients - yields", '{:.2f}'.format(many), "servings")
print('{:.2f}'.format((many / 3) / 16), "gallon(s) lemon juice")
print('{:.2f}'.format((many / .375) / 16), "gallon(s) water")
print('{:.2f}'.format((many / 2.4) / 16), "gallon(s) agave nectar")
