from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.Qt import Qt
from widgets.location.Location import Location

# Widget for displaying weather results (from query)
class WeatherResult(QWidget):
    def __init__(self):
        super().__init__()

        self.current_location = None
      
        self.setFont(QFont("Times"))
        self.table = QTableWidget(1,4)
        self.title_location = QLabel()
        self.title_date = QLabel()
        self.table.setHorizontalHeaderLabels(["Wind speed", "Temperature", "Icon", "Precipitation amount"])
        self.table.verticalHeader().setVisible(False)
        self.table.setFixedSize(850, 100)

        # Table styling
        self.table.setShowGrid(False)
        font_table_header = QFont()
        font_table_header.setBold(True)
        self.table.horizontalHeader().setFont(font_table_header)
        self.table.horizontalHeader().setStretchLastSection(True)

        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title_location)
        self.layout.addWidget(self.title_date)
        self.layout.addWidget(self.table)
        self.layout.addStretch()
        self.setLayout(self.layout)

    def update_location(self, location: Location):
        '''Updates displayed location data'''
        if location.location_name == "":
            self.current_location = None
            return
        self.current_location = location
        self.update_table()

    def update_table(self):
        # Create the table content
        if self.current_location is not None:
            self.title_location.setText(self.current_location.location_name)
            self.title_date.setText(self.current_location.last_modified.strftime("%d.%m.%Y %H:%M:%S"))
            icon_path = "images/met/" + self.current_location.weather_symbol + ".png"
            weather_icon = QIcon(icon_path)
            
            location_data = [
                f"{self.current_location.wind_speed:.1f}",
                f"{self.current_location.air_temperature:.1f}",
                weather_icon,
                f"{self.current_location.percipitation_amount:.1f}"
            ]

            # Update the table
            row = 0
            for col, value in enumerate(location_data):
                if col == 2:
                    item = QTableWidgetItem()
                    item.setIcon(value)
                else:
                    item = QTableWidgetItem(str(value))

                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)
                self.table.setColumnWidth(col, 200)

           