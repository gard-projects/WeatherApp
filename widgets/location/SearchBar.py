from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QLabel
from .SearchLine import SearchLineEdit


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

        settings_button = QPushButton("Settings (WIP)")

        self.layout.addWidget(search_label)
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(settings_button)

        self.setLayout(self.layout)
        
    def search(self):
        # Check if search input is empty
        if self.search_input.text() == "":
            return

        self.search_input.setText("")
        print("Test")