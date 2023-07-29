from datetime import datetime, timedelta



def formatted_date_time():
    return datetime.now().strftime("%Y%m%d")

def format_datetime(unix_timestamp):

    # Convertir el tiempo Unix a una fecha y hora en UTC
    utc_datetime = datetime.utcfromtimestamp(unix_timestamp)

    gmt3_offset = timedelta(hours=-3)
    argentina_datetime = utc_datetime + gmt3_offset
    
    return argentina_datetime

def to_unix_timestamp(argentina_datetime):
    # Restar la diferencia de tiempo correspondiente al huso horario de Argentina para obtener la fecha y hora en UTC
    gmt3_offset = timedelta(hours=-3)
    utc_datetime = argentina_datetime - gmt3_offset

    # Convertir la fecha y hora en UTC a un tiempo Unix (timestamp)
    unix_timestamp = int((utc_datetime - datetime(1970, 1, 1)) / timedelta(seconds=1))

    return unix_timestamp

def dtnow():
    return to_unix_timestamp(datetime.now())
