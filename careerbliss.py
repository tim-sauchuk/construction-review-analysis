from bs4 import BeautifulSoup
import urllib.request as lib
import requests
import pandas as pd
from lxml import html

# specify the url
url = 'https://www.careerbliss.com/suffolk-construction/reviews/'

def getData(url):
    req = lib.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = lib.urlopen(req)
    soup = BeautifulSoup(webpage, 'html.parser')
    name_box = soup.find_all('div', attrs={'class' : 'company-reviews'})
    for i in name_box:
        print(i.text.strip())

getData(url)