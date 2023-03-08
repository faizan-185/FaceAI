from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images


class Start_Page5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("/Users/abbas-ali/Desktop/This Mac/D Drive/Practise Projects/PycharmProjects/FaceAI/FaceAI/UI_Designs/Page_5.ui", self)
        self.pg5_btn1 = self.findChild(QPushButton, "pushButton_5")
        self.pg5_btn2 = self.findChild(QPushButton, "pushButton_6")
        self.pg5_btn3 = self.findChild(QPushButton, "pushButton")
        # self.pg7_btnhome = self.findChild(QPushButton, "pushButton_12")
