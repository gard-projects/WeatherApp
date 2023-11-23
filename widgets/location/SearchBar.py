from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QMenu, QAction, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from .SearchLine import SearchLineEdit
from widgets.gui.SettingsButton import SettingsButton
from widgets.gui.AboutWindow import AboutWindow


# Widget for searching for a location
class SearchWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
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


        # Handles settings functionality
        self.settings_button = SettingsButton()
        self.settings_menu = QMenu()
        # self.settings_menu.addAction(close_app)
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
        # Check if search input is empty
        if self.search_input.text() == "":
            return

        self.search_input.setText("")
        print("Test")

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

        