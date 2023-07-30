import requests
from config import *
from datetime_utils import *
from file_utils import *
from clean_data import clean_data


def request_data(city: str = None, coord: str = None, dt: str = None):
    """
    Recibe "city" que es el nombre de la ciudad, en formato string
    Hace una solicitud a la api y si el código de respuesta
    Es 200, devuelve la data en formato json
    De lo contrario, intentará manejar las excepciones
    """

    try:
        params = {
            "lat": coord[0],
            "lon": coord[1],
            "units": UNITS,
            "appid": API_KEY,
            "dt": dt,
            "exclude": "exclude=minutely, hourly",
        }

        response = requests.get(BASE_URL, params)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except KeyError as e:
        print(f"Error en el formato de respuesta de la API: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")


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

