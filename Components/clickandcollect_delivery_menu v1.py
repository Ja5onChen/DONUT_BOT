# Bugs
# Will only work for valid input "d" and "c"
# menu so that user can choose either click and collect or delivery
print ("Do you want your order delivered or are you collecting it?")
print ("For delivery enter d or enter p for click and collect")
delivery = input()
if delivery == "d":
    print ("Delivery")
elif delivery == "c":
    print ("Click and collect")
