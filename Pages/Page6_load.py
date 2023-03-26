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

        self.probe_id = self.findChild(QLabel, "label_11")
        self.probe_result = self.findChild(QLabel, "label_12")
        self.time = self.findChild(QLabel, "label_13")
        self.case_number = self.findChild(QLabel, "label_14")
        self.examiner_no = self.findChild(QLabel, "label_15")
        self.examiner_name = self.findChild(QLabel, "label_16")
        self.remarks = self.findChild(QLabel, "label_17")
        self.case_image = self.findChild(QLabel, "label_8")

        self.layout = self.findChild(QWidget, "scrollAreaWidgetContents_2")

        self.pg6_btn1 = self.findChild(QPushButton, "pushButton_3")
        self.pg6_btn2 = self.findChild(QPushButton, "pushButton_6")
        self.pg6_btn3 = self.findChild(QPushButton, "pushButton")
