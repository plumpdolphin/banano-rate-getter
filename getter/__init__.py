import re
import requests
from bs4 import BeautifulSoup

class BananoRateGetter:
    def __init__(self):
        pass

    # Get the HTML of the website from the internet
    def get_url(self):
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    # Return HTML element from DOM
    def get_element(self, selector):
        return self.soup.select(selector)[0]

    # Returns the current buying price for the exchange
    def purchase_price(self):
        self.get_url()
        self.get_element(self.buy_selector)

    # Returns the current selling price for the exchange
    def sell_price(self):
        pass

    # Converts price innerHTML to float price in NANO per BAN
    def price_float(self, text):
        # Extract price string from input
        match = self.exp.match(text)

        # Convert text to float
        str = match.group(1)
        return float(str)

    # Inverts trading pair, ie. from NANO/BAN to BAN/NANO
    def invert_pair(self, a):
        if a == 0:
            raise ZeroDivisionError
        return( 1 / a )