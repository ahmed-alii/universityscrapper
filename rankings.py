import pandas as pd

data = pd.read_csv("data.csv", header=1, delimiter='\t')
print(data["Location"][0])

