print ("Please Confirm Your Order")
print ("To confirm please enter 1 ")
print ("To cancel please enter 2 ")
while True:
    try:
        delivery = int(input("Please enter a number "))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print ("Order Confirmed")
                break
    
            elif delivery == 2:
                print ("Your Order has been Cancelled")

                break
        else:
            print("The number must be 1 or 2")    
    except ValueError:
       print("That is not a valid number")
       print("Please enter 1 or 2")


       