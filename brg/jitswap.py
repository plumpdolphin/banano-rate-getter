import re

from . import BananoRateGetter


class JitSwap(BananoRateGetter):
    def __init__(self):
        super().__init__()

        # Shared variables
        self.buy_url = 'https://jitswap.com/swap/NANO/to/BAN'
        self.sell_url = 'https://jitswap.com/swap/BAN/to/NANO'
    
        # CSS selector for HTML element
        self.buy_selector = '#withValue'
        self.sell_selector = '#withValue'

        # Expression for separating the price text
        self.exp = re.compile('([\w.]*)')
    
    # Inverts from BAN/NANO to NANO/BAN
    def purchase_price(self):
        price = super().purchase_price()
        return super().invert_pair(price)

    # Adjusts rate by the default 200 BAN trade
    def sell_price(self):
        price = super().sell_price() 
        return (price / 200)