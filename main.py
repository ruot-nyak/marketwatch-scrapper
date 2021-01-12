import requests
import re
from bs4 import BeautifulSoup as bs
import html5lib


stock = input('What is your stock tag? ')

#requesting the url for desired page to scrape
r = requests.get(f"https://www.marketwatch.com/investing/stock/{stock}/analystestimates?mod=mw_quote_tab")

#grabbing all of the information on the page
page = bs(r.content, features="html5lib")

#gathering specific elements from page
tables = page.find_all(class_="table value-pairs no-heading font--lato") 


#parsing for the statistics on the stocks
numbers = tables[1].find_all(class_="table__cell w25")

#creating parameters for floats in a list
numeric_const_pattern = r'[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'

#rx function allows us to pull floats from a string
rx = re.compile(numeric_const_pattern, re.VERBOSE)

class bot:
    def __init__(self,high,low,median,average,current_price):
        self.high = high
        self.low = low
        self.median = median
        self.average = average
        self.current_price = current_price



    def return_high(self,high):

        high_num = str(numbers[0])
        #pulling the float from the parsed information, without this returns strange string
        high = rx.findall(high_num)  
        print(f'The High for {stock} is, ${high[1]}')
        return high

    def return_low(self,low):
        low_num = str(numbers[2])
        low = rx.findall(low_num)
        print(f'The low for {stock} is, ${low[1]}')
        return low

    def return_median(self,median):
        median_num = str(numbers[1])
        median = rx.findall(median_num)
        print(f'The median for {stock} is, ${median[1]}')
        return median

    def return_average(self,average):
        average_num = str(numbers[3])
        self.average = rx.findall(average_num)
        print(f'The average for {stock} is, ${self.average[1]}')
        return self.average[1]

    def return_current_price(self,current_price):
        current_price_num = str(numbers[4])
        self.current_price = rx.findall(current_price_num)
        print(f'The current value of {stock} is, ${self.current_price[1]}')
        return self.current_price[1]

    # def choice(self,):
    #     if (self.current_price >= self.average):
    #         print('Buy!')
    #         return
    #     else:
    #         print('Don\'t Buy!')




# print(tables[1])
# print(numbers)
test = bot('',0,0,0,0)
test.return_high('')
test.return_low('')
test.return_median('')
test.return_average('')
test.return_current_price('')
# test.choice()