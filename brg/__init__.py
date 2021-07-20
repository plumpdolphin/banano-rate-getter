import re
import time

from .rhh import HTMLSession


class BananoRateGetter:
    def __init__(self, inverse_pair = False):
        self.inverse = inverse_pair
        self.session = HTMLSession()

    # Get the HTML of the website from the internet
    def get_url(self, url):
        self.response = self.session.get(url)
        self.render_session()

    # Executes Javascript to dynamically load webpage
    def render_session(self):
        self.response.html.render()

    # Return HTML element from DOM
    def get_element(self, selector):
        return self.response.html.find(selector, first=True)

    # Return data from HTML element
    @staticmethod
    def get_element_text(element):
        return element.text

    # Returns the current buying price for the exchange
    def purchase_price(self):
        self.get_url(self.buy_url)
        element = self.get_element(self.buy_selector)
        price = self.price_float(self.get_element_text(element))

        if (self.inverse):
            return self.invert_pair(price)
        return price

    # Returns the current selling price for the exchange
    def sell_price(self):
        self.get_url(self.sell_url)
        element = self.get_element(self.sell_selector)
        price = self.price_float(self.get_element_text(element))
        
        if (self.inverse):
            return self.invert_pair(price)
        return price

    # Converts price innerHTML to floating-point number
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