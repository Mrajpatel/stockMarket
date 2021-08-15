# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from yahoo_fin.stock_info import *

# testing the yahoo finance methods
# print(get_live_price("FB"))
# print(get_quote_table("FB"))

# List of all S&P 500 companies
print(tickers_sp500())

# Getting input from user and displaying stock price
stock = input("Please enter a ticket symbol: ")
quote_table = {}

if stock.upper() in tickers_sp500():
    print("The stock is in the S&P 500.\n")
    print("The stock price of "+stock.upper()+" is: ", str(round(get_live_price(stock.upper()), 2)))

    # print("Quote Data:\n")
    quote_table = get_quote_table(stock.upper())
    print("{:<25} {:<50}".format('Data-Type', 'Value'))
    # print(type(quote_table))

    # Format the data in table grid
    for k, v in quote_table.items():
        print("{:<25} {:<50}".format(k, v))
else:
    print("Not in the S&P 500")



