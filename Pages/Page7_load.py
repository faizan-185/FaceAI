from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images


class Start_Page7(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("/Users/abbas-ali/Desktop/This Mac/D Drive/Practise Projects/PycharmProjects/FaceAI/FaceAI/UI_Designs/Page_7.ui", self)
        self.pg7_btnhome = self.findChild(QPushButton, "pushButton")
