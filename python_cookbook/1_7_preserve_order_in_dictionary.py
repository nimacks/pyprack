'''
You want to create a dictionary, and you also want to control the order of items when
iterating or serializing.
'''
from collections import OrderedDict
import json

d = OrderedDict()
d['foo']= 1
d['bar']=3
d['can']=9

for key in d:
    print(key,d[key])
    
print(json.dumps(d))