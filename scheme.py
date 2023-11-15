from sqlalchemy import String, Integer, Float, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Table for weather
class Weather(Base):
    __tablename__ = "weather"
    air_pressure_sea = Column("air_pressure_sea", Float)
    air_temp = Column("air_temp", Float)
    cloud_area_fraction = Column("cloud_area_fraction", Float)
    relative_humidity = Column("relative_humidity", Float)
    wind_from_direction = Column("wind_from_direction", Float)
    wind_speed = Column("wind_speed", Float)

