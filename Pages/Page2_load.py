from PyQt5 import uic
import sys
# from PyQt5 import QtWidgets
# from Page1 import Ui_MainWindow
# from page1_load import Start_Page
# import images
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Start_Page2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_2.ui", self)
        self.pg2_btn3 = self.findChild(QPushButton, "home")
        self.pg2_btn2 = self.findChild(QPushButton, "cont")