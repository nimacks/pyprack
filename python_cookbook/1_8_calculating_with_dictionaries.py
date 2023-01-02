'''
You want to perform various calculations (e.g., minimum value, maximum value, sorting,
etc.) on a dictionary of data.
'''

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 37.20,
    'AMZN': 3320.23
}

cars = {
    'BMW': 34,
    'Toyota': 24,
    'Mercedez': 90
}

# Finding the minimum value in a dictionary
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

cheapest_Car = min(zip(cars.values(), cars.keys()))
expensive_car = max(zip(cars.values(), cars.keys()))
print(f"The Cheapest car is {cheapest_Car}")
print(f"The most expensive car is {expensive_car}")
print((expensive_car[0]))  # gives you the value
print((expensive_car[1]))  # gives you the key
