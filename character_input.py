"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = input("Enter your name : ")

age = int(input("Enter your age : "))

year = (2018 - age)+100

print("Hi {}, you are {} years old.".format(name, age))
print("You will turn 100 in the year {} year".format(year))

