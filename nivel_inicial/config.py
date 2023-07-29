import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

API_KEY = os.getenv('api_key')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
UNITS = 'metric'
FOLDER = 'data_analytics/openweather'
FILENAME = FOLDER + '/tiempodiario'

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")


cityList = [
    "London",
    "New York",
    "Cordoba",
    "Taipei",
    "Buenos Aires",
    "Mexico City",
    "Dublin",
    "Tiflis",
    "Bogota",
    "Tokio",
]

coordList = [
    "lat=31&lon=64",
    "lat=40&lon=-73",
    "lat=-31&lon=-64",
    "lat=25&lon=64",
    "lat=-34&lon=-58",
    "lat=19&lon=-99",
    "lat=53&lon=6",
    "lat=41&lon=44",
    "lat=4&lon=74",
    "lat=35&lon=139",
]
