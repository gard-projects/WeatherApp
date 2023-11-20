from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt

# Widget for displaying weather results (from query)
class WeatherResult(QWidget):
    def __init__(self):
        super().__init__()


        # Fetch data
        input = {"wind_speed": "4.0", 
                 "temp": "12.0", 
                 "icon": "something", 
                 "precipitation_amount": "4.0"}

        # Fields used in table
     
        self.location = "London"
        self.current_date = "20.11.2023"
        self.wind_speed = 4.0
        self.temp = 12.0
        self.icon = "something"
        self.precipitation_amount = 4.0
        self.title_location = QLabel(f"Location: {self.location}")
        self.title_date = QLabel(f"Date: {self.current_date}")

        table = QTableWidget(1,4)
        table.setHorizontalHeaderLabels(["Wind speed", "Temperature", "Icon", "Precipitation amount"])
        table.verticalHeader().setVisible(False)
        table.setFixedSize(850, 100)

        # Insert into table
        for row in range(1):
            for col, entry in enumerate(input):
                item = QTableWidgetItem(input[entry])
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, col, item)
                table.setColumnWidth(col, 200)

        table.setShowGrid(False)
        font_table_header = QFont()
        font_table_header.setBold(True)
        table.horizontalHeader().setFont(font_table_header)
       
        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title_location)
        self.layout.addWidget(self.title_date)
        self.layout.addWidget(table)
        self.layout.addStretch()
        self.setLayout(self.layout)