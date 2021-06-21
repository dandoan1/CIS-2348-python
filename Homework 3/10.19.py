# Dan Doan 1986920

# print menu to print menu
def printmenu():
    print("""MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
""")


# from the last lab
class ItemToPurchase:
    item_name = ""
    item_price = 0
    item_quantity = 0
    item_description = "none"

    def init(self, item_name="", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price,
                                                 (self.item_price * self.item_quantity)))


# main shopping cart class
class ShoppingCart:
    # initialize with given customer namem current date, and an empty cart item dictionary
    def __init__(self, customer_name="none", current_date="January 1, 2016", cart_items=None):

        if cart_items is None:
            cart_items = {}
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items  # name as key, description, price, quantity list as the other

    # adding items to cart items as dictionary and list
    def add_item(self, ItemToPurchase):
        description1 = input("Enter the item description:\n")
        price1 = input("Enter the item price:\n")
        quantity1 = input("Enter the item quantity:\n")
        self.cart_items[ItemToPurchase] = [description1, price1, quantity1]
        print()

    # removing items using string to search for keys inside cart
    def remove_item(self, ItemName):
        if ItemName in self.cart_items:
            del self.cart_items[ItemName]
            print()
        else:
            print("Item not found in cart. Nothing removed.\n")

    # using input to look for string search inside cart, if found, will prompt a new quantity number
    def modify_item(self, ItemToPurchase):
        newquant = input("Enter the new quantity:\n")
        if ItemToPurchase in self.cart_items:
            print(self.cart_items[ItemToPurchase])
            self.cart_items[ItemToPurchase][2] = newquant
        else:
            print("Item not found in cart. Nothing modified.\n")

    # will print keys and keys[0] as descriptions
    def print_descriptions(self):
        print("Item Descriptions")
        for keys in self.cart_items:
            print("{}: {}".format(keys, self.cart_items[keys][0]))
        print()

    # will print total items in cart and their prices
    def print_total(self):
        total_num_items = 0
        for keys in self.cart_items:
            total_num_items += int(self.cart_items[keys][2])
        print("Number of Items: {}\n".format(total_num_items))
        total_prices = 0
        for keys in self.cart_items:
            print("{} {} @ ${} = ${}".format(keys, self.cart_items[keys][2],
                                             self.cart_items[keys][1],
                                             int(self.cart_items[keys][2]) * int(self.cart_items[keys][1])))
            total_prices += int(self.cart_items[keys][2]) * int(self.cart_items[keys][1])
            if keys == list(self.cart_items)[-1]:
                print()
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY\n")
        print("Total: ${}".format(total_prices))
        print()

    # supposed to return the total quanity of item (asked for by zybooks but no idea why it won't work)
    def get_num_items_in_cart(self):
        total_quant = 0
        for keys in self.cart_items:
            total_quant += int(self.cart_items[keys][2])
        return total_quant

    # supposed to return total cost of all items (asked for by zybooks but no idea why it won't work either)
    def get_cost_of_cart(self):
        total_cost = 0
        for keys in self.cart_items:
            total_cost += int(self.cart_items[keys][1])
        return total_cost


if __name__ == "__main__":
    # a main function to be called upon
    def main():
        print("""Enter customer's name:
Enter today's date:\n""")
        print("""Customer name: {}
Today's date: {}\n""".format(customer_name, todays_date))
        printmenu()
        chosen = input("Choose an option:\n")
        # loops that continues to ask for options, will loops until "q" is input then loops breaks
        # will always print menu and then ask for another input afterward
        while True:
            if chosen not in "arcioq":
                chosen = input("Choose an option:\n")
            if chosen == "q":
                break
            if chosen == "a":
                print("ADD ITEM TO CART")
                shop.add_item(input("Enter the item name:\n"))
                printmenu()
                chosen = input("Choose an option:\n")
            if chosen == "r":
                print("REMOVE ITEM FROM CART")
                shop.remove_item(input("Enter name of item to remove:\n"))
                printmenu()
                chosen = input("Choose an option:\n")
            if chosen == "c":
                print("CHANGE ITEM QUANTITY")
                shop.modify_item(input("Enter the item name:\n"))
                printmenu()
                chosen = input("Choose an option:\n")
            if chosen == "i":
                print("OUTPUT ITEMS' DESCRIPTIONS")
                print("{}'s Shopping Cart - {}\n".format(customer_name, todays_date))
                shop.print_descriptions()
                printmenu()
                chosen = input("Choose an option:\n")
            if chosen == "o":
                print("OUTPUT SHOPPING CART")
                print("{}'s Shopping Cart - {}".format(customer_name, todays_date))
                shop.print_total()
                printmenu()
                chosen = input("Choose an option:\n")


    # initial input to get names and dates, then initializing the shoppingcart
    # the getnumitems and getcostofcart supposed to work for zybooks but they will not give me the points
    # for some reason, they keep telling me "Traceback (most recent call last): EOFError: EOF when reading a line"
    # but this program does not work if there is no item input and amount and price, ect...
    customer_name = input()
    todays_date = input()
    shop = ShoppingCart()
    shop.get_num_items_in_cart()
    shop.get_cost_of_cart()
    # calling main to initialize everything
    main()
    item = ItemToPurchase()
