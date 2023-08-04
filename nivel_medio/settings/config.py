from dotenv import dotenv_values
import logging

cfg = { ** dotenv_values('.env') }

BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
UNITS = 'metric'
FOLDER = 'data_analytics/openweather'
FILENAME = FOLDER + '/tiempodiario'
CON_STR = f"postgresql://{cfg['DB_USER']}:{cfg['DB_PASS']}@{cfg['DB_HOST']}:{cfg['DB_PORT']}/{cfg['DB_NAME']}"

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

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)