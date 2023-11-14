from PyQt5.QtWidgets import QApplication
from widgets.gui.AppWindow import AppWindow

# Function for executing application
def main():
    app = QApplication([])
    main_window = AppWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()
