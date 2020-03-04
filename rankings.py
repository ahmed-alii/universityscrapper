import pandas as pd
pd.set_option('display.max_rows', None)
data = pd.read_csv("data.csv", header=0, delimiter='\t')
data = data[data['Location'] == "United Kingdom"]

print(data[['Institution Name', 'Overall Score']])

