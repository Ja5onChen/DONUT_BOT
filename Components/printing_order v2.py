#list of donut names
order_list = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed']
# list to store ordered prices
order_cost = [3.50,4.00,4.00,3.00]

cust_details = {'name':'Mark','phone':'0213345656', 'house':'45', 'street':'Harry', 'suburb':'Howick'}


print(f"{cust_details['name']} {cust_details['phone']} {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")

count = 0 
for item in order_list:
    print("{} ${:.2f}" .format(item, order_cost[count]))
    count = count+1