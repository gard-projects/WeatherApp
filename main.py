from PyQt5.QtWidgets import QApplication
from widgets.gui.AppWindow import AppWindow
from query import db_setup, weather_request

# Function for executing application
def main():
    db_setup()
    app = QApplication([])
    main_window = AppWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()
