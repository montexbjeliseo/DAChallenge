import config
import requests
import json
from datetime import datetime
import pandas as pd

def request_data_by_city(city: str):
    """
    Recibe "city" que es el nombre de la ciudad, en formato string
    Hace una solicitud a la api y si el código de respuesta
    Es 200, devuelve la data en formato json
    De lo contrario, intentará manejar las excepciones
    """
    print("*"*50)
    print(f"Solicitando datos")
    print(f"Ciudad: \"{city}\"")
    print(f"Unidad: \"{config.UNITS}\"")
    
    params = {"q": city, "units": config.UNITS, "appid": config.API_KEY}

    try:
        
        response = requests.get(config.BASE_URL, params)
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
    with open(filename, 'w') as file:
        json.dump(data, file)
        
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
        file.close()

def formatted_date_time():
    return datetime.now().strftime("%Y%m%d")
        
def export_to_csv(data_list, filename):
    
    dfs = []
    for data in data_list:
        wdf = pd.json_normalize(data['weather'][0]).add_prefix('weather_')
        
        keys_to_remove = ['weather', 'base', 'timezone', 'id', 'name', 'cod']

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
    
    for city in config.cityList:
        city_data = request_data_by_city(city)
        if city_data:
            cities_data.append(city_data)
        else:
            unreached_cities.append(city)
    
    export_to_json(unreached_cities, f'{config.FOLDER}/no_alcanzadas_{formatted_date_time()}.lst')    
    export_to_csv(cities_data, f'{config.FILENAME}_{formatted_date_time()}.csv')
            
    return cities_data