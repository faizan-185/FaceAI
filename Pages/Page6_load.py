from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images


class Start_Page6(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_6.ui", self)
        self.pg6_btn1 = self.findChild(QPushButton, "pushButton_2")
        self.pg6_btn2 = self.findChild(QPushButton, "pushButton_3")
        self.pg6_btn3 = self.findChild(QPushButton, "pushButton")