# Dan Doan 1986920
# making the class
class ItemToPurchase:
    item_name = "none"
    item_price = 0
    item_quantity = 0

    def init(self):
        self.item_name = ""
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price,
                                                 (self.item_price * self.item_quantity)))


if __name__ == "__main__":
    # asking for input and printing them out as needed
    item = ItemToPurchase()
    print("Item 1")
    name1 = input("Enter the item name:\n")
    price1 = float(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    print("\nItem 2")
    name2 = input("Enter the item name:\n")
    price2 = float(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    print("\nTOTAL COST")
    # calling the class and then getting results
    item.item_name = name1
    item.item_price = price1
    item.item_quantity = quantity1
    item.print_item_cost()
    item.item_name = name2
    item.item_price = price2
    item.item_quantity = quantity2
    item.print_item_cost()
    print("\nTotal: ${:.0f}".format(price1 * quantity1 + price2 * quantity2))
