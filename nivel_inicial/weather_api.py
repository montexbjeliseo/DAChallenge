import config
import requests
import json
from datetime import datetime, timedelta
import pandas as pd

from alive_progress import alive_bar


def request_data(city: str = None, coord: str = None):
    """
    Recibe "city" que es el nombre de la ciudad, en formato string
    Hace una solicitud a la api y si el código de respuesta
    Es 200, devuelve la data en formato json
    De lo contrario, intentará manejar las excepciones
    """

    try:
        if city:
            params = {"q": city, "units": config.UNITS, "appid": config.API_KEY}

            response = requests.get(config.BASE_URL, params)
        else:
            response = requests.get(
                f"{config.BASE_URL}?{coord}&appid={config.API_KEY}&units{config.UNITS}"
            )

        response.raise_for_status()

        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except KeyError as e:
        print(f"Error en el formato de respuesta de la API: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")


def export_to_json(data: list, filename: str):
    """Exportar datos a un archivo JSON."""
    with open(filename, "w") as file:
        json.dump(data, file)


def save_to_file(data, filename):
    with open(filename, "w") as file:
        file.write(data)
        file.close()


def formatted_date_time():
    return datetime.now().strftime("%Y%m%d")

def format_datetime(unix_timestamp):

    # Convertir el tiempo Unix a una fecha y hora en UTC
    utc_datetime = datetime.utcfromtimestamp(unix_timestamp)

    gmt3_offset = timedelta(hours=-3)
    argentina_datetime = utc_datetime + gmt3_offset
    
    return argentina_datetime


def export_to_csv(data_list, filename):
    dfs = []
    for data in data_list:
        wdf = pd.json_normalize(data["weather"][0]).add_prefix("weather_")

        keys_to_remove = ["weather", "base", "timezone", "cod"]

        for key in keys_to_remove:
            del data[key]

        dfc = pd.json_normalize(data)

        dfc = pd.concat([dfc, wdf], axis=1)

        dfs.append(dfc)

    df = pd.concat(dfs, axis=0)

    df.to_csv(filename, index=False)


def get_cities_weather_data():
    """
    Obtener los datos del clima
    A partir de la lista de ciudades
    Devuelve un conjunto de respuestas
    """

    # Acá almacenamos los datos de todas las ciudades
    # Para luego ser exportadas
    cities_data = []
    unreached_cities = []

    with alive_bar(len(config.cityList), title='Processing', length=60) as bar:
        for city in config.cityList:
            bar()
            city_data = request_data(city=city)
            if city_data:
                city_data["dt"] = format_datetime(city_data["dt"])
                cities_data.append(city_data)
            else:
                unreached_cities.append(city)
    
    with alive_bar(len(config.coordList), title='Processing', length=60) as bar:
        for coord in config.coordList:
            bar()
            coord_data = request_data(coord=coord)
            if coord_data:
                coord_data["dt"] = format_datetime(coord_data["dt"])
                cities_data.append(coord_data)
            else:
                unreached_cities.append(coord)

    print("_" * 50)

    unreached_cities_filename = (
        f"{config.FOLDER}/no_alcanzadas_{formatted_date_time()}.lst"
    )
    weather_data_filename = f"{config.FILENAME}_{formatted_date_time()}.csv"

    export_to_json(unreached_cities, unreached_cities_filename)
    print(
        f"Se guardó la lista de ciudades no alcanzadas en {unreached_cities_filename}"
    )

    export_to_csv(cities_data, weather_data_filename)
    print(f"Los datos del tiempo se guardaron en {weather_data_filename}")

    return cities_data
