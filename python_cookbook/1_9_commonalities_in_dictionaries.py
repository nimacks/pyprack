"""
You have two dictionaries and want to find out what
they might have in common (same
keys, same values, etc.).
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# perform a common set operation to get common keys
print(a.keys() & b.keys())

# find keys that are common
print(a.items() & b.items())

# find keys in a that are not in b
print(a.keys() - b.keys())

# create a dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)
