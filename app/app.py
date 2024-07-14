from flask import Flask, render_template, request
from util import get_weather
from util import get_coords

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def weather():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if city:
        coords = get_coords.Coordinates()
        coords = coords.get_cooords(city)
        Weather = get_weather.Weather(coords.latitude, coords.longitude)
        weather_data = Weather.get_weather().json()
    else:
        Weather = get_weather.Weather(lat, lon)
        weather_data = Weather.get_weather().json()
        city = ""
    return render_template("weather.html", **weather_data, city=city)


if __name__ == "__main__":
    app.run(debug=True)
