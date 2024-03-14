from flask import Flask, render_template, request
import requests
from datetime import datetime
from matplotlib import pyplot as plt

app = Flask(__name__)

x_time = [0, 1, 2, 3, 4, 5, 6]
y_temp = [18, 15, 18, 13, 9, 8, 8]
plt.plot(x_time, y_temp)
plt.savefig('test_chart')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/results', methods=["GET", "POST"])
def results():
    api_key = "219ee2cd1c341d93688001529dc36a06"
    form_city = request.form.get("city")
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + form_city + "&APPID=" + api_key
    response = requests.get(url).json()

    weather_list = response.get("weather", [{}])
    first_weather_dict = weather_list[0]
    description = first_weather_dict.get("description")
    city_name = response.get("name")
    timezone = response.get("timezone")
    timestamp = response.get("dt")
    timestamp_local = datetime.fromtimestamp(timestamp)

    temp_k = response.get("main", {}).get("temp")
    temp_c = int(temp_k) - 273.15 if temp_k is not None else None
    temp_celcius = round(temp_c) if temp_c is not None else None

    wind_speed = response.get("wind").get("speed")
    wind_speed_imperial = wind_speed / 1.609 if wind_speed is not None else None

    dt = datetime.fromtimestamp(timestamp)
    temp_max = response.get("main", {}).get("temp_max")
    temp_day = response.get("main", {}).get("temp_day")
    temp_night = response.get("main", {}).get("temp_eve")
    temp_eve = response.get("main", {}).get("temp_eve")
    temp_morn = response.get("main", {}).get("temp_morn")
    feels_like = response.get("main", {}).get("feels_like")

    temp_max_c = round(temp_max - 273.15) if temp_max is not None else None
    temp_day_c = round(temp_day - 273.15) if temp_day is not None else None
    temp_night_c = round(temp_night - 273.15) if temp_night is not None else None
    temp_eve_c = round(temp_eve - 273.15) if temp_eve is not None else None
    temp_morn_c = round(temp_morn - 273.15) if temp_morn is not None else None
    feels_like_c = round(feels_like - 273.15) if feels_like is not None else None

    return render_template('results.html',
                           temp_max=temp_max,
                           temp_day=temp_day,
                           temp_night=temp_night,
                           temp_eve=temp_eve,
                           temp_morn=temp_morn,
                           feels_like=feels_like,
                           temp_max_c=temp_max_c,
                           temp_day_c=temp_day_c,
                           temp_night_c=temp_night_c,
                           temp_eve_c=temp_eve_c,
                           temp_morn_c=temp_morn_c,
                           feels_like_c=feels_like_c,
                           wind_speed_imperial=wind_speed_imperial,
                           temp_celcius=temp_celcius,
                           response=response,
                           city_name=city_name,
                           wind_speed=wind_speed,
                           timezone=timezone,
                           timestamp=timestamp,
                           temp_k=temp_k,
                           temp_c=temp_c,
                           dt=dt)


@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/resultsimperial')
def resultsimperial():
    return render_template('resultsimperial.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/ques')
def ques():
    return render_template('?.html')


if __name__ == '__main__':
    app.run(debug=True)
