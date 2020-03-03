from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get('file:///Users/ahmed/Downloads/CWUR%202018-2019%20_%20Top%20Universities%20in%20the%20World.html')
# time.sleep(5)

soup = BeautifulSoup(driver.page_source.encode("utf-8"), features="html.parser")
tables = soup.findChildren('table')

my_table = tables[0]

head = my_table.findChildren(['th'])
rows = my_table.findChildren(['tr'])


def head_row():
    head_list = []
    for h in head:
        head_list.append(h.string)
    return head_list


def body_rows():
    data_list = []
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            print(cell)


body_rows()

# for row in rows:
#     cells = row.findChildren('td')
#     print(cells)
#     # if len(cells) > 0:
#         # for cell in cells:
#         #     # value = cell.string
#         #     # print(value)
#     print("----")

# with open('test.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(head_row())
