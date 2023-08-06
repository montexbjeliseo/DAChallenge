from datetime import datetime

def time(ts, tz):
    if isinstance(ts, str):
        ts = int(ts)
    
    if isinstance(tz, str):
        tz = int(tz)
    return datetime.utcfromtimestamp(ts + tz).strftime("%H:%Mhs")