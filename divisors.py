"""
Create a program that asks the user for a number
and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

user_number = int(input("Please enter a number : "))

list_range = list(range(1, user_number+1))

divisorList = []

# Solution 1
for n in list_range:
    if user_number % n == 0:
        divisorList.append(n)

print(divisorList)

# Solution 2
d = [x for x in list_range if user_number % x == 0]
print(d)