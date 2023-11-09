from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Function for executing application
def main():

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Weather App")
    window.setWindowIcon(QIcon("weather_logo.png"))
    window.show()

    app.exec()

# Main file for handling software interactions
if __name__ == "__main__":
    main()
