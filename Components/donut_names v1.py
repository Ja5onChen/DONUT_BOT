donut_names = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed', 
               'Chocolate Frosted', 'Bavarian cream ', 'Maple Frosted', 'French Cruller', 
               'Glazed', 'Apple Fritter', 'Chocolate Glazed', 'Boston Kreme']

donut_prices = [3.50,4.00,4.00,3.00,2.50,3.50,5.00,4.50,3.00,2.00,4.50,5.00]

number_donuts = 12

#print("How many laptops would you like to order?")
#num_laptops = int(input())

for count in range (number_donuts):
    print (count,donut_names[count],donut_prices[count])