from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from widgets.location.Location import Location
from .SearchLine import SearchLineEdit
from widgets.gui.SettingsButton import SettingsButton
from widgets.gui.AboutWindow import AboutWindow
from PyQt5.QtCore import pyqtSignal
from query import weather_request


# Widget for searching for a location
class SearchWidget(QWidget):
    location_request = pyqtSignal(Location)
    change_background_color_request = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.counter = 0

        # Handles search functionality
        search_label = QLabel("Find location: ")
        self.search_input = SearchLineEdit()
        self.search_input.setPlaceholderText("........")
        self.search_input.setClearButtonEnabled(True)
        self.search_input.editingFinished.connect(self.search)
        self.search_input.iconClicked.connect(self.search)

        # Actions
        self.close_app_action = QAction(QIcon("images/app_icons/close_icon.png"), "Exit")
        self.close_app_action.triggered.connect(self.close_app)
        self.about_action = QAction(QIcon("images/app_icons/about_icon.png"), "About")
        self.about_action.triggered.connect(self.about_window)
        self.change_mode_icon = QIcon("images/app_icons/dark_mode.png")
        self.change_mode_state = True
        self.change_mode_action = QAction(self.change_mode_icon, "Dark mode")
        self.change_mode_action.triggered.connect(self.change_mode)


        # Handles settings functionality
        self.settings_button = SettingsButton()
        self.settings_menu = QMenu()
        self.settings_menu.addAction(self.change_mode_action)
        self.settings_menu.addAction(self.about_action)
        self.settings_menu.addAction(self.close_app_action)
        
        # Show menu when settings button is clicked
        self.settings_button.clicked.connect(self.show_menu)

        self.layout.addWidget(search_label)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.settings_button)

        self.setLayout(self.layout)

        # About window (set to hidden by default)
        self.about_window = AboutWindow()
        self.about_window.hide()
        
    def search(self):
        '''Provides search functionality for widget'''
        if self.search_input.text() == "":
            return

        # Emit signal to update location in main window
        searched_location = weather_request(self.search_input.text())
        if searched_location is None:
            self.location_request.emit(Location("", None, None, 0, 0, 0, 0))
            self.search_input.setText("Location not found")
            return
        
        self.location_request.emit(searched_location)
        self.search_input.setText("")

    def show_menu(self):
        '''Displays menu'''
        button_pos = self.settings_button.mapToGlobal(self.settings_button.rect().bottomLeft())
        self.settings_menu.exec(button_pos)

    def close_app(self):
        '''Closes application'''
        QCoreApplication.quit()

    def about_window(self):
        '''Opens window covering the about section'''
        self.about_window.show()

    def change_mode(self):
        '''Changes mode (light/dark)'''
        if self.change_mode_state:
            new_icon = QIcon("images/app_icons/light_mode.png")
            self.change_mode_action.setText("Light mode")
            self.change_mode_state = False
            self.change_background_color_request.emit(False)
        else:
            new_icon = QIcon("images/app_icons/dark_mode.png")
            self.change_mode_action.setText("Dark mode")
            self.change_mode_state = True
            self.change_background_color_request.emit(True)
        
        self.change_mode_action.setIcon(new_icon)