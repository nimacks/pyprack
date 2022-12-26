"""
you want to keep a limited history of the last few items seen during iteration
 or during some other kind of processing
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def run():
    with open(
            '/Users/nimacks/Projects/repos/github/pyprack/python_cookbook/1_2_unpacking_elements_arbitrary_length.py') as f:
        for line, previous_lines in search(f.readlines(), 'uname', 5):
            for pline in previous_lines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


run()
