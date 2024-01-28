# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = Request(
    url='https://www.businessdailyafrica.com/bd/news/ethiopia-third-africa-state-to-default-on-sovereign-debt-4474762',
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req, context=ctx).read()
soup = BeautifulSoup(webpage, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#   print(tag.get('href', None))
soup = soup.get_text()
soup = soup.strip()
print(soup)




