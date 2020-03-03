from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
import csv, time


def get_university_list():
    soup = Soup(uReq('https://cwur.org/2018-19.php'), "html.parser")
    table = soup.find_all("table", {"class": "table"})
    with open('URL_LIST.csv', 'w', encoding='utf-8', newline='') as csvfile:
        f = csv.writer(csvfile, delimiter='\t')
        for table_data in table:
            table_body = table_data.find('tbody')
            rows = table_body.find_all('tr')
            for tr in rows:
                data = []
                cols = tr.find_all('td')
                nav_anchor = cols[1].find('a', href=True)
                data.append("https://cwur.org/" + nav_anchor['href'])
                f.writerow(data)
    print("Got list of URLs in `URL_LIST.csv`.")
    return


def scrape_data(url_address):
    data = []
    page_html = uReq(url_address)
    soup = Soup(page_html, "html.parser")
    table = soup.find_all("table", {"class": "table"})[0]
    rows = table.find_all('tr')
    for row in rows:
        data.append(row.find_all('td')[-1].text)
    return data


def generate_header(url_address):
    data = []
    page_html = uReq(url_address)
    soup = Soup(page_html, "html.parser")
    table = soup.find_all("table", {"class": "table"})[0]
    rows = table.find_all('tr')
    for row in rows:
        data.append(row.find_all('td')[0].text)
    write_to_csv(data)
    return True


def append_to_csv(data):
    with open("data.csv", 'a', encoding='utf-8', newline='') as csv_file:
        f = csv.writer(csv_file, delimiter='\t')
        f.writerow(data)
    return


def write_to_csv(data):
    with open("data.csv", 'w', encoding='utf-8', newline='') as csv_file:
        f = csv.writer(csv_file, delimiter='\t')
        f.writerow(data)
    return


def scrape_n_save(url):
    append_to_csv(scrape_data(url))
    print("Done Scrape & Save")


get_university_list()
# time.sleep(3)
# generate_header('https://cwur.org/2018-19/University-of-California,-Berkeley.php')

