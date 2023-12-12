from datetime import datetime
from textwrap import dedent

# Helper class for storing locations
class Location:
    def __init__(self, 
                 location_name: str,
                 expires: datetime, 
                 last_modified: datetime, 
                 wind_speed: float, 
                 air_temperature: float, 
                 weather_symbol: str, 
                 percipitation_amount: float):
        
        self.location_name = location_name
        self.expire_date = expires
        self.last_modified = last_modified
        self.wind_speed = wind_speed
        self.air_temperature = air_temperature
        self.weather_symbol = weather_symbol
        self.percipitation_amount = percipitation_amount

    def __str__(self):
        return dedent(f"""
            Location: {self.location_name}\n
            Expires: {self.expire_date}\n
            Last modified: {self.last_modified}\n
            Wind speed: {self.wind_speed}\n
            Air temperature: {self.air_temperature}\n
            Weather symbol: {self.weather_symbol}\n
            Percipitation amount: {self.percipitation_amount}
        """).strip()

    @classmethod
    def from_schema(cls, db_object):
        '''Converts the database object to a Location object'''
        return cls(
            location_name = db_object.location_name,
            expires = datetime.strptime(db_object.expires, "%Y-%m-%d %H:%M:%S"),
            last_modified = datetime.strptime(db_object.last_modified, "%Y-%m-%d %H:%M:%S"),
            wind_speed = db_object.wind_speed,
            air_temperature = db_object.air_temperature,
            weather_symbol = db_object.weather_symbol,
            percipitation_amount = db_object.percipitation_amount
        )