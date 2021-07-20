import re

from .brg import BananoRateGetter

### WARNING NOT FUNCTIONAL ###
# TODO Needs to render JavaScript to the DOM before it can be parsed.


class BanFarm(BananoRateGetter):
    def __init__(self):
        super().__init__()

        # Shared variables
        self.buy_url = 'https://ban.farm/'
        self.sell_url = 'https://ban.farm/'
    
        # CSS selector for HTML element
        self.buy_selector = '.price p b'
        self.sell_selector = '.price p b:nth-child(2)'

        # Expression for separating the price text
        self.exp = re.compile('([\w.]*)')
    
    # Invert price pairs to standard NANO/BAN pair
    def purchase_price(self):
        price = super().purchase_price()
        return super().invert_pair(price)

    def sell_price(self):
        price = super().sell_price()
        return super().invert_pair(price)