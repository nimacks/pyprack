"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in number_list:
    if i < 5:
        print(i)

numbers_five_less = [x for x in number_list if x < 5]
print(numbers_five_less)