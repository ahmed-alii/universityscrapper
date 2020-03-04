import csv

with open("data.csv", 'r', encoding='utf-8', newline='') as csv_file:
    data = csv.reader(csv_file, delimiter='\t')
    for d in data:
        print(d)