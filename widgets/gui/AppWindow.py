from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QMainWindow, QToolBar
from PyQt5.QtGui import QIcon
from widgets.location.SearchBar import SearchWidget

# Primary window for the application

class AppWindow(QMainWindow):
    def __init__(self):
        '''Initializes the main window for the application'''
        super().__init__()

        # Widgets
        location_widget = QWidget()
        central_widget = QWidget()
        search_bar = SearchWidget(location_widget)
        
        # Layout¨
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Window settings
        self.setWindowTitle("WeatherAPI")
        self.setWindowIcon(QIcon("images/weather_logo.png"))
        

