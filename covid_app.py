import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def covid_app():
    if request.method == "POST":
        url = "https://api.covid19api.com/summary"
        api_response = requests.get(url).json()
        user_country = request.form["country"]
        for i in api_response.get("Countries"):
            if i["Country"].lower() == user_country.lower():
                print_data = {
                    "country_name": i["Country"],
                    "total_confirmed": i["TotalConfirmed"],
                    "total_deaths": i["TotalDeaths"],
                    'status_code': 200
                }
                return render_template('index.html', data=print_data)
        else:
            print('in for_else')
            print_data = {
                'message': 'Country not found, please click the above link for country reference list',
                'status_code': 404
            }
            return render_template('index.html', data=print_data)
    else:
        return render_template('index.html', data=None)


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(port=port)
