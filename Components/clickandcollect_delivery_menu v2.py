# Bugs
# Will only work for valid input "d" and "c"
# menu so that user can choose either click and collect or delivery
print ("Do you want your order delivered or are you collecting it?")
print ("For delivery enter d")
print ("For Click and collect enter c")
delivery = input()
if delivery == "d":
    print ("Delivery")
elif delivery == "c":
    print ("Click and collect")
else:
    print ("That was not a valid input")
