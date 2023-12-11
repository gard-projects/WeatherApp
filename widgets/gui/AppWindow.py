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
        self.search_widget = SearchWidget()
        # Link custom signal (update location data when searching for a new/existing location)
        self.search_widget.location_request.connect(self.result_widget.update_location_data)
        self.search_widget.change_background_color_request.connect(self.change_background_color)
        self.search_bar.addWidget(self.search_widget)
        self.search_bar.setMovable(False)
        self.addToolBar(self.search_bar)

        self.setStyleSheet("background-color: #ffffff;")
        self.setCentralWidget(self.central_widget)
        
    def change_background_color(self, state):
        '''Changes background color of central widget (used for dark/white mode change)'''
        if state:
            # Light mode
            self.central_widget.setStyleSheet("background-color: #ffffff;")
            self.search_bar.setStyleSheet("background-color: #ffffff;")
            self.result_widget.table.setStyleSheet('''
                    QTableWidget {
                        background-color: #ffffff;
                        border: 2px solid #3A3238;
                    }
                    
                    QHeaderView::section {
                        background-color: #ffffff;
                        border: 2px solid #3A3238;
                    }    
                ''')
        else:
            # Dark mode
            self.central_widget.setStyleSheet("background-color: #1e1e1e;")
            self.search_bar.setStyleSheet("background-color: #1e1e1e;")
            self.result_widget.table.setStyleSheet('''
                    QTableWidget {
                        background-color: #1e1e1e;
                        border: 2px solid #3A3238;
                    }
                    
                    QHeaderView::section {
                        background-color: #1e1e1e;
                        border: 2px solid #3A3238;
                    }    
                ''')




