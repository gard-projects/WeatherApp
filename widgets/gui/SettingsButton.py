from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

# Class for settings button
class SettingsButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("images/app_icons/settings_icon.png"))
        self.setFixedSize(40, 40)