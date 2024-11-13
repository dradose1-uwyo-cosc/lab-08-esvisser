# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section:
# Sources, people worked with, help given to:
# Your
# Comments
# Here


# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria
# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
# - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
# - This method needs to be able to handle multiple values.
# - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
# - This one does not need to take in any extra parameters.
# - It should create and set the attributes defined above.
# - placeOrder():
# - This method will allow a customer to order a pizza.
# - Which will increment the number of orders.
# - It will need to create a pizza object.
# - You will need to prompt the user for:
# - the size
# - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
# - all the toppings the user wants, ending prompting on an empty string.
# - Implementation of this is left to you; you can, for example:
# - have a while loop and append new entries to a list
# - have the user separate all toppings by a space and turn that into a list.
# - Upon completion, create the pizza object and store it in the list.
# - getPrice()
# - You will need to determine the price of the pizza.
# - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
# - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
# - Creates a receipt of the current pizza.
# - Show the sauce, size, and toppings.
# - Show the price for the size.
# - The price for the toppings.
# - The total price.
# - getNumberOfOrders()
# - This will simply return the number of orders.
# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
# Example output:
class pizza:
    """a pizza"""
    def __init__(self,Size,Sauce='red'):
        self.Size= Size
        self.Sauce = Sauce
        self.Toppings=["cheese"]
    def getsize(self):
        return int(self.Size)
    def getsauce(self):
        return self.Sauce
    def set_size(self,size):
        if int(size)>10:
            self.Size=int(size)
        return size
    def gettoppings(self):
        return self.Toppings
    def set_sauce(self):
        return self.Sauce
    def toppings_num(self):
        return len(self.Toppings)
class Pizzaria:
    """a restaurant, but for pizza"""
   
    def __init__(self):
        self.orders=0
        self.price_topping=0.30
        self.price_inch=0.60
        self.pizzas=[]
    def place_order(self):
        self.orders+=1
        ordersize=input("enter the size of pizza you want. cannot be smaller than 10")
        ordersauce=input("enter the type of sauce you want. the default is red")
        topings_list=[]
        while True:
            ordertoppings=input('enter the toppings you want. enter stop to exit')
            if ordertoppings=='stop':
                break
            else:
                topings_list.append(ordertoppings)
        ordered_pizza=pizza(ordersize,ordersauce)
        for topping in ordertoppings:
            ordered_pizza.Toppings.append(topping)
        self.pizzas.append(ordered_pizza)
    def getprice(self):
       return (pizza.getsize()*self.price_inch)+(pizza.toppings_num*self.price_topping)
    def getrecipt(self):
        current_piz=self.pizzas[-1]
        print(current_piz.getsize())
        print(current_piz.getsauce())
        print(current_piz.gettoppings())
        print(f"the size price is ${current_piz.getsize()*self.price_inch}")
        print(f"the price for toppings is ${current_piz.toppings_num()*self.price_topping}")
        print(f"the total price is ${(current_piz.getsize()*self.price_inch)+(current_piz.toppings_num()*self.price_topping)}")
    def num_orders(self):
        return self.orders
pizzaria=Pizzaria()
while True:
    user_input=input("do you want a pizza? enter exit to exit")
    if user_input=='exit':
       print(pizzaria.num_orders())
       break
    else:
        pizzaria.place_order()
        print(f"the number of pizzas orderd is{pizzaria.getrecipt()}")




"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon
You ordered a 20" pizza with garlic sauce and the following toppings:
cheese
pepperoni
bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9
Would you like to place an order? exit to exit
"""
