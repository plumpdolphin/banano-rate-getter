import re

from . import BananoRateGetter


class Kuyumcu(BananoRateGetter):
    def __init__(self, inverse_pair=False):
        super().__init__(inverse_pair=inverse_pair)

        # Shared variables
        self.buy_url = 'https://banano.nano.trade/'
        self.sell_url = 'https://banano.nano.trade/'
    
        # Yes, I am aware this looks very backwards. I didn't design the site.
        # Don't ask me why they made the classes this way
        self.buy_selector = '.SellPrice'
        self.sell_selector = '.BuyPrice'

        # Expression for separating the price text
        self.exp = re.compile('@ ([\w.]*)')

    # Pass on Javascript rendering
    def render_session(self):
        pass