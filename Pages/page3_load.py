from PyQt5 import uic
import sys
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


class Start_Page3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("UI_Designs/Page_3.ui", self)
        self.pg3_btn1 = self.findChild(QPushButton, "pushButton")
        self.pg3_btn2 = self.findChild(QPushButton, "pushButton_2")
        self.pg3_btn3 = self.findChild(QCommandLinkButton, "commandLinkButton")

        self.target_img = self.findChild(QLabel, "label_2")
        self.selection = self.findChild(QLabel, "label_3")
        pixmap = QPixmap("/images/select.png")
        pixmap = pixmap.scaled(250, 250, aspectRatioMode=Qt.KeepAspectRatio)
        self.target_img.setPixmap(pixmap)
        self.target_img.setStyleSheet("border-radius: 20px")

        self.upload_image = self.findChild(QPushButton, "pushButton_3")
        self.upload_image.clicked.connect(self.get_files)

        self.radio1 = self.findChild(QRadioButton, "radioButton_2")
        self.radio2 = self.findChild(QRadioButton, "radioButton_4")
        self.radio3 = self.findChild(QRadioButton, "radioButton_3")
        self.radio4 = self.findChild(QRadioButton, "radioButton")
        self.selected_option = None
        self.selected_file = []

    def clear(self):
        self.selected_option = None
        self.selected_file = []
        pixmap = QPixmap("/images/select.png")
        pixmap = pixmap.scaled(250, 250, aspectRatioMode=Qt.KeepAspectRatio)
        self.target_img.setPixmap(pixmap)
        self.target_img.setStyleSheet("border-radius: 20px")

    def get_files(self):
        if self.radio1.isChecked():
            self.file_picker(1)
        elif self.radio2.isChecked():
            self.file_picker(2)
        elif self.radio3.isChecked():
            self.file_picker(3)
        elif self.radio4.isChecked():
            pass

    def file_picker(self, option):
        self.selected_option = option
        dlg = QFileDialog()
        if option == 1:
            dlg.setFileMode(QFileDialog.ExistingFile)
            dlg.setNameFilters(['Image files (*.png *.jpg *.jpeg)'])
            if dlg.exec_():
                self.selected_file = dlg.selectedFiles()
                pixmap = QPixmap(self.selected_file[0])
                pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
                self.target_img.setPixmap(pixmap)
                self.selection.setText("")
        elif option == 2:
            dlg.setFileMode(QFileDialog.ExistingFiles)
            dlg.setNameFilters(['Image files (*.png *.jpg *.jpeg)'])
            if dlg.exec_():
                self.selected_file = dlg.selectedFiles()
                pixmap = QPixmap("/images/selected_images.png")
                pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
                self.target_img.setPixmap(pixmap)
                self.selection.setText(f"Picked {len(self.selected_file)} images.")
        elif option == 3:
            dlg.setFileMode(QFileDialog.DirectoryOnly)
            if dlg.exec_():
                self.selected_file = dlg.selectedFiles()
                print(self.selected_file)
                pixmap = QPixmap("/images/directory.png")
                pixmap = pixmap.scaled(100, 100, aspectRatioMode=Qt.KeepAspectRatio)
                self.target_img.setPixmap(pixmap)
                self.selection.setText(f"Picked folder:  '  {self.selected_file[0].split('/')[-1]}  '")

    def validate(self):
        if len(self.selected_file) == 0 or self.selected_option is None:
            show_critical_messagebox("Please select image")
        else:
            return True
