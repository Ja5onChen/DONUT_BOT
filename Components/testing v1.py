import sys
import random

# List of random names
names = ["Mark", "Phoebe", "Michael", "Denise", "Ellen", "Eric", "Lewis", "Lana", "Moana", "Sally"]

# List of donut names
donut_names = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed',
               'Chocolate Frosted', 'Bavarian Cream', 'Maple Frosted', 'French Cruller',
               'Glazed', 'Apple Fritter', 'Chocolate Glazed', 'Boston Kreme']

# List of donut prices
donut_prices = [3.50, 4.00, 4.00, 3.00, 2.50, 3.50, 5.00, 4.50, 3.00, 2.00, 4.50, 5.00]

# List to store ordered donuts
order_list = []

# List to store donut prices
order_cost = []

# Customer details dictionary
customer_details = {}

# Validates inputs to check they are not blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("This cannot be blank")

# Validates inputs to check if they are an integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:
            print("That is not a valid number")
            print(f"Please enter a number between {low} and {high}")

# Validates string input to check if they are alphabetical
def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if not x:
            print("Input must only contain letters")
        else:
            return response.title()

# Validates phone number to check if it is between 7 to 10 digits
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num // 10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return num
            else:
                print("NZ phone numbers have 7 and 10 digits")
        except ValueError:
            print("Please enter a number")


# Welcome message with random name
def welcome():
    num = random.randint(0, 9)
    name = names[num]
    print("***Welcome to Dream Donut***")
    print("***My name is", name, "****")
    print("*** I will be here to help you order your delicious dream donut ***")


# Menu for click and collect or delivery
def order_type():
    del_pick = ""
    LOW = 1
    HIGH = 2
    question = f"Enter a number between {LOW} and {HIGH}: "
    print("Is your order for Click and collect or delivery?")
    print("For Click and Collect please enter 1")
    print("For Delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print("Click and Collect")
        del_pick = "Click and Collect"
        click_and_collect_info()
    else:
        print("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick


# Click and collect information
def click_and_collect_info():
    question = "Please enter your name: "
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = "Please enter your phone number: "
    customer_details['phone'] = check_phone(question, 7, 10)
    print(customer_details['phone'])
    print(customer_details)
    print()


# Delivery information
def delivery_info():
    question = "Please enter your name: "
    customer_details['name'] = check_string(question)
    print(customer_details['name'])

    question = "Please enter your phone number: "
    customer_details['phone'] = check_phone(question, 7, 10)
    print(customer_details['phone'])

    question = "Please enter your house number: "
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = "Please enter your street name: "
    customer_details['street'] = check_string(question)
    print(customer_details['street'])

    question = "Please enter your suburb: "
    customer_details['suburb'] = check_string(question)
    print(customer_details['suburb'])
    print(customer_details)
    print()

#donut list
def donut_list():
    number_donuts = 12
    for count in range (number_donuts):
        print("{} {} ${:.2f}" .format(count + 1, donut_names[count], donut_prices[count]))


# Choose total Number of donuts - max 20
# donut order - from menu - print each donut ordered with cost
def order_donuts():
    # ask for total number of pizzas for order
    num_donuts = 0
    LOW = 1
    HIGH = 20
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {LOW} and {HIGH} ") 
    print("How many donuts do you want to order? ")
    num_donuts = val_int(LOW, HIGH, question)
    #choose donut from menu
    for item in range(num_donuts):
        while num_donuts > 0:
            print("Please choose your donuts by entering the"
            "number from the menu ")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ") 
            donut_ordered =  val_int(MENU_LOW, MENU_HIGH, question)
            donut_ordered = donut_ordered -1
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
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ") 
    print ("Please Confirm Your Order")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("Order Confirmed")
        print ("Your order has been sent to our kitchen")
        print ("Your delicious donut will be with you shortly")
        new_exit()                
    elif confirm == 2:
        print ("Your Order has been Cancelled")
        print ("You can restart your order or exit the BOT")
        new_exit() 
#option for new order or to exit
def new_exit():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ") 
    print ("Do you want to start another Order or exit?")
    print ("To start another order please enter 1 ")
    print ("To exit the BOT please enter 2 ")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear() 
        main()
    elif confirm == 2:
        print ("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear() 
        sys.exit()

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

