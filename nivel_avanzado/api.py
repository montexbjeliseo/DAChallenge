import requests 
from datetime import datetime


def get_current_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={'821f98f224c0263d251c23e1d435e937'}"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'icon': data['weather'][0]['icon'],
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
        }
        return weather

    return None

