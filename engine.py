from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scheme import Base, Weather
import os

def db_setup():
    '''Create database (if needed)'''
    engine = create_engine("sqlite:///weather.db")

    is_db_present = os.path.isfile("weather.db")
    if is_db_present is False:
        Base.metadata.create_all(bind=engine)

def db_add_location():
    '''Adds a new location to the database'''
    engine = create_engine("sqlite:///weather.db")
    Session = sessionmaker(engine)
    session = Session()

    weather1 = Weather("London", 4.0, 4.0, 4.0, 4.0, 4.0, 4.0)
    session.add(weather1)
    session.commit()
