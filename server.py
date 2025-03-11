from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve


app = Flask(__name__)
app.config['DEBUG'] = False
app.debug = False
app.config['ENV'] = 'production'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Sacramento"


    weather_data = get_current_weather(city)

    # city is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
   )

from waitress import serve
from server import app 


if __name__ == "__main__":
    app.config['DEBUG'] = False
    serve(app, host='0.0.0.0', port=8000)