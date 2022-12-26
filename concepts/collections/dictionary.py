# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

"""
Ordered
Changeable
Duplicates Not allowed
"""

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Length
print(len(this_dict))

# constructor
dict_one = dict(name="john", age="36", country="Norway")
print(dict_one)

# accessing elements in a dictionary
name = dict_one["name"]
print(name)

# Get Keys
# The keys method will return a list of all keys in the dictionary

keys = dict_one.keys()

# get values
# the values method will return a list of all values in the dictionary
values = dict_one.values()

dict_one["name"] = "Jude"
print(dict_one["name"])
print(dict_one.values())

# get Items
# The items() method will return each item in a dictionary as tuples in a list
print(dict_one.items())

# Check if key exists
if "name" in dict_one:
    print(f"Yes name  exists")

# Update Dictionary
dict_one.update({"name": "Bob"})
print(dict_one)

# Removing items
# The pop method removes the item with the specified key name
dict_one.pop("name")
print(dict_one)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
print(dict_one.popitem())

# Clear
# The clear method empties the dictionary
dict_one.clear()

# Loop through keys and values using items()
dict_two = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in dict_two.items():
    print(x, y)

# Nested dictionaries
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(my_family["child1"])
