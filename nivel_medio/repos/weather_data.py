from datetime import datetime
from sqlalchemy import create_engine, Column, DateTime, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from settings.config import *

# Crear una clase base declarativa para las clases ORM
Base = declarative_base()

# Definir la estructura de la tabla en la base de datos
class WeatherData(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    dt = Column(DateTime)
    temp = Column(Integer)
    my_timezone = Column(String)
    sunrise_local = Column(String)
    sunset_local = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now())

engine = create_engine(CON_STR)
Base.metadata.create_all(engine)

def store_weather_data(city, dt, temp, my_timezone, sunrise, sunset, session):
    """Almacenar datos meteorológicos en la base de datos."""
    

    weather_data = WeatherData(
        city=city,
        dt=dt,
        temp=temp,
        my_timezone=my_timezone,
        sunrise_local=sunrise,
        sunset_local=sunset,
    )
    session.add(weather_data)
    session.commit()
    