import re

from .brg import BananoRateGetter


class BanFarm(BananoRateGetter):
    def __init__(self):
        super().__init__()

        # Shared variables
        self.buy_url = 'https://ban.farm/'
        self.sell_url = 'https://ban.farm/'
    
        # Yes, I am aware this looks very backwards. I didn't design the site.
        # Don't ask me why they made the classes this way
        self.buy_selector = 'app-price div.price p b'
        self.sell_selector = 'app-price div.price p b:nth-of-type(2)'

        # Expression for separating the price text
        self.exp = re.compile('([\w.]*)')
    
    # Invert price pairs to standard NANO/BAN pair
    def purchase_price(self):
        price = super().purchase_price()
        return super().invert_pair(price)

    def sell_price(self):
        price = super().sell_price()
        return super().invert_pair(price)