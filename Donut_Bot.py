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
                    print ("Click and collect")
                    clickandcollect_info()
                    break
                elif delivery ==2:
                    print ("Delivery")
                    delivery_info()
                    break
                else:
                    print("Number must be 1 or 2")
        except ValueError:
            print ("That was not a valid input")
            print ("Please enter 1 or 2")
       
       
       

   
   

   
   
   
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

#ability to cancel or proceed with order


#option for new order or to exit



#main function
def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: none
    Returns: None
    '''
    welcome()
    order_type()
    donut_list()
    order_donuts()
   
main()

