# Data Analytics Challenge - Nivel Medio
1. La descarga, procesamiento y actualización de la información en la base de datos
se debe poder ejecutar desde un archivo .py
2. El proyecto debe poder deployarse en forma sencilla siguiendo un readme, que al
menos contenga las instrucciones para:

    - Utilizarse creando un entorno virtual (venv)
    - Instalar las dependencias necesarias con pip.
    - Configurar la conexión a la base de datos.

Enpoint: 

BASE_URL = "[https://api.openweathermap.org/data/2.5/onecall/timemachine?"](https://api.openweathermap.org/data/2.5/onecall/timemachine?%22)

Tomar 5 días de cada ciudad.

Normalizar Tabla teniendo en cuenta el formato y el tipo de dato contenido en cada columna.

1. Las configuraciones necesarias para que el proyecto se ejecute deben poder
configurarse desde un archivo config.py
2. Realizar los comentarios correspondientes para su correcta documentación con docstrings(’’’ ‘’’).

## Bases de datos

Se deben dejar disponibles los scripts de creación de las tablas utilizadas.
Conexión a la base de datos:
● Los datos se deben almacenar en una base PostgreSQL.
● La conexión a la base de datos se debe implementar con la librería y ORM
SQLalchemy.
● Se recomienda ver la funcionalidad de pandas dataframe.to_sql.

## **Herramientas para el procesamiento de datos:**

En esta etapa del proyecto, se utilizará la librería Pandas para procesar los datos obtenidos y almacenarlos en la base de datos PostgreSQL.

**Explicación:**

1. La librería Pandas se utilizará para leer los datos en formato CSV y procesarlos antes de cargarlos en la base de datos.

**Parte Práctica:**
Ya hemos utilizado la librería Pandas en la parte práctica anterior, donde hemos procesado los datos y los hemos cargado en la base de datos utilizando esta herramienta.

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
    api_key=my_api_key
    DB_HOST=my_db_host
    DB_PORT=my_db_port
    DB_NAME=my_db_name
    DB_USER=my_db_user
    DB_PASS=my_db_password
    ```

3. Lanzar la app:
    ```bash
    python main.py
    ```
