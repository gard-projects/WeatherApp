from PyQt5.QtWidgets import QApplication
from widgets.gui.AppWindow import AppWindow
from engine import db_setup, db_add_location

# Function for executing application
def main():
    app = QApplication([])
    main_window = AppWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    db_setup()
    db_add_location()
    main()
