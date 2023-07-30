import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

API_KEY = os.getenv('api_key')
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
UNITS = 'metric'
FOLDER = 'data_analytics/openweather'
FILENAME = FOLDER + '/tiempodiario'

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

cityCoord = {
    "Resistencia, AR": (-27.4511, -58.9866),
    # "City of London, GB": (51.512791, -0.09184),   
    # "New York, US":    (40.714272, -74.005966),
    # "Cordoba, ES":    (37.90448, -4.77768),  
    # "Taipei, TW":    (25.025881, 121.651611),
    # "Ciudad Autónoma de Buenos Aires, AR":    (-34.599998, -58.450001),
    # "Mexico City, MX":    (19.428471, -99.127663),   
    # "Dublin City, IE (Ireland)":    (53.355122, -6.24922),     
    # "Tbilisi, GE (Georgia)": (41.694111, 44.833679),   
    # "Bogotá, CO":    (4.60971, -74.081749),     
    # "Tokyo, JP": (35.689499, 139.691711)    
}