"""
You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
"""


# if the values in the sequence are hashable then
# the problem can be solved using a set and generatar

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


    
a = [1, 2, 4, 65, 3, 2, 1, 1, 4, 65, 7, 3, 8]
print(list(dedupe(a)))


def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a_dict = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_dict(a_dict, key=lambda d: (d['x'], d['y']))))
