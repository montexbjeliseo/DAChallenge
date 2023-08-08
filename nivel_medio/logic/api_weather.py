import requests
from utils.clean_data import clean_data
from utils.datetime_utils import dtnow
from settings.config import *

def request_data(city: str = None, coord: str = None, dt: str = None):
    """
    Recibe "city" que es el nombre de la ciudad, en formato string
    Hace una solicitud a la api y si el código de respuesta
    Es 200, devuelve la data en formato json
    De lo contrario, intentará manejar las excepciones
    """

    params = {
        "lat": coord[0],
        "lon": coord[1],
        "units": UNITS,
        "appid": cfg['API_KEY'],
        "dt": dt,
        "exclude": "exclude=minutely, hourly",
    }
    logger.info(f"params: {params}\n\n")
    response = requests.get(BASE_URL, params)

    try:
        response.raise_for_status()  # Genera una excepción para errores HTTP (status_code >= 400)
        return response.json()
    except requests.exceptions.HTTPError as e:
        logger.error(f"Error en la solicitud: {e}\nCódigo de estado: {response.status_code}\nMensaje de error: {response.text}\n\n")
        raise 
    except Exception as e:
        logger.error(f"Error desconocido: {e}\n\n")
        raise


def get_cities_weather_data(dt):
    """
    Obtener los datos del clima
    A partir de la lista de ciudades
    Devuelve un conjunto de respuestas
    """

    # Acá almacenamos los datos de todas las ciudades
    # Para luego ser exportadas
    cities_data = []

    for city, coord in cityCoord.items():
        coord_data = request_data(coord=coord, dt=dt)
        if coord_data:
            city_data = {}
            city_data["city"] = city
            city_data["data"] = coord_data
            cities_data.append(city_data)
    return cities_data


def get_last_five_days_cities_weather_data():
    # Este preciso momento en unix timestamp format
    ts = dtnow()
    # Un dia en unix timestamp format
    oditsu = 86400
    
    cleaned_data_list = []
    for i in range(5):
        df = get_cities_weather_data(ts)

        ts -= oditsu
        # Limpiamos y agregamos a la lista
        cleaned_data_list.append(clean_data(df))
        
    return cleaned_data_list

