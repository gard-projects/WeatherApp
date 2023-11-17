from PyQt5.QtWidgets import QLineEdit, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal

class SearchLineEdit(QLineEdit):
    # Signal handling search icon being clicked
    iconClicked = pyqtSignal()

    def __init__(self):
        '''Create a custom QLineEdit which supports a clicked signal'''
        super().__init__()
        self.search_create_icon()

    def search_create_icon(self):
        '''Creates search icon and connects a signal to it'''
        self.searchAction = QAction(QIcon("images/app_icons/search_icon.png"), '')
        self.searchAction.triggered.connect(self.iconClicked.emit)
        self.addAction(self.searchAction, QLineEdit.TrailingPosition)