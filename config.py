import os


API_KEY = os.getenv('api_key')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cityList = [
    "London",
    "New York",
    "Cordoba",
    "Taipei",
    "Buenos Aires",
    "Mexico DF",
    "Dublin",
    "Tilfis",
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
