"""
Write a pogram to determine if a number is odd or even
"""


try:
    x = int(input("Insert any number"))
    if x%2 ==0:
        print("The number you entered is even")
    else: 
        print("The number you entered is odd")
except:
    print("You did not enter a number")