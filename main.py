# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from termcolor import colored
from yahoo_fin.stock_info import *

# testing the yahoo finance methods
# print(get_live_price("FB"))
# print(get_quote_table("FB"))

# List of all S&P 500 companies
print(tickers_sp500())

# Getting input from user and displaying stock price
# stock = input("Please enter a ticket symbol: ")
stock = input(colored('Please enter a ticket symbol: ', 'red', attrs=['bold']))
quote_table = {}

if stock.upper() in tickers_sp500():
    print(colored('The stock is in the S&P 500.\n', 'blue', attrs=['bold']))
    print("The stock price of "+stock.upper()+" is: ", colored(str(round(get_live_price(stock.upper()), 2)), 'blue'))

    # print("Quote Data:\n")
    quote_table = get_quote_table(stock.upper())
    print("\n{:<39} {:<61}".format(colored('Data-Point', 'red'), colored('Value', 'red')))
    # print(type(quote_table))

    # Format the data in table grid
    for k, v in quote_table.items():
        print("{:<30} {:<70}".format(k, colored(v, 'blue')))
else:
    print("Not in the S&P 500")



