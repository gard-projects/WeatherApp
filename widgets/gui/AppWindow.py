from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QMainWindow, QToolBar
from PyQt5.QtGui import QIcon
from widgets.location.SearchBar import SearchWidget

# Primary window for the application

class AppWindow(QMainWindow):
    def __init__(self):
        '''Initializes the main window for the application'''
        super().__init__()
        self.setWindowTitle("WeatherAPI")
        self.setWindowIcon(QIcon("images/weather_logo.png"))
        self.resize(800, 600)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Search bar
        self.search_bar = QToolBar()
        self.search_bar.addWidget(SearchWidget())
        self.search_bar.setMovable(False)
        self.addToolBar(self.search_bar)
        
      




