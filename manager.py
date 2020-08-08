
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
    
# Update order for custom pizza
  def update_order(self):
    while True:
      try:
        customer = int(input("Please enter your phone number to update your order: "))
      except:
        print("Please enter numbers!")
        continue
      else:
        break

    while customer not in self.orders:
      while True:
        try:
          customer = int(input("The option you entered does not exist, please try again, or press '0' to quit: "))
        except:
          print("Please enter numbers!")
          continue
        else:
          break
      
      if customer == 0:
        return
    
    order = self.orders[customer]

    print("""    
                     1. Update your pizza type

                     2. Update your name 

                     3. Update your topping

                     4. Update your sauce

                     0. Cancel""")

    choice = input("Enter an Option: ")
    if(choice == '1'):
      newType = input("New pizza type: ")
      order.setType(newType)
    elif(choice == '2'):
      newName = input("New name: ")
      order.setName(newName)
    elif(choice == '3'):
      newTopping = input("New topping: ")
      order.setTopping(newTopping)
    elif(choice == '4'):
      newSauce = input("New sauce: ")
      order.setSauce(newSauce)
    else:
      pass
      
    print("Done! \n")

# Deleting order for custom Pizza
  def delete_order(self):
    
    while True:
      try:
        customer = int(input("Please enter your phone number to update your order: "))
      except:
        print("Please enter numbers!")
        continue
      else:
        break

    while customer not in self.orders:
      while True:
        try:
          customer = int(input("The option you entered does not exist please try again, or press '0' to quit: "))
        except:
          print("Please enter numbers!")
          continue
        else:
          break
  
    del self.orders[customer]

    print("Thank you! Your order has been deleted! \n")
 
 # Read the custom pizza

  def see_order(self):

    if not self.orders:
      print("No orders yet. \n")
      return
    
    for order in self.orders:
      print(self.orders.get(order))