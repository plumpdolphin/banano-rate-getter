import re
import requests
from bs4 import BeautifulSoup


# Shared variables
exp = re.compile('BAN/NANO rate: ([\w.]*) NANO')
url = 'https://jitswap.com/swap/BAN/to/NANO'

# Converts price innerHTML to float price in NANO per BAN
def price_float(text):
    # Extract price string from input
    match = exp.match(text)
    print(match)

    # Convert text to float
    str = match.group(1)
    return float(str)


# Invert NANO/BAN to BAN/NANO
def nano_to_banano(a):
    if a == 0:
        return -1
    return( 1 / a )


# Gets buy price of BAN in NANO
def buy_banano():
    # Get text response from Kuyumcu
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Return price from SellPrice element
    price = soup.select('.small')[0]
    print (price.text)
    return price_float(price.text)


# Gets sell price of BAN in NANO
def sell_banano():
    # Get text response from Kuyumcu
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Return price from BuyPrice element
    price = soup.select('small.BuyPrice')[0]
    return price_float(price.text)

print(buy_banano())