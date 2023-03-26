from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images
from random import randint


class Start_Page5(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_5.ui", self)

        self.probe_id = self.findChild(QLabel, "label_51")
        self.probe_result = self.findChild(QLabel, "label_52")
        self.time = self.findChild(QLabel, "label_54")
        self.case_number = self.findChild(QLabel, "label_55")
        self.examiner_no = self.findChild(QLabel, "label_56")
        self.examiner_name = self.findChild(QLabel, "label_57")
        self.remarks = self.findChild(QLabel, "label_53")
        self.case_image = self.findChild(QLabel, "label_8")

        self.layout = self.findChild(QWidget, "scrollAreaWidgetContents_2")


        self.pg5_btn1 = self.findChild(QPushButton, "pushButton_5")
        self.pg5_btn2 = self.findChild(QPushButton, "pushButton_6")
        self.pg5_btn3 = self.findChild(QPushButton, "pushButton")
        # self.pg7_btnhome = self.findChild(QPushButton, "pushButton_12")
