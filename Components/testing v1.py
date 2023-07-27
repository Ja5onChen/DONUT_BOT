# Donut Bot
# Bugs - Phone Number allows letters
#      - Name allows numbers
# Different types of modules being imported into the code
import sys
# - Importing the module of sys which is a module
#   that provides access to some objects used or
#   maintained by the interpreter
import random
# - Importing the module of random which is a
#   module that is used to generate random things
from random import randint
# - From the module of random,
#   it imports the module of randint
#   which returns an integer number from a
#   specified range of numbers


# - List of random names used at the beginning of
#   the code when starting the program and the welcome message appears
names = ["Mark", "Phoebe", "Michael", "Denise", "Ellen", "Eric", "Lewis", "Lana", "Moana", "Sally"]

# List of donut names
#   These donut names are the different products that the
#   store has to offer for sale
donut_names = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed',
               'Chocolate Frosted', 'Bavarian Cream', 'Maple Frosted', 'French Cruller',
               'Glazed', 'Apple Fritter', 'Chocolate Glazed', 'Boston Kreme']

# - List of donut prices.
#   These are the prices for the different donuts
#   the store has to offer for sale
donut_prices = [3.50, 4.00, 4.00, 3.00, 2.50, 3.50, 5.00, 4.50, 3.00, 2.00, 4.50, 5.00]

# - list to store ordered donuts. When ordering the donuts,
#   the program will append all the names of the donuts
#   which are ordered
order_list = []

# - list to store donut prices. When ordering the donuts,
#   the program will append all the costs of the donuts
#   which are ordered
order_cost = []

# - Customer details dictionary - Is a dictionary (a list)
#   which can hold customer details and has a variable name.
#   It allows the user to take information out more easily
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
            

# validates inputs to check if they an integer
# takes low, high and question as parameters
# returns input if the integer is valid
def val_int(low, high, question):
    while True:
        # sets up while loop
        try:
            # - the program will print the statement
            #   (question) which is asking for an input
            num = int(input(question))
            # asks for input(integer)
            if num >= low and num <= high:
                # - if num is inside or equal
                #   to the one of the numberic
                #   boundaries, it will return num.
                return num
            else:
                # - if num is outside of the numeric boundaries
                #   an error message
                    print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            # - if the input is not an integer it will go to the
            #   except code and print an error message followed
            #   by an instruction
            print ("That is not a valid number.")
            # Error Print Statement
            print(f"Please enter a number between {low} and {high}.")
            # Instruction print statement
            
            
# validates string inputs to check if they are a string
# takes question as parameter
# returns response in title class if valid
def check_string(question):
    while True:
        # sets up while true loop
        response = input(question)
        # asks for input(string)
        x = response.isalpha()
        # - checks that the input is in alphabetical
        #   and sets x to True if alpha
        if x is False:
            # if x is False prints error message
            print("Input must only contain letters.")
        else:
            return response.title()
            # if True returns response in title class


# Validates phone number to check if it is between 7 to 10 digits
# takes low, high and question as parameters
# returns input if the input is an integer and has 7 to 10 digits
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        # sets up while loop
        try:
            # - the program will print the statement
            #   (question) which is asking for an input
            num = int(input(question))
            # asks for input(integer)
            test_num = num
            # - sets test_number to equal number which
            #   allows program to pull apart the number
            #   which is inputted to make sure it is a number
            count = 0
            while test_num > 0:
                # - starts another while loop where
                #   test_num is bigger than 0
                test_num = test_num//10
                # - test_num is being divided by 10 to
                #   split up the number
                count = count + 1
                # - since count is equal to 0,
                #   every digit will be
                #   counted to check the number of
                #   digits that have been entered
            if count >= PH_LOW and count <= PH_HIGH:
                # - if count is inside or equal
                #   to one of the numeric boundaries,
                #   it will return num.
                return num
            else:
                # - if num is outside of the numeric
                #   boundaries an error message
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            # - if the input is not an integer it will go
            #   to the except code and print an error
            #   message followed by an instrction
            print ("That is not a valid number.")
            # Error Print Statement
            print("Please enter a number.")
            # Instruction print statement

# Generates message with a random name
# from the list called names and prints it out
# No Parameters
# No Returns


def welcome():
    '''
    Purpose: To generate a random name form the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0, 9)
    # - setting num to randint which returns
    #   an integer number from a specified range
    #   of numbers, 0 to 9 in this case
    name = (names[num])
    # - setting name to equal the list of names at the index of
    #   the random numbers. Each word in a list has an index
    #   number with the first one starting with 0 unless specified
    print()
    # prints blank space
    print("***Welcome to Dream Donut***")
    # Print statement welcoming user to online shop with help of bot
    print("***My name is", name, "****")
    # - Print statement which introduces the person
    #   helping including the random name
    print("*** I will be here to help you order your delicious dream donut ***")
    # Print statement stating what the program will help you achieve
    print()
    # prints blank space




# Creates the option to choose either pickup or delivery
# takes in Low, High and question as parameters when
# sending to the validate integer input function
# returns del_pick information at the end of the function
def order_type():
    del_pick = 0
     # Sets del_pick to empty
    LOW = 1
    HIGH = 2
    question = f"Enter a number between {LOW} and {HIGH}: "
    # - The question which asks if the user type in 1 or 2
    #   depending on if they want delivery or pickup
    print("Is your order for Click and collect or delivery?")
    # - Print statement which informs customer
    #   they are going to have to choose between delivery and pickup
    print("For Click and Collect please enter 1")
    print("For Delivery please enter 2")
    delivery = val_int(LOW, HIGH, question)
    # - sets delivery to equal validate input which sends
    #   input through the function of validate input which
    #   checks if the input is an integer and if it fits in
    #   the numeric boundaries set by low and high
    if delivery == 1:
        # If Delivery is equal to 1
        print("Click and Collect")
        # - Prints statement stating Click and collect
        #   to show you have chosen click and collect
        del_pick = "click and collect"
        # - sets del_pick to equal click and collect
        #   (will be used in the order print statement function)
        click_and_collect_info()
        # Opens and runs the function called click and collect info
    else:
        # if delivery is the other option, 2
        print("Delivery")
        # - Prints statement stating
        #   Delivery to show you have chosen Delivery
        del_pick = "delivery"
        # - sets del_pick to equal
        #   delivery (will be used in the order print statement function)
        delivery_info()
        # Opens and runs the function called delivery info
    return del_pick
    # returns del_pick information back to del_pick


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

