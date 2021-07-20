import re

from .brg import BananoRateGetter

### WARNING NOT FUNCTIONAL ###
# TODO Needs to render JavaScript to the DOM before it can be parsed.


class BananoExchange(BananoRateGetter):
    def __init__(self):
        super().__init__()

        # Shared variables
        self.buy_url = 'https://banano.exchange/'
        self.sell_url = 'https://banano.exchange/'
    
        # CSS selector for HTML element
        self.buy_selector = 'input#price'
        self.sell_selector = 'input#price'

        # Expression for separating the price text
        self.exp = re.compile('([\w.]*)')
