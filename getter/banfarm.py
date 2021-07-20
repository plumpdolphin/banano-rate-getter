import re
import requests
from bs4 import BeautifulSoup

# Shared variables
exp = re.compile('@ ([\w.]*)')
url = 'https://ban.farm/'