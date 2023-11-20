from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scheme import Base, Weather
from geopy.geocoders import Nominatim
import requests
import os

"""
This file contains functions for performing operations on database and on the API
"""


def db_setup():
    '''Create database (if needed)'''
    engine = create_engine("sqlite:///weather.db", echo=True)

    is_db_present = os.path.isfile("weather.db")
    if is_db_present is False:
        Base.metadata.create_all(bind=engine)

def db_add_location():
    '''Adds a new location to the database'''
    engine = create_engine("sqlite:///weather.db")
    Session = sessionmaker(engine) # Creates a class
    session = Session() # Create an instance

    weather1 = Weather("London", 4.0, 4.0, 4.0, 4.0, 4.0, 4.0)
    session.add(weather1)
    session.commit()

def find_coordinates(location: str) -> (float,float):
    '''Finds the coordinates of a given location (longitude and latitude)'''
    geolocator = Nominatim(user_agent="WeatherAPI")
    result = geolocator.geocode(location)

    return round(result.latitude, 3), round(result.longitude, 3)

def weather_request(location: str, altitude=None) -> tuple:
    '''Fetches weather data for a given location'''
    latitude, longitude = find_coordinates(location)
    base_url = "https://api.met.no/weatherapi/locationforecast/2.0/"
    data_method = "compact"
    params = {"lat": latitude, 
              "lon": longitude, 
              "altitude": altitude}
    headers = {
        "User-Agent": "WeatherApp/1.0 (https://github.com/gard-projects/WeatherApp)"
    }

    # Make request to API (Met.no)
    response = requests.get(f"{base_url}{data_method}", params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Could not fetch data from API, error code: {response.status_code}")
        return None
