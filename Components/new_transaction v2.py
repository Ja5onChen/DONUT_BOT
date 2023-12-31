import sys

#list to store ordered donuts
order_list = []
#list to store donut prices
order_cost = []

#customer details dictionary
customer_details = {}

#option for new order or to exit
def main():
    print("start again")
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