from PyQt5.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QToolBar
from PyQt5.QtGui import QIcon
from widgets.location.SearchBar import SearchWidget
from widgets.gui.WeatherResult import WeatherResult

# Primary window for the application

class AppWindow(QMainWindow):
    def __init__(self):
        '''Initializes the main window for the application'''
        super().__init__()
        self.setWindowTitle("WeatherAPI")
        self.setWindowIcon(QIcon("images/app_icons/weather_logo.png"))
        self.resize(900, 600)

        self.central_widget = QWidget()
        self.result_widget = WeatherResult()
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.result_widget)

        # Search bar
        self.search_bar = QToolBar()
        self.search_bar.addWidget(SearchWidget())
        self.search_bar.setMovable(False)
        self.addToolBar(self.search_bar)

        self.setCentralWidget(self.central_widget)
        
      




