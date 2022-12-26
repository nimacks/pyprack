"""
You want to implement a queue that sorts items by a given
priority and always returns the item with the highest priority on each pop operation
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # In this recipe, the queue consists of tuples
        # of the form (-priority, index, item).
        # The priority value is negated to get the queue to sort items
        # from the highest priority to lowest priority.
        # This is opposite of the normal heap ordering,
        # which sorts from lowest to highestvalue
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


dental_line = PriorityQueue()
dental_line.push(Item('john'), 6)
dental_line.push(Item('Julie'), 8)
dental_line.push(Item('Bob'), 9)
dental_line.push(Item('Kofi'), 10)

# The first pop operation returned the item with the highest priority
print(dental_line.pop())
print(dental_line.pop())
print(dental_line.pop())
print(dental_line.pop())
