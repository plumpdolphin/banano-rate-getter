import re
import requests

from bs4 import BeautifulSoup


class BananoRateGetter:
    def __init__(self, inverse_pair = False):
        self.inverse = inverse_pair

    # Get the HTML of the website from the internet
    def get_url(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    # Return HTML element from DOM
    def get_element(self, selector):
        return self.soup.select(selector)[0]

    # Returns the current buying price for the exchange
    def purchase_price(self):
        self.get_url(self.buy_url)
        element = self.get_element(self.buy_selector)
        price = self.price_float(element.text)

        if (self.inverse):
            return self.invert_pair(price)
        return price

    # Returns the current selling price for the exchange
    def sell_price(self):
        self.get_url(self.sell_url)
        element = self.get_element(self.sell_selector)
        price = self.price_float(element.text)
        
        if (self.inverse):
            return self.invert_pair(price)
        return price

    # Converts price innerHTML to float price in NANO per BAN
    def price_float(self, text):
        # Extract price string from input
        match = self.exp.match(text)

        # Convert text to float
        str = match.group(1)
        return float(str)

    # Inverts trading pair, ie. from NANO/BAN to BAN/NANO
    @staticmethod
    def invert_pair(a):
        if a == 0:
            raise ZeroDivisionError
        return( 1 / a )