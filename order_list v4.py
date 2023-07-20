donut_names = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed', 
               'Chocolate Frosted', 'Bavarian cream ', 'Maple Frosted', 'French Cruller', 
               'Glazed', 'Apple Fritter', 'Chocolate Glazed', 'Boston Kreme']

donut_prices = [3.50,4.00,4.00,3.00,2.50,3.50,5.00,4.50,3.00,2.00,4.50,5.00]


#donut list
def menu():
    number_donuts = 12
    for count in range (number_donuts):
        print("{} {} ${:.2f}" .format(count+1,donut_names[count],donut_prices[count]))

#list to store ordered donuts
order_list =[]

#list to store donut prices
order_cost = []

#ask for total number of donuts for order
num_donuts = 0
menu()
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

#choose donuts from the list
print("Please choose your donuts by entering the number from the menu ")

for item in range(num_donuts):
    while num_donuts >0:
        donut_ordered = int(input())
        donut_ordered = donut_ordered-1
        order_list.append(donut_names[donut_ordered])
        order_cost.append(donut_prices[donut_ordered])
        print("{} ${:.2f}" .format(donut_names[donut_ordered],donut_prices[donut_ordered]))
        num_donuts = num_donuts-1
        
print(order_list)
print(order_cost)
