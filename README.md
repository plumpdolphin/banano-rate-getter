# banano-rate-tool
### An open-source python tool for getting exchange rates.

This project allows you to easily scrape various Banano/Nano exchange websites to grab the price.
In order to use this module, you will need to install the python requests package.

You can do so with this command:
'''
pip install requests
'''

Then, just copy the <b>/brg</b> folder into your project, and you can start getting exchange prices!



## How to use

First, import the module for the exchange you'd like to request from.
Let's take Kuyumcu for example, you would import it like this:
'''python
from brg.kuyumcu import Kuyumcu
'''

And now that you have it imported, we just need to make an instance of the Kuyumcu class.
'''python
myInstance = Kuyumcu()
'''

Now you are ready to use the two price functions!
The all exchange classes have three functions: <i>purchase_price()</i>, <i>sell_price()</i>, and <i>invert_pair</i>.

The purchase_price() function gives the cost to purchase 1 BAN in NANO.
The sell_price() function gives the amount of NANO you receive for 1 BAN.
The invert_pair() function swaps the currency pair; if it's BAN per NANO, it swaps to NANO per BAN, and visa versa.
invert_pair() is a static function, and can be used without an instance.

Here's how you can use them:
'''python
buy_price = myInstance.purchase_price()
sell_price = myInstance.sell_price()

ban_per_nano_price = Kuyumcu.invert_pair(buy_price)
'''

And that's all there is too it!
