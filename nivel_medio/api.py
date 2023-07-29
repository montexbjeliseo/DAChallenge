import requests
from config import *
from datetime_utils import *
from file_utils import *


def request_data(city: str = None, coord: str = None, dt: str = None) -> dict:
    """
    Recibe "city" que es el nombre de la ciudad, en formato string
    Hace una solicitud a la api y si el código de respuesta
    Es 200, devuelve la data en formato json
    De lo contrario, intentará manejar las excepciones
    """

    try:
        if city:
            params = {"q": city, "units": UNITS, "appid": API_KEY, "dt": dt}

            response = requests.get(BASE_URL, params)
        else:
            response = requests.get(f"{BASE_URL}?{coord}&appid={API_KEY}&units={UNITS}&dt={dt}")

        response.raise_for_status()

        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except KeyError as e:
        print(f"Error en el formato de respuesta de la API: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")


def join_data(data_list) -> pd.DataFrame:
    dfs = []
    for data in data_list:
        wdf = pd.json_normalize(data["weather"][0]).add_prefix("weather_")

        keys_to_remove = ["weather", "base", "timezone", "cod"]

        for key in keys_to_remove:
            del data[key]

        dfc = pd.json_normalize(data)

        dfc = pd.concat([dfc, wdf], axis=1)

        dfs.append(dfc)

    return pd.concat(dfs, axis=0)


def get_cities_weather_data(dt) -> (pd.DataFrame, list):
    """
    Obtener los datos del clima
    A partir de la lista de ciudades
    Devuelve un conjunto de respuestas
    """

    # Acá almacenamos los datos de todas las ciudades
    # Para luego ser exportadas
    cities_data = []
    unreached_cities = []

    for city in cityList:
        city_data = request_data(city=city, dt=dtnow())
        if city_data:
            city_data["dt"] = format_datetime(city_data["dt"])
            cities_data.append(city_data)
        else:
            unreached_cities.append(city)

    for coord in coordList:
        coord_data = request_data(coord=coord, dt=dtnow())
        if coord_data:
            coord_data["dt"] = format_datetime(coord_data["dt"])
            cities_data.append(coord_data)
        else:
            unreached_cities.append(coord)

    return join_data(cities_data), unreached_cities

def get_last_five_days_cities_weather_data():
    ts = dtnow()
    # Un dia en unix timestamp format
    oditsu = 86400
    
    dfs = []
    for i in range(5):
        df, unreached =  get_cities_weather_data(dt=ts)
        dfs.append(df)
        ts-=oditsu
        
    return pd.concat(dfs, axis=0)