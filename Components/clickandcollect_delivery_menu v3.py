# Bugs
# Will only work for valid input "d" and "c"
# menu so that user can choose either click and collect or delivery
print ("Do you want your order delivered or are you collecting it?")
print ("For Click and collect enter 1")
print ("For delivery enter 2")
delivery = int(input())
if delivery == 1:
    print ("Click and collect")
elif delivery == 2:
    print ("Delivery")
else:
    print ("That was not a valid input")