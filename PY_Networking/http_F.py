# Web Scrapping in Python

"""
- When a program or script pretends to be a browser and retrieves web pages, looks at those web pages, extracts information, and hten looks at more web pages

- Search engines scrape web pages - we call this "spidering the web" or "web crawling"
"""

# Beautiful Soup is another way to exercise web scraping with Python

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
  print(tag.get('href', None))