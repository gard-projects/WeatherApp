# WeatherApp
An application coded in Python which analyzes weather data

The application features a search bar where the user can enter a location and find the current weather. The GUI features a table which displays relevant information about the current location. 

The API sends a request to MET's API, by sending the respective latitude and longitude for the location. These parameters are found using geopy's libraries. The application first looks at the database for the given location, and refreshes its contents if the data has expired or if it is not present. 
