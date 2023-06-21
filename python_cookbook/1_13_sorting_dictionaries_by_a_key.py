# Sorting a list of dictionaries by a common key

# create a dictionary
stocks = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22}, 
            {'name': 'FB', 'shares': 200, 'price': 21.09}]

# use the itemgetter function from the operator module
from operator import itemgetter
rows_by_name = sorted(stocks, key=itemgetter('name'))
print(rows_by_name)

rows_by_price = sorted(stocks, key=itemgetter('price'))
print(rows_by_price)