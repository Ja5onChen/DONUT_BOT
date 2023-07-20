#list of donut names
order_list = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed']
# list to store ordered prices
order_cost = [3.50,4.00,4.00,3.00]


cust_details = {'name':'Mark','phone':'0213345656', 'house':'45', 'street':'Harry', 'suburb':'Howick'}

def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details:")
    print(f"Customer Name: {cust_details['name']} \nCustomer phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Details")
    count = 0 
    for item in order_list:
        print("{} ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")
    
print_order()