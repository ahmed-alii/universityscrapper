from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

url = 'https://cwur.org/2018-19.php'
pageHtml = uReq(url)
soup = soup(pageHtml, "html.parser")
table = soup.find_all("table", {"class": "table"})

with open('test.csv', 'w', encoding='utf-8', newline='') as csvfile:
    f = csv.writer(csvfile, delimiter='\t')

    f.writerow(['Nav_url', 'World Rank', 'Institution', 'Location',
                'National Rank', 'Quality of Education',
                'Alumni Employment', 'Quality of Faculty',
                'Research Output', 'Quality Publications',
                'Influence', 'Citations', 'Score'])
    for table_data in table:
        table_body = table_data.find('tbody')
        rows = table_body.find_all('tr')
        for tr in rows:
            data = []
            cols = tr.find_all('td')
            nav_anchor = cols[1].find('a', href=True)
            data.append("https://cwur.org/"+nav_anchor['href'])
            for td in cols:
                data.append(td.text.strip())
            f.writerow(data)
            # print(data)