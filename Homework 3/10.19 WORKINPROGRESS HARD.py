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
  def add_item(ItemToPurchase, item_name=None):
    self.cart_items.append((item_name))
shop = ShoppingCart
shop.add_item("oreos")

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
if __name__=="__main__":
  item = ItemToPurchase()
  print ("Item 1")
  name1 = input("Enter the item name:\n")
  price1 = float(input("Enter the item price:\n"))
  quantity1 = int(input("Enter the item quantity:\n"))
  print ("\nItem 2")
  name2 = input("Enter the item name:\n")
  price2 = float(input("Enter the item price:\n"))
  quantity2 = int(input("Enter the item quantity:\n"))
  print("\nTOTAL COST")
  item.item_name = name1
  item.item_price = price1
  item.item_quantity = quantity1
  item.print_item_cost()
  item.item_name = name2
  item.item_price = price2
  item.item_quantity = quantity2
  item.print_item_cost()
  print("\nTotal: ${:.0f}".format(price1*quantity1+price2*quantity2))