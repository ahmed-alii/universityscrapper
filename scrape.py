from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
import csv

url = 'https://cwur.org/2018-19.php'

soup = Soup(uReq(url), "html.parser")
table = soup.find_all("table", {"class": "table"})
with open('to_scrape.csv', 'w', encoding='utf-8', newline='') as csvfile:
    f = csv.writer(csvfile, delimiter='\t')
    for table_data in table:
        table_body = table_data.find('tbody')
        rows = table_body.find_all('tr')
        for tr in rows:
            data = []
            cols = tr.find_all('td')
            nav_anchor = cols[1].find('a', href=True)
            data.append("https://cwur.org/"+nav_anchor['href'])
            f.writerow(data)
