import requests
from utils import time, clean_forecast_data, day
from dotenv import load_dotenv
import os

_= load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

API_KEY = os.getenv("API_KEY")

def get_current_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}&lang=es"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        timezone = data["timezone"]
        
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "pressure": data["main"]["pressure"],
            "visibility": int(data["visibility"] / 1000),
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"],
            "sunrise": time(data["sys"]["sunrise"], timezone),
            "sunset": time(data["sys"]["sunset"], timezone),
        }
        return weather

    return None

def get_forecast_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}&lang=es"
    response = requests.get(url)
    response_data = response.json()
    
    if response.status_code == 200:
        tz = response_data["city"]["timezone"]
        response_data_list = response_data["list"]
        
        cleaned_data_list = clean_forecast_data(response_data_list, tz)
        return cleaned_data_list
            
    return None

