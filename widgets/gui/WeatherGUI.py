from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from widgets.location.SearchBar import SearchWidget
from .TitleBar import WeatherTitle

# This class handles the creation of a custom MainWindow for application
class WeatherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint) # Removes original title bar
        self.setMenuWidget(WeatherTitle(self))

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)
        layout.addWidget(SearchWidget())

       