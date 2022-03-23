'''
You want to make a dictionary that maps keys to more than one value (a so-called
“multidict”).
the key benefit of a default dictionary is that it automatically initializes the data structure so you can 
focus on appending

'''
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['b'].append(4)

for key in d:
    print(d,d[key])