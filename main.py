from PyQt5.QtWidgets import QApplication
from widgets.gui.AppWindow import AppWindow
from query import db_setup, weather_request
import json

# Function for executing application
def main():
    app = QApplication([])
    main_window = AppWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    db_setup()
    #db_add_location()
    #data = weather_request("London")
    #print(json.dumps(data, indent=4))
    main()
