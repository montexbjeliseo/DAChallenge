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


con_str = f"postgresql://{cfg['DB_USER']}:{cfg['DB_PASS']}@{cfg['DB_HOST']}:{cfg['DB_PORT']}/{cfg['DB_NAME']}"

# Configuración de la base de datos
engine = create_engine(con_str)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def store_weather_data(city, dt, temp, my_timezone, sunrise, sunset):
    """Almacenar datos meteorológicos en la base de datos."""
    session = Session()
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
    session.close()
