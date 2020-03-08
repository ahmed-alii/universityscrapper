import pandas as pd

pd.set_option('display.max_rows', None)
data = pd.read_csv("data/data.csv", header=0, delimiter='\t')


def country_overall_score_mean(country):
    return data[data['Location'] == country]['Overall Score'].mean()


def countrywise_data(country):
    return data[data['Location'] == country][['Institution Name', 'Overall Score', 'Domain']]


def get_countries():
    return data.Location.unique()


def get_results(country):
    print("Country: ", country)
    print("Total Universities: ", len(countrywise_data(country)))
    print("Average Ranking: ", country_overall_score_mean(country))

    print(countrywise_data(country).to_string(index=False, header=True))


def flask_results(country):
    return {"country": country,
            "graph_data": countrywise_data(country),
            "total_uni": len(countrywise_data(country)),
            "avg": country_overall_score_mean(country)
            }
