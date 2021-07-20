import re

from . import BananoRateGetter

### WARNING NOT FUNCTIONAL ###
# TODO Renders Javascript, but needs to wait for async JSON response from XHR


class BananoExchange(BananoRateGetter):
    def __init__(self, inverse_pair=False):
        super().__init__(inverse_pair=inverse_pair)

        # Shared variables
        self.buy_url = 'https://banano.exchange/'
        self.sell_url = 'https://banano.exchange/'
    
        # CSS selector for HTML element
        self.buy_selector = 'input#price'
        self.sell_selector = 'input#price'

        # Expression for separating the price text
        self.exp = re.compile('([\w.]*)')

    @staticmethod
    def get_element_text(element):
        return element.attrs['value']
