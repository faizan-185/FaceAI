import os
from PyQt5 import uic
from PyQt5 import QtWidgets
import sys
import images
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Page2_load import Start_Page2
from page3_load import Start_Page3
from Page7_load import Start_Page7
from Page4_load import Start_Page4
from Page5_load import Start_Page5
from Page6_load import Start_Page6


class Start_Page(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_6.ui", self)
        self.showMaximized()


app = QtWidgets.QApplication(sys.argv)
window = Start_Page()
app.exec_()
