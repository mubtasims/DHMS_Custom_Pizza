
"""
Main CRUD methods

"""

from order import OrderPizza


class Manager:
  def __init__ (self):
    self.orders = {}
   # self.id = 0

#Implementing the CRUD Methodology
# Create Order for the custome pizza
  def create_order(self):
    name = input("Please enter your name: ")
    while True:
      try:
        phoneNumber = int(input("Please enter your phone number: "))
      except:
        print("Please enter numbers!")
        continue
      else:
        break
 
    pizzaType = input("What type of pizza would you like to order? : ")
    topping = input("What topping would you like? : ")
    sauce = input("What sauce would you like? : ")
    
    self.orders[phoneNumber] = OrderPizza(pizzaType, name, phoneNumber, topping, sauce)

    print("Order created! \n")
  