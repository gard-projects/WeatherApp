from sqlalchemy import String, Float, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Table for weather searches
class Weather(Base):
    __tablename__ = "weather"
    location_name = Column("location_name", String(30), primary_key=True)
    expires = Column("expires", String(30))
    last_modified = Column("last_modified", String(30))
    wind_speed = Column("wind_speed", Float)
    air_temperature = Column("air_temperature", Float)
    weather_symbol = Column("weather_symbol", String(50))
    percipitation_amount = Column("percipitation_amount", Float)

    def __init__(self, location_name, expires, last_modified, wind_speed, air_temperature, weather_symbol, percipitation_amount):
        self.location_name = location_name
        self.expires = expires
        self.last_modified = last_modified
        self.wind_speed = wind_speed
        self.air_temperature = air_temperature
        self.weather_symbol = weather_symbol
        self.percipitation_amount = percipitation_amount
        

    def __repr__(self):
        '''Method for representing the a weather object as string'''
        return f"<Location: {self.location_name}, Temperature: {self.air_temperature}, Wind speed: {self.wind_speed}>"

