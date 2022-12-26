import heapq
"""[A program to find the largest or small of n numbers]

"""


def find():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    small_numbers = heapq.nsmallest(5, nums)
    large_numbers = heapq.nlargest(3, nums)
    small_numbers.sort()
    large_numbers.sort(reverse=True)
    print(small_numbers)
    print(large_numbers)


def find_tuple():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    tweets = [
        {'tweet1': 'welcome to twitter', 'length': 10},
        {'tweet1': 'this is the second message', 'length': 20}
    ]

    people = [
        {'person': 'john doe', 'height': 200},
        {'person': 'eve johnson', 'height': 150},
        {'person': 'mary blithe', 'height': 170},
    ]
    
    longest_tweet = heapq.nlargest(1,tweets,key=lambda k:k['length'])
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
    expensive = heapq.nlargest(1, portfolio, key=lambda p: p['price'])
    two_tallest_person = heapq.nlargest(2, people, key=lambda t: t['height'])
    print(cheap)
    print(expensive)
    print(longest_tweet)
    print(f"The two tallest people are {two_tallest_person}")


# find()
find_tuple()
