from flask import Flask, render_template
from scraper import rankings as r

app = Flask(__name__)

countries = r.get_countries()


@app.route('/')
def index():
    data = r.flask_results("Pakistan")
    return render_template("index.html",
                           data=data["graph_data"].values.tolist(),
                           countries=countries,
                           current=data["country"],
                           uni_count=data["total_uni"],
                           avg_ranking=data["avg"])


@app.route('/country/<country_name>')
def hello(country_name):
    data = r.flask_results(country_name)
    return render_template("index.html",
                           data=data["graph_data"].values.tolist(),
                           countries=countries,
                           current=data["country"],
                           uni_count=data["total_uni"],
                           avg_ranking=data["avg"])


if __name__ == "__main__":
    app.run()
