print("hello")

# create a tuple to store book prices
book_prices = (12.50, 15.00, 24.50)
#find the average price of the books
average_price = sum(book_prices) / len(book_prices)

#create a dictionary to store the book titles and individual prices
book_info = {"title": "Python", "price": average_price}
book_info.update({"title": "C#", "price": 123.5})
# Add a new book to the dictionary
book_info = ({"title": "Java", "price": 123.5}, 
                 {"title": "C++", "price": 123.5},
                 {"title": "C", "price": 123.5},
                    {"title": "C#", "price": 123.5},)
# print the book info
print(book_info)