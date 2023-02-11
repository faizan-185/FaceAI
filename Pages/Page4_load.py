from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images


class Start_Page4(QMainWindow):
    def __init__(self):
        super().__init__()
        print("3")
        self.window = uic.loadUi("UI_Designs/Page_4.ui", self)
