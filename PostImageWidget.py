from PyQt5.QtWidgets import QWidget as QtWidget

class PostImageWidget(QtWidget):
    def __init__(self, title, description, image_path):
        super().__init__() # Use the parent class constructor
        self.label = QLabel(title)
        self.label = QLabel(description)
        self.image 