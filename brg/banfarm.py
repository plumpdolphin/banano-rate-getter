import re
import time

from . import BananoRateGetter

### WARNING NOT FUNCTIONAL ###
# TODO Renders Javascript, but needs to wait for async JSON response from XHR


class BanFarm(BananoRateGetter):
    def __init__(self, inverse_pair=False):
        super().__init__(inverse_pair=inverse_pair)

        # Shared variables
        self.buy_url = 'https://ban.farm/'
        self.sell_url = 'https://ban.farm/'
    
        # CSS selector for HTML element
        self.buy_selector = '.price p'
        self.sell_selector = '.price p'

        # Expression for separating the price text
        self.exp = re.compile('Buy ([\w.]*) ')
    
    # Invert price pairs to standard NANO/BAN pair
    def purchase_price(self):
        price = super().purchase_price()
        return super().invert_pair(price)

    def sell_price(self):
        price = super().sell_price()
        return super().invert_pair(price)