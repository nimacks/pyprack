"""
Problem :
You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception.

Solution:
Use the python star expression to encapsulate the numbers you're interested in
"""


# star unpacking throwing elements
def drop_first_last(grades):
    first, *middle, last = grades
    return (sum(middle) / len(middle))


####

def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


# Star unpacking using for loops
def tuple_star():
    records = [('foo', 1, 2),
               ('bar', 'hello'),
               ('far', 3, 4)]

    for tag, *args in records:
        if tag == 'far':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)


# start unpacking with string processing

def stringify():
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    result = 'The user name is {uname}. Files are {fields}. Homedirectory is linked to {homedir} and shell is {sh}'
    result_with_f_strings = f'The user name is {uname}. Files are {fields}. Homedirectory is linked to {homedir} and shell is {sh}'
    print(result.format(uname=uname, fields=fields, homedir=homedir, sh=sh))
    print(result_with_f_strings)


# unpacking by throwing away values

def throwaway():
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(f'The name is {name} and year is {year}')


# Execute
# print(drop_frist_last([1,2,45,23,5,4,4,7,3,4,43]))
# tuple_star()
# stringify()
throwaway()

if __name__ == "__main__":
    throwaway()
