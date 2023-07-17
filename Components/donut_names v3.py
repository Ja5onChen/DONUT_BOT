donut_names = ['Powdered', 'Jelly', 'Strawberry Frosted', 'Blueberry Glazed', 
               'Chocolate Frosted', 'Bavarian cream ', 'Maple Frosted', 'French Cruller', 
               'Glazed', 'Apple Fritter', 'Chocolate Glazed', 'Boston Kreme']

donut_prices = [3.50,4.00,4.00,3.00,2.50,3.50,5.00,4.50,3.00,2.00,4.50,5.00]



#Item list
def list():
    number_donuts = 12
    for count in range (number_donuts):
        print("{} {} ${:.2f}" .format(count+1,donut_names[count],donut_prices[count]))
list()
