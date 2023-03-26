from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ItemWidget2(QWidget):
    def __init__(self, image_path, text, parent=None):
        super().__init__(parent)

        # Create the QLabel for the image
        pixmap = QPixmap(image_path)
        pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
        label_image = QLabel(self)
        label_image.setPixmap(pixmap)
        label_image.setScaledContents(True)

        match = ""

        if 70 <= text < 80:
            match = "Low match"
        elif 80 <= text < 90:
            match = "High match"
        elif 90 <= text < 100:
            match = "Highest match"

        label_text = QLabel(f"Similarity Score: {text} % ({match} Match)", self)
        label_text.setStyleSheet("color: white;")

        # Create the vertical layout and add the image and text labels
        layout = QVBoxLayout(self)
        layout.addWidget(label_image)
        layout.addWidget(label_text)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setMaximumSize(350, 350)

    def remove_self(self):
        layout = self.parent().layout()
        index = layout.indexOf(self)
        print(index)
        row, col, rowspan, colspan = layout.getItemPosition(index)
        print(row, col)
        item = layout.takeAt(index)
        for i in range(index, layout.count()):
            item = layout.itemAt(i)
            row, col, rowspan, colspan = layout.getItemPosition(i)

            layout.addWidget(item.widget(), row, col)
        self.deleteLater()
