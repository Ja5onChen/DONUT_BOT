# Will only work for valid input "d" and "c"
# menu so that user can choose either click and collect or delivery
# Bugs - need it so that it only accepts 1 or 2
print ("Do you want your order delivered or are you collecting it?")
print ("For Click and collect enter 1")
print ("For delivery enter 2")

while True:
    try:
        delivery =int(input("Please enter a number "))
        if delivery >= 1 and delivery <= 2:
            if delivery == 1:
                print ("Click and collect")
                break
            elif delivery ==2:
                print ("Delivery")
                break
            else:
                print("Number must be 1 or 2")
    except ValueError:
        print ("That was not a valid input")
        print ("Please enter 1 or 2")
        