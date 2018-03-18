from bs4 import BeautifulSoup
import urllib.request as lib
import csv
import os

# specify the url
url = 'https://www.indeed.com/cmp/Suffolk-Construction/reviews'

def getData(url):

    # list of reviews
    text = []
    header = []
    job_title = []

    # whether to go to next page of reviews
    bool = True
    # current index of review
    start = 0

    while(bool):

        # get HTML
        req = lib.Request(url + '?start=' + str(start), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = lib.urlopen(req)
        soup = BeautifulSoup(webpage, 'html.parser')

        # find reviews
        current_text = soup.find_all('span', attrs={'class' : 'cmp-review-text'})
        current_header = soup.find_all('div', attrs={'class': 'cmp-review-title'})
        current_job_title = soup.find_all('span', attrs={'class': 'cmp-reviewer'})

        # check to see if there are more reviews
        if(len(current_text) != 21):
            bool = False

        # if second or more page, remove first review
        if(start != 0 and len(current_text) != 0):
            current_text.pop(0)
            current_text.pop(0)

        # index to next page
        start += 20

        # add text to list
        for i in current_text:
            text.append(i.text.strip())

        # add headers to list
        for i in current_header:
            header.append(i.text.strip())

        # add job titles to list
        for i in current_job_title:
            job_title.append(i.text.strip())

    # open a csv file with append, so old data will not be erased
    os.remove('indeed-com.csv')

    with open('indeed-com.csv', 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)
        for i, v in enumerate(text):
            writer.writerow([job_title[i], header[i], text[i]])

getData(url)