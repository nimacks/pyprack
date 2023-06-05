"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

Characteristics
- Ordered
- Unchangeable
- Allow duplicates
"""
# find the length of a tuple
this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple))

tuple_variety = ("1", 1, "one")
print(tuple_variety[0])

# creating a tuple with one item requires a comma at the end
tuple_two = ("apple",)

# tuples can contain different data types
tuple_three = ("abc", 34, True, 40, "male")

# tuple() constructor
tuple_four = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# accessing tuples using index
print(f"This is how we access tuple two =>  {tuple_two[0]} \n")

# Negative indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item
print(f"The last element in a tuple is {tuple_four[-1]} \n")

# range indexing
# leaving out the start and end value will include the beginning and end
# tuple_four[:2] & tuple_four[0:]
print(f"The range {tuple_four[0:2]} \n")

# range of negative values
# Specify negative indexes if you want to start the search from the end of the tuple:
print(f"The range {tuple_four[-1:-2]} \n")

# check if item exists
if "apple" in tuple_four:
    print("Yes, 'apple' is in the fruits tuple")

# Change tuple values
# Once a tuple is created, you cannot change its values.
# Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list,
# change the list, and convert the list back into a tuple.

x = ("one", "two", "three")
y = list(x)
y[0] = "four"
x = tuple(y)
print(x)

# Adding items to a tuple
# 1. convert into a list

# see above

# 2. add tuple to a tuple
tuple_five = ("one", "two", "three")
tuple_six = ("four", "five", "six")
tuple_five += tuple_six
print(tuple_five)


# Removing items for a tuple
# Tuples are unchangeable, so you cannot remove items from it,
# but you can use the same workaround as we used for changing and adding tuple items:
tuple_seven = ("one", "two", "three")
p = list(tuple_seven)
p.remove("three")
tuple_seven = tuple(p)

# Unpacking a tuple
packed_fruits = ("apple", "banana", "cherry")
(green, yellow, red) = packed_fruits

# using asterisk
# If the number of variables is less than the number of values,
# you can add an * to the variable
# name and the values will be assigned to the variable as a list:
seattle_packed_fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green1, yellow2, *red3) = seattle_packed_fruits
print(red3)

# loop through a tuple
tuple_eight = ("apple", "banana", "cherry")
for x in tuple_eight:
    print(x)

# join two tuples
tuple_nine = ("a", "b", "c")
tuple_ten = (1,2,3)
tuple_eleven = tuple_nine + tuple_ten
print(tuple_eleven)
print(tuple_eleven.count('a'))
