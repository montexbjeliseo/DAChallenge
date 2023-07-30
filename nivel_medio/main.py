from api import *
from weather_data import store_weather_data


def store_data(weather_data):
    for data in weather_data:
        dt = data["dt"]
        city = data["city"]
        temp = data["temp"] 
        my_timezone = data["timezone"]
        sunrise = data["sunrise"] 
        sunset = data["sunset"]
        
        #store_weather_data(**data)
        store_weather_data(city, dt, temp, my_timezone, sunrise, sunset)

def main():
    print("App has been started")
    weather_data = get_last_five_days_cities_weather_data()
    store_data(weather_data)

if __name__ == '__main__':
    main()
    
    