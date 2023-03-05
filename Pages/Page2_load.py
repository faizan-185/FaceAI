from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import images


def show_critical_messagebox(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("Fields Required!")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()


class Start_Page2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("UI_Designs/Page_2.ui", self)
        self.case_number = self.findChild(QLineEdit, "probe_idLineEdit_3")
        self.ps = self.findChild(QLineEdit, "probe_idLineEdit_4")
        self.examiner_name = self.findChild(QLineEdit, "probe_idLineEdit_5")
        self.examiner_number = self.findChild(QLineEdit, "probe_idLineEdit_6")
        self.remarks = self.findChild(QLineEdit, "probe_idLineEdit_7")
        self.image = None

        self.pg2_btn3 = self.findChild(QPushButton, "home")
        self.pg2_btn2 = self.findChild(QPushButton, "cont")
        self.select_target = self.findChild(QLabel, "label")
        self.select_target.setPixmap(QPixmap("/home/anonymous/Documents/FaceAI_GUI_PyQT/images/select.png"))
        self.select_target.setStyleSheet("border-radius: 20px")
        self.upload = self.findChild(QPushButton, "pushButton")
        self.upload.setStyleSheet("background-image : url(/home/anonymous/Documents/FaceAI_GUI_PyQT/images/upload.png); border: none; background-color: rgb(0, 90, 226); border-radius: 15px; width:40px; height: 50px")
        self.upload.clicked.connect(self.getfiles)


        # validators
        self.case_number.textChanged.connect(self.validate_case_number)
        self.ps.textChanged.connect(self.validate_ps)
        self.examiner_name.textChanged.connect(self.validate_examiner_name)
        self.examiner_number.textChanged.connect(self.validate_examiner_contact)
        self.remarks.textChanged.connect(self.validate_remarks)
        self.select_target.setPixmap(QPixmap("/home/anonymous/Documents/FaceAI_GUI_PyQT/images/select.png"))

    def clear(self):
        self.image = None
        self.ps.setText("")
        self.case_number.setText("")
        self.examiner_name.setText("")
        self.examiner_number.setText("")
        self.remarks.setText("")
        pixmap = QPixmap("/home/anonymous/Documents/FaceAI_GUI_PyQT/images/select.png")
        pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
        self.select_target.setPixmap(pixmap)

    def validate_case_number(self):
        if not self.case_number.text().isascii():
            show_critical_messagebox("Character must belongs to the basic Latin characters.")

    def validate_ps(self):
        if not self.ps.text().isascii():
            show_critical_messagebox("Character must belongs to the basic Latin characters.")

    def validate_examiner_name(self):
        if not self.examiner_name.text().isascii():
            show_critical_messagebox("Character must belongs to the basic Latin characters.")

    def validate_examiner_contact(self):
        if not self.examiner_number.text().isascii():
            show_critical_messagebox("Character must belongs to the basic Latin characters.")

    def validate_remarks(self):
        if not self.remarks.text().isascii():
            show_critical_messagebox("Character must belongs to the basic Latin characters.")

    def validate_all(self):
        if self.case_number.text() == "":
            show_critical_messagebox("Please enter case number.")
        elif self.ps.text() == "":
            show_critical_messagebox("Please enter PS.")
        elif self.examiner_name.text() == "":
            show_critical_messagebox("Please enter examiner's name.")
        elif self.examiner_number.text() == "":
            show_critical_messagebox("Please enter examiner's number.")
        elif self.remarks.text() == "":
            show_critical_messagebox("Please enter remarks.")
        elif not self.case_number.text().isascii():
            show_critical_messagebox("Characters of case number must belongs to the basic Latin characters.")
        elif not self.ps.text().isascii():
            show_critical_messagebox("Characters of PS must belongs to the basic Latin characters.")
        elif not self.examiner_name.text().isascii():
            show_critical_messagebox("Characters of examiner's name must belongs to the basic Latin characters.")
        elif not self.examiner_number.text().isascii():
            show_critical_messagebox("Characters of examiner's number must belongs to the basic Latin characters.")
        elif not self.remarks.text().isascii():
            show_critical_messagebox("Characters of remarks must belongs to the basic Latin characters.")
        elif self.image is None:
            show_critical_messagebox("please select a target image.")
        else:
            return True

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setNameFilters(['Image files (*.png *.jpg *.jpeg)'])
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            self.image = filenames[0]
            pixmap = QPixmap(filenames[0])
            pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
            self.select_target.setPixmap(pixmap)
