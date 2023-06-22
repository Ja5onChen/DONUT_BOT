import random
from random import randint
#list of random names
names = ["Mark", "Pheobe", "Michael", "Denise", "Ellen", "Eric", "Lewis", "Lana", "Moana", "Sally" ]
def welcome():
    '''
    purpose: To generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
num = randint(0,9)
name = (names[num])
print("***Welcome to Dream Donut***")
print("***My name is",name,"****")
print("*** I will be here to help you order your delicious dream donut ***")
def main():
    '''
    Purpose: To run all functions
    A welcome message
    Parameters: none
    Returns: None
    '''
    welcome()
main()