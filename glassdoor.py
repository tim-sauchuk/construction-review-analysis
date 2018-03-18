from bs4 import BeautifulSoup
import urllib.request as lib
import requests
import pandas as pd
from lxml import html

def getData(url):
    req = lib.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = lib.urlopen(req)
    soup = BeautifulSoup(webpage, 'html.parser')
    name_box = soup.find_all('span', attrs={'class': 'value'})
    for i in name_box:
        print(i.text.strip())

getData('https://www.glassdoor.com/Overview/Working-at-Suffolk-Construction-EI_IE11220.11,31.htm')

'''payload = {
	"username": "<USER NAME>",
	"password": "<PASSWORD>"
}

session_requests = requests.session()
login_url = 'https://www.glassdoor.com/profile/login_input.htm?userOriginHook=HEADER_SIGNIN_LINK'
result = session_requests.get(login_url)

tree = html.fromstring(result.text)

result = session_requests.post(
	login_url,
	data = payload,
	headers = dict(referer=login_url)
)

url = 'https://www.glassdoor.com/index.htm'
result = session_requests.get(
	url,
	headers = dict(referer = url)
)
'''