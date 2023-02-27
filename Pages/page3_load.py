from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Start_Page3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("UI_Designs/Page_3.ui", self)
        self.pg3_btn1 = self.findChild(QPushButton, "pushButton")
        self.pg3_btn2 = self.findChild(QPushButton, "pushButton_2")
        self.pg3_btn3 = self.findChild(QCommandLinkButton, "commandLinkButton")

        self.radio1 = self.findChild(QRadioButton, "radioButton")
        self.radio2 = self.findChild(QRadioButton, "radioButton_2")
        self.radio3 = self.findChild(QRadioButton, "radioButton_3")
        self.radio4 = self.findChild(QRadioButton, "radioButton_4")
