from utils.datetime_utils import format_datetime


def clean_data(city_raw_data_list):
    cleaned = {}
    if city_raw_data_list:
        city_raw_data = city_raw_data_list[0]
        city_raw_data['']
        cleaned["city"] = city_raw_data["city"]
        
        data = city_raw_data["data"]
        cleaned["dt"] = format_datetime(data["current"]["dt"]).isoformat()
        cleaned["temp"] = data["current"]["temp"]
        cleaned["sunrise"] = format_datetime(data["current"]["sunrise"]).time().isoformat()
        cleaned["sunset"] = format_datetime(data["current"]["sunset"]).time().isoformat()
        cleaned["timezone"] = data["timezone"]
    
    return cleaned
    