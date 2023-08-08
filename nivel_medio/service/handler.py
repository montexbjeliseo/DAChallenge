from settings.config import *
from repos.weather_data import store_weather_data
from logic.api_weather import get_last_five_days_cities_weather_data as logic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def store_data():
    weather_data = logic()
    try:
        engine = create_engine(CON_STR)
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        raise e

    for data in weather_data:
        if data:
            dt = data["dt"]
            city = data["city"]
            temp = data["temp"] 
            my_timezone = data["timezone"]
            sunrise = data["sunrise"] 
            sunset = data["sunset"]
            
            #store_weather_data(**data)
            store_weather_data(city, dt, temp, my_timezone, sunrise, sunset,session)
    
    session.close()