from api import *
from datetime_utils import dtnow


if __name__ == '__main__':
    print("App has been started")
    
    weather_data = get_last_five_days_cities_weather_data()
    
    weather_data.to_csv(f'weather_data_{dtnow()}.csv', index=False)
    
    