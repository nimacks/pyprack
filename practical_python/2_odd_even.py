"""
Write a pogram to determine if a number is odd or even
"""

try:
    x: int = int(input("Insert any number"))
    if 0 == x % 2:
        print("The number you entered is even")
    else:
        print("The number you entered is odd")
except:
    print("You did not enter a number")
