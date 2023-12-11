from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scheme import Base, Weather
from geopy.geocoders import Nominatim
import requests
import os
from datetime import datetime
from widgets.location.Location import Location

"""
This file contains functions for performing operations on database and on the API
"""

def db_setup():
    '''Create database (if needed)'''
    engine = create_engine("sqlite:///weather.db", echo=True)

    is_db_present = os.path.isfile("weather.db")
    if is_db_present is False:
        Base.metadata.create_all(bind=engine)

def db_fetch_location(location_name: str) -> Location:
    '''Fetches a specific location from the database if it is present'''
    engine = create_engine("sqlite:///weather.db")
    Session = sessionmaker(engine)
    session = Session()

    location = session.query(Weather).filter_by(location_name=location_name).first()
    session.close()
    return location

def db_add_location(location: Location):
    '''Add a new location to the database'''
    engine = create_engine("sqlite:///weather.db")
    Session = sessionmaker(engine)
    session = Session()

    # Create db object from location
    new_location = Weather(location.location_name, location.expire_date, location.last_modified, 
                           location.wind_speed, location.air_temperature, location.weather_symbol, 
                           location.percipitation_amount)

    session.add(new_location)
    session.commit()
    session.close()

def db_update_location(location: Location):
    '''Updates an existing location in the database'''
    db_engine = create_engine("sqlite:///weather.db")
    Session = sessionmaker(db_engine)
    session = Session()

    db_location = db_fetch_location(location.location_name) # Location will not be None

    # Update attributes of location
    db_location.expires = location.expire_date
    db_location.last_modified = location.last_modified
    db_location.wind_speed = location.wind_speed
    db_location.air_temperature = location.air_temperature
    db_location.weather_symbol = location.weather_symbol
    db_location.percipitation_amount = location.percipitation_amount
    session.commit()
    session.close()

def create_location(location_name: str, expire_date: datetime, last_modified: datetime, location_data: dict) -> Location:
    '''Creates a location object from a dictionary of data'''
    wind_speed = location_data["data"]["instant"]["details"]["wind_speed"]
    air_temperature = location_data["data"]["instant"]["details"]["air_temperature"]
    weather_symbol = location_data["data"]["next_1_hours"]["summary"]["symbol_code"]

    # Check if there is any precipitation
    if location_data["data"]["next_1_hours"]["details"]:
        precipitation_amount = location_data["data"]["next_1_hours"]["details"]["precipitation_amount"]
    else:
        precipitation_amount = 0.0
    
    return Location(location_name, expire_date, last_modified, wind_speed, air_temperature, weather_symbol, precipitation_amount)

def find_coordinates(location: str) -> tuple[float ,float] | None:
    '''Finds the coordinates of a given location (longitude and latitude)'''
    geolocator = Nominatim(user_agent="WeatherAPI")
    result = geolocator.geocode(location)
    
    # Handle case where location is not found
    if result is None:
        return 

    return round(result.latitude, 3), round(result.longitude, 3)

def weather_request(location_name: str, altitude=None) -> Location | None:
    '''Fetches weather data for a given location'''
    result = find_coordinates(location_name)
    if result is None:
        return None
    latitude, longitude = result

    base_url = "https://api.met.no/weatherapi/locationforecast/2.0/"
    data_method = "compact"
    params = {"lat": latitude, 
              "lon": longitude, 
              "altitude": altitude}
    headers = {
        "User-Agent": "WeatherApp/1.0 (https://github.com/gard-projects/WeatherApp)"
    }

    # Check database first for location
    db_loc = db_fetch_location(location_name)
    if db_loc:
        db_loc = Location.from_schema(db_loc)
        if db_loc.expire_date > datetime.now():
            return db_loc
        else:
            # Location has expired, update it
            response = requests.get(base_url + data_method, params=params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                expire_date = datetime.strptime(response.headers["Expires"], "%a, %d %b %Y %H:%M:%S GMT")
                last_modified = datetime.strptime(response.headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S GMT")
                new_location = create_location(location_name, expire_date, last_modified, data["properties"]["timeseries"][0])
                db_update_location(new_location)
                return new_location
            else:
                print("Could not fetch data from API, returning old data")
                return db_loc
    else:
        # Location is not in database, add it
        response = requests.get(base_url + data_method, params=params, headers=headers)

        if response.status_code != 200:
            print("Could not fetch data from API, returning None")
            return None
        
        data = response.json()
        expire_date = datetime.strptime(response.headers["Expires"], "%a, %d %b %Y %H:%M:%S GMT")
        last_modified = datetime.strptime(response.headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S GMT")
        new_location = create_location(location_name, expire_date, last_modified, data["properties"]["timeseries"][0])
        db_add_location(new_location)
        return new_location
