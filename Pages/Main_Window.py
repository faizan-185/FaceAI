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
BASE_PATH = os.path.abspath(os.getcwd())


class Start_Page(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_1.ui", self)
        self.btn1 = self.findChild(QtWidgets.QPushButton, "CreateCase")
        self.pg1_btn2 = self.findChild(QtWidgets.QPushButton, "ProbeText")

        self.ui_2 = Start_Page2()
        self.ui_3 = Start_Page3()
        self.ui_4 = Start_Page4()
        self.ui_5 = Start_Page5()
        self.ui_6 = Start_Page6()
        self.ui_7 = Start_Page7()

        # Click to go page2 from page 1 button
        self.btn1.clicked.connect(self.show_Page2)
        # Click to go to page 7 from page 1 button
        self.pg1_btn2.clicked.connect(self.show_Page7)

        self.showMaximized()
        # self.show()

    def show_Page1(self):
        self.ui_2.hide()
        self.ui_3.hide()
        self.ui_6.hide()
        self.ui_7.hide()
        self.ui_5.hide()
        self.showMaximized()

    def show_Page2(self):
        self.hide()

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_3.hide()
        # self.ui_2 = Start_Page2()
        # Click to go page1 from page 2 button
        self.ui_2.pg2_btn3.clicked.connect(self.show_Page1)
        # Click to go page 3 from page 2 button
        self.ui_2.pg2_btn2.clicked.connect(self.show_Page3)
        self.ui_2.showMaximized()

    def show_Page3(self):
        self.hide()
        self.ui_2.hide()
        self.ui_5.hide()
        self.MainWindow = QtWidgets.QMainWindow()
        # self.ui_3 = Start_Page3()
        # Click to go page 4 from page 3
        self.ui_3.pg3_btn1.clicked.connect(self.show_Page4)
        # Click to go page 1 from page 3
        self.ui_3.pg3_btn2.clicked.connect(self.show_Page1)
        # Click to go page 2 from page 3
        self.ui_3.pg3_btn3.clicked.connect(self.show_Page2)
        self.ui_3.showMaximized()

    def show_Page4(self):
        self.ui_3.hide()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_4.showMaximized()
        QTimer.singleShot(2000, self.show_Page5)

    def show_Page5(self):
        self.ui_4.hide()
        self.ui_6.hide()
        self.MainWindow = QtWidgets.QMainWindow()
        # Click to go page 6 from page 5
        self.ui_5.pg5_btn1.clicked.connect(self.show_Page6)
        # Click to go page 1 from page 5
        self.ui_5.pg5_btn2.clicked.connect(self.show_Page1)
        # Click to go page 3 from page 5
        self.ui_5.pg5_btn3.clicked.connect(self.show_Page3)
        self.ui_5.showMaximized()

    def show_Page6(self):
        self.ui_5.hide()
        self.MainWindow = QtWidgets.QMainWindow()
        # Click to go page 5 from page 6
        self.ui_6.pg6_btn3.clicked.connect(self.show_Page5)
        # Click to go page 1 from page 6
        self.ui_6.pg6_btn2.clicked.connect(self.show_Page1)
        self.ui_6.showMaximized()



    def show_Page7(self):
        self.hide()
        self.ui_4.hide()
        self.MainWindow = QtWidgets.QMainWindow()
        # Click to go page 1 from page 7
        self.ui_7.pg7_btnhome.clicked.connect(self.show_Page1)
        self.ui_7.showMaximized()







app = QtWidgets.QApplication(sys.argv)
window = Start_Page()
app.exec_()
