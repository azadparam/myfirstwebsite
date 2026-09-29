from flask import Flask, render_template
from random import choice
weather_combos = ["Rainy", "Sunny", "Cloudy", "Snowy", "Windy", "Stormy", "Foggy", "Hazy", "Drizzling"]
app = Flask(__name__)

greeter = "Hello, this is a home page and i just used Python's Flask module in this website, this message is also coming from python to HTML, Welcome to my website"

@app.route('/')
def home():
    return render_template('index.html', greeting=greeter)

@app.route('/weather')
def send_weather_info():
    weather_part = choice(weather_combos)
    weather = (f"The weather today is {weather_part}. And if you ACTUALLY search it up and say 'thats wrong' then take the L i didnt specify the place so the weather is correct, somewhere.")
    return render_template('weather.html', user_weather=weather)

if __name__ == '__main__':
    app.run(debug=False)

