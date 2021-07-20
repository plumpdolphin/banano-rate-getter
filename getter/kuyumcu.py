import re

from . import BananoRateGetter

class Kuyumcu(BananoRateGetter):
    def __init__(self):
        # Shared variables
        self.exp = re.compile('@ ([\w.]*)')
        self.url = 'https://banano.nano.trade/'
    
        # Yes, I am aware this looks very backwards. I didn't design the site.
        # Don't ask me why they made the classes this way
        self.buy_selector = '.SellPrice'
        self.sell_selector = '.BuyPrice'
