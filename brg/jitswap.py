import re

from . import BananoRateGetter


class JitSwap(BananoRateGetter):
    def __init__(self, inverse_pair=False):
        super().__init__(inverse_pair=inverse_pair)

        # Shared variables
        self.buy_url = 'https://jitswap.com/swap/NANO/to/BAN'
        self.sell_url = 'https://jitswap.com/swap/BAN/to/NANO'
    
        # CSS selector for HTML element
        self.buy_selector = '#withValue'
        self.sell_selector = '#withValue'

        # Expression for separating the price text
        self.exp = re.compile('([\w.]*)')
    
    # Pass on Javascript rendering
    def render_session(self):
        pass

    # Inverts from BAN/NANO to NANO/BAN
    def purchase_price(self):
        price = super().purchase_price()
        return super().invert_pair(price)

    # Adjusts rate by the default 200 BAN trade
    def sell_price(self):
        self.get_url(self.sell_url)
        element = self.get_element(self.sell_selector)
        
        # Adjust by default trade size
        price = self.price_float(self.get_element_text(element)) / 200

        if (self.inverse):
            return self.invert_pair(price)
        return price