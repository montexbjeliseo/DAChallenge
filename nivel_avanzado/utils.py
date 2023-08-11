from datetime import datetime
import pandas as pd

def time(ts, tz = 0):
    if isinstance(ts, str):
        ts = int(ts)
    
    if isinstance(tz, str):
        tz = int(tz)
    return datetime.utcfromtimestamp(ts + tz).strftime("%H:%Mhs")

def day(ts, tz = 0):
    if isinstance(ts, str):
        ts = int(ts)
    
    if isinstance(tz, str):
        tz = int(tz)
    day_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return day_names[datetime.utcfromtimestamp(ts + tz).weekday()]

def clean_forecast_data(forecast_data_list, tz = 0):
    
    dfs = []
    for forecast_data in forecast_data_list:
        wdf = pd.json_normalize(forecast_data["weather"][0]).add_prefix("weather_")

        del forecast_data['weather']

        dfc = pd.json_normalize(forecast_data)

        dfc = pd.concat([dfc, wdf], axis=1)

        dfs.append(dfc)

    df = pd.concat(dfs, axis=0)
    df["day"] = df["dt"].apply(lambda x: day(x, tz))
    df["time"] = df["dt"].apply(lambda x: time(x, tz))
    return df

def format_forecast_data(forecast_data):
    pass