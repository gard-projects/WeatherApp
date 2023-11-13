from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStyle
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize


class WeatherTitle(QWidget):
    ''' This class handles the creation of a custom title bar for the application'''
    def __init__(self, parent):
        super().__init__()
        # Customize layout of title bar
        main_widget = QWidget()
        self.parent = parent
        self.layout = QHBoxLayout(main_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setStretch(1,500)
        self.layout.setSpacing(0)

        # Create widgets (which represents the title bar)
        title = QLabel("WeatherAPI")
        app_logo = self.setIconLabel(QIcon("images/weather_logo.png"))
        close_button = self.setIconButton("SP_TitleBarCloseButton")
        
        # Add widget to layout
        self.layout.addWidget(app_logo)
        self.layout.addWidget(title)
        self.layout.addWidget(close_button)
        self.setLayout(self.layout)

        # Setup signal(s)
        close_button.clicked.connect(self.closeButton)

        # Adjust background color
        main_widget.setStyleSheet("background-color: #403233;")

    def closeButton(self):
        '''Closes application if clicked'''
        self.parent.close()
    
    def setIconLabel(self, icon: QIcon) -> QLabel:
        '''Creates a label with an icon'''
        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(32,32))
        return icon_label
    
    def setIconButton(self, icon_name: str) -> QPushButton:
        '''Creates a button with a standard icon included in Qt5'''
        icon_button = QPushButton()
        icon = self.style().standardIcon(getattr(QStyle, icon_name))
        icon_button.setIcon(icon)
        icon_button.setFixedSize(32,32)
        return icon_button


        
        
