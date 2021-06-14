#Dan Doan 1986920
class ItemToPurchase:
  item_name = "none"
  item_price = 0
  item_quantity = 0
  item_description = "none"
  def init(self):
    self.item_name = ""
    self.item_price = 0
    self.item_quantity = 0
  def print_item_cost(self):
    print("{} {} @ ${:.0f} = ${:.0f}".format(self.item_name, self.item_quantity, self.item_price, (self.item_price*self.item_quantity)))
  def print_item_description(self):
    print("{}: {}".format(self.item_name, self.item_description))
class ShoppingCart:
  customer_name = "none"
  current_date = "January 1, 2016"
  cart_items = []
  def init(self):
    self.customer_name = "none"
    self.current_date = "January 1, 2016"
    self.cart_items = []
  def add_item(ItemToPurchase):
    shop.cart_items.append(ItemToPurchase)

"""
  def remove_item(item_name):
    if item_name in self.cart_items:
      self.cart_items.remove(item_name)
    else:
      print("Item not found in cart. Nothing removed.")
  def modify_item(ItemToPurchase):
    if item_name in self.cart_items:
      #change amount of items in cart
    else:
      print("Item not found in cart. Nothing modified.")
  def get_num_items_in_cart():
    #return len(self.cart_items) or return quant of all items in cart
  def get_cost_of_cart():
    return #total cost of items in cart
  def print_total():
    if self.cart_items != 0:
      print(#total of objects in cart)
    else:
      print("SHOPPING CART IS EMPTY")
  def print_descriptions():
    for x in self.cart_items:
      print(ItemToPurchase.item_description(x))
  """
def print_menu(ShoppingCart):
    print("""MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
""")

    option = input("Choose an option:")
    while True:
        if option not in "arcioq":
            option = input("Choose an option:")
        if option == "q":
            break

shop = ShoppingCart
shop.add_item("oreos")
shop.customer_name = input("Enter customer's name:\n")
shop.current_date = input("Enter today's date:\n")
print("""Customer name: {}
Today's date: {}""".format(shop.customer_name, shop.current_date))
print(shop.cart_items)
print_menu(1)