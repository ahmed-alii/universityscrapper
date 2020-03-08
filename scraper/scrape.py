from scraper import scrapper
import csv


def generate_list():
    scrapper.get_university_list()


def get_all_data():
    with open("URL_LIST.csv", 'r', encoding='utf-8', newline='') as csv_file:
        data = csv.reader(csv_file, delimiter='\t')
        scrapper.write_to_csv(["Institution Name", "Native Name", "Location", "World Rank",
                               "National Rank", "Quality of Education Rank", "Alumni Employment Rank",
                               "Quality of Faculty Rank", "Research Output Rank", "Quality Publications Rank",
                               "Influence Rank", "Citations Rank", "Overall Score", "Domain"])
        x = 0
        for d in data:
            x = x + 1
            print(x, "-> ", d[0])
            scrapper.scrape_n_save(d[0])


get_all_data()
s