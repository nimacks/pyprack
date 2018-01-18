"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""
# solution 1
random_list = list(range(1, 10, 2))
random_list_two = list(range(1, 10, 1))

common_elements = []

for i in random_list_two:
    if i in random_list:
        common_elements.append(i)

print(common_elements)


# solution 2
a = list(range(1, 10, 2))
b = list(range(1, 100, 1))
c = [x for x in set(a) if x in set(b)]
print(c)
