from flask import Flask, render_template

import random
import requests
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    today = date.today()
    year = today.year
    name = "Perfect"
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, current_year=year, name=name)

@app.route('/guess/<name>')
def api(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_data = gender_response.json()
    age_data = age_response.json()
    searched_name = gender_data["name"]
    searched_name_cap = searched_name.title()
    gender = gender_data["gender"]
    age = age_data["age"]
    return render_template("api.html", name=searched_name_cap, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)