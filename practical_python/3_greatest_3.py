"""
Write a program to determine the greatest of 3 numbers
"""
try:
    x = float(input("Enter your first number"))
    y = float(input("Enter your second number"))
    z = float(input("Enter your third number"))

    print("The maximum number is: ", end="")
    if y <= x >= z:
        print(x) 
    elif x <= y >= z:
        print(y)
    elif y <= z >=x:
        print(z)

except:
    print("One of you inputs is not valid")