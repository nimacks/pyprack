"""
    Problem: You have multiple dictionaries or mappings that you want to 
    logically combine into a single mapping to perform certain operations, 
    such as looking up values or checking for the existence of keys.
    """

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# use the chainMap class from the collections module

from collections import ChainMap

c = ChainMap(a, b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

# A ChainMap takes multiple mappings and makes them logically appear as one.
# However, the mappings are not literally merged together. Instead, a ChainMap
# simply keeps a list of the underlying mappings and redefines common dictionary
# operations to scan the list. Most operations will work. For example:  

# Alternative to ChainMap
# The update() method of dictionaries does not return any value. It updates the
# Dictionary with elements from a dictionary object or an iterable object of key/value pairs.   
#