# Challenge Data Analytics - Nivel Inicial

## Nivel inicial:

1. Obtener el archivo de la fuente que escojamos archivos de fuente utilizando Google Colab y la librería requests, por último debe almacenarse en forma local en formato CSV:

Librerias necesarias:

```python
from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json
```

### API de datos abiertos del clima:

Descripción: Algunas APIs públicas proporcionan datos históricos o en tiempo real sobre el clima, incluidas temperaturas, precipitaciones, vientos, etc.
API: https://openweathermap.org/api

1. Solicitud: Debes hacer una solicitud HTTP a la API para obtener los datos en formato JSON y luego convertirlos a CSV utilizando Python.

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

1. Organizar los archivos en rutas siguiendo la siguiente estructura:
“data_analytics\openweather\tiempodiario_yyyymmdd.csv”
La fecha de la nomenclatura es la fecha del tiempo tomado.
2. buscar estas ciudades:

```python
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
```

1. Realizar los comentarios correspondientes para una correcta comprensión del código. (#)

## Getting started
1. Es recomendable crear un entorno virtual e instalar las dependencias:

    Bash:
    ```bash
    python -m venv env
    source env/Scripts/activate
    pip install -r requirements.txt
    ```
    Windows cmd:
    ```cmd
    python -m venv env
    env/Scripts/activate
    pip install -r requirements.txt
    ```

2. Crear el archivo .env:
    
    ```ini
    api_key = Tu api key va aquí
    ```

3. Lanzar la app:
    ```bash
    python main.py
    ```
