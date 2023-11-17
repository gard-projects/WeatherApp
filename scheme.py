from sqlalchemy import String, Float, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Table for weather searches
class Weather(Base):
    __tablename__ = "weather"
    location_name = Column("location_name", String(30), primary_key=True)
    air_pressure_at_sea_level = Column("air_pressure_at_sea_level", Float)
    air_temp = Column("air_temp", Float)
    cloud_area_fraction = Column("cloud_area_fraction", Float)
    relative_humidity = Column("relative_humidity", Float)
    wind_from_direction = Column("wind_from_direction", Float) # Direction in degrees
    wind_speed = Column("wind_speed", Float)

    def __init__(self, location_name, air_pressure_at_sea_level, air_temp, cloud_area_fraction, relative_humidity, wind_from_direction, wind_speed):
        ''' Constructor for creating a Weather object'''
        self.location_name = location_name
        self.air_pressure_at_sea_level = air_pressure_at_sea_level
        self.air_temp = air_temp
        self.cloud_area_fraction = cloud_area_fraction
        self.relative_humidity = relative_humidity
        self.wind_from_direction = wind_from_direction
        self.wind_speed = wind_speed

    def __repr__(self):
        '''Method for representing the a weather object as string'''
        return f"<Location: {self.location_name}, Temperature: {self.air_temp}, Wind speed: {self.wind_speed}>"

