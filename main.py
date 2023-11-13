from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from widgets.gui.WeatherGUI import WeatherGUI 

# Function for executing application
def main():

    app = QApplication([])
    main_window = WeatherGUI()
    main_window.show()
    app.exec()

# Main file for handling software interactions
if __name__ == "__main__":
    main()
