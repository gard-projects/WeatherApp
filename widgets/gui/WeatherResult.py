from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
from query import weather_request
from widgets.location.Location import Location

# Widget for displaying weather results (from query)
class WeatherResult(QWidget):
    def __init__(self):
        super().__init__()

        self.current_location = None
      
        self.setFont(QFont("Times"))
        self.table = QTableWidget(1,4)
        self.table.setHorizontalHeaderLabels(["Wind speed", "Temperature", "Icon", "Precipitation amount"])
        self.table.verticalHeader().setVisible(False)
        self.table.setFixedSize(850, 100)

        # Create the table content
        if self.current_location is not None:
            self.title_location = self.current_location.location_name
            self.title_date = self.current_location.last_modified.strftime("%d.%m.%Y %H:%M:%S")
            location_data = [self.current_location.wind_speed,
                             self.current_location.air_temperature,
                             self.current_location.weather_symbol,
                             self.current_location.precipitation_amount]
            row = 0
            for col, value in enumerate(location_data):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
                self.table.setColumnWidth(col, 200)

        self.table.setShowGrid(False)
        font_table_header = QFont()
        font_table_header.setBold(True)
        self.table.horizontalHeader().setFont(font_table_header)
        self.table.horizontalHeader().setStretchLastSection(True)
       
        # Layout
        self.layout = QVBoxLayout(self)
        if self.current_location is not None:
            self.layout.addWidget(self.title_location)
            self.layout.addWidget(self.title_date)
            self.layout.addWidget(self.table)
            self.layout.addStretch()
        self.setLayout(self.layout)

    def update_location_data(self, location):
        '''Updates displayed location data'''
        if location.location_name == "":
            print("I recieved an update!")
            self.current_location = None
        self.current_location = location
    