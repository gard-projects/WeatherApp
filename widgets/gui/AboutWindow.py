from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QIcon

# This class features the about window
class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About WeatherAPI")
        self.setWindowIcon(QIcon("images/app_icons/weather_logo.png"))

        text_widget = QWidget()
        about_text = QLabel('''
                        This is a simple weather application made by Gard, which sends requests to
                        Met's API to fetch weather data. This data is then displayed on the website.
        
                        The application itself is meant for educational purposes, simply to learn PyQt5, 
                        SQLAlchemy and other libraries like requests and geopy (in Python).
                     ''', text_widget)
        self.setCentralWidget(text_widget)
        self.resize(900, 600)