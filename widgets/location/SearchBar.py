from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon


# Widget for searching for a location
class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        search_label = QLabel("Find location: ")
        search_input = QLineEdit()
        search_input.setPlaceholderText("...")

        settings_button = QPushButton("Settings (WIP)")

        self.layout.addWidget(search_label)
        self.layout.addWidget(search_input)
        self.layout.addWidget(settings_button)

        self.setLayout(self.layout)
    