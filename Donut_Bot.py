import sys
import random
from random import randint
#list of random names
names = ["Mark", "Pheobe", "Michael", "Denise", "Ellen", "Eric", "Lewis", "Lana", "Moana", "Sally" ]
#list of donut names
donut_names = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed',
               'Chocolate Frosted', 'Bavarian cream ', 'Maple Frosted', 'French Cruller',
               'Glazed', 'Apple Fritter', 'Chocolate Glazed', 'Boston Kreme']

#list of donut prices
donut_prices = [3.50,4.00,4.00,3.00,2.50,3.50,5.00,4.50,3.00,2.00,4.50,5.00]

#list to store ordered donuts
order_list = []
#list to sore donut prices
order_cost = []
#Customer details dictionary
customer_details = {}

#validates inputs to check they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print ("This cannot be blank")
#welcome message with random name
def welcome():
    '''
    purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
num = randint(0,9)
name = (names[num])
print("***Welcome to Dream Donut***")
print("***My name is",name,"****")
print("*** I will be here to help you order your delicious dream donut ***")




#click and collect information
def clickandcollect_info():  
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ("please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])
   
#delivery information
def delivery_info():
    question = ("Plese enter your name ")
    customer_details['name'] = not_blank(question )
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("please enter your street name ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])
    print(customer_details)
    


#menu for click and collect or delivery
def order_type():
    print ("Do you want your order delivered or are you collecting it?")
    print ("For Click and collect enter 1")
    print ("For delivery enter 2")
   
    while True:
        try:
            delivery =int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and Collect")
                    del_pick = "click and collect"
                    clickandcollect_info()
                    break
                elif delivery ==2:
                    print ("Delivery")
                    del_pick = "delivery"
                    delivery_info()
                    break
                else:
                    print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2")
    return del_pick 
   
   
#donut list
def donut_list():
    number_donuts = 12
    for count in range (number_donuts):
        print("{} {} ${:.2f}" .format(count+1,donut_names[count],donut_prices[count]))

#choose total number of donuts -max 20
#donut order
def order_donuts():
    num_donuts = 0
    while True:
        try:        
            num_donuts = int(input("How many Donuts do you want to order? "))
            if num_donuts >=1 and num_donuts <= 20:
                break
            else:
                print("Your order must be between 1 and 20")
        except ValueError:
            print("That is not a valid number")
            print("Please enter number between 1 and 20")
   
    print(num_donuts)
    #choose donut from menu
    for item in range(num_donuts):
        while num_donuts >0:
            while True:
                try:
                    donut_ordered = int(input("Please choose your donuts by entering the number from the menu "))
                    if donut_ordered >= 1 and donut_ordered <=12:
                        break
                    else:
                        print("your number must be between 1 and 12")
                except ValueError:
                    print ("that is not a valid number")
                    print ("Please enter number between 1 and 12")
            donut_ordered = donut_ordered-1
            order_list.append(donut_names[donut_ordered])
            order_cost.append(donut_prices[donut_ordered])
            print("{} ${:.2f}" .format(donut_names[donut_ordered],donut_prices[donut_ordered]))
            num_donuts = num_donuts-1

#print order out- including if order is del or pick up and names and price of each pizza - total cost including any delivery charge

def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Customer Details:")
    if del_pick =="click and collect":
            print("Your order is for Click and Collect")
            print(f"Customer Name:  {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
            print("Your order is for Delivery")
            print(f"Customer Name:  {customer_details['name']} \nCustomer Phone: {customer_details['phone']}  \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print()
    if del_pick == "delivery":
        if len(order_list) >= 5:
            print("Your order will be delivered to you for free")
        elif len(order_list) <5:
            print("Due to the fact that you have ordered less than 5 items, there is a $9.00 surcharge for delivery")
            total_cost = total_cost +9
    print("Total Order Cost")
    print(f"${total_cost:.2f}")



#ability to cancel or proceed with order
def confirm_cancel():
    print ("Please Confirm Your Order")
    print ("To confirm please enter 1 ")
    print ("To cancel please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order Confirmed")
                    print ("Your Order has been sent to our kitchen")
                    print ("Your delicious pizza will be with you shortly")
                    new_exit()
                    break
            
                elif confirm == 2:
                    print ("Your Order has been Cancelled ")
                    print ("You can restart the order ot exit the BOT")
                    new_exit()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is no a valid number")
            print("Please enter 1 or 2")

#option for new order or to exit
def new_exit():
    print ("Do you want to start another Order or exit?")
    print ("To start another order please enter 1")
    print ("To exit the BOT please enter 2")
    while True:
        try:
            confirm = int(input("Please enter a number"))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("New Order")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear() 
                    main()
                    break
            
                elif confirm == 2:
                    print ("Exit")
                    order_list.clear()
                    order_cost.clear()
                    customer_details.clear() 
                    sys.exit()
                    break
            else:
                print("The number must be 1 or 2")    
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


#main function
def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: none
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    donut_list()
    order_donuts()
    print_order(del_pick)
    confirm_cancel()
    
   
main()

