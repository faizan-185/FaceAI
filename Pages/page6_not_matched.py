from PyQt5 import uic
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images



class Start_Page6_NotMatched(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_6_Not_Matched.ui", self)

        self.probe_id = self.findChild(QLineEdit, "probe_idLineEdit")
        self.probe_result = self.findChild(QLineEdit, "probe_idLineEdit_2")
        self.time = self.findChild(QLineEdit, "probe_idLineEdit_3")
        self.case_number = self.findChild(QLineEdit, "probe_idLineEdit_4")
        self.examiner_no = self.findChild(QLineEdit, "probe_idLineEdit_6")
        self.examiner_name = self.findChild(QLineEdit, "probe_idLineEdit_5")
        self.remarks = self.findChild(QLineEdit, "probe_idLineEdit_7")
        self.case_image = self.findChild(QLabel, "label_8")

        self.pg6_n_btn1 = self.findChild(QPushButton, "pushButton_3")
        self.pg6_n_btn2 = self.findChild(QPushButton, "pushButton_2")
        self.pg6_n_btn3 = self.findChild(QPushButton, "pushButton")
        # self.pg7_btnhome = self.findChild(QPushButton, "pushButton_12")
