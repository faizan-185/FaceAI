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
from page5_not_matched import Start_Page5_NotMatched
from page6_not_matched import Start_Page6_NotMatched
from probe_image import ItemWidget
from probe_image2 import ItemWidget2
from random import randint
import datetime

BASE_PATH = os.path.abspath(os.getcwd())
# from src.similarity import runner


def show_critical_messagebox(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("Fields Required!")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    retval = msg.exec_()


class Start_Page(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("UI_Designs/Page_1.ui", self)
        self.btn1 = self.findChild(QtWidgets.QPushButton, "CreateCase")
        self.pg1_btn2 = self.findChild(QtWidgets.QPushButton, "ProbeText")

        self.ui_2 = Start_Page2()
        self.ui_3 = Start_Page3()
        # self.ui_3.showMaximized()
        self.ui_4 = Start_Page4()
        self.ui_5 = Start_Page5()
        self.ui_5_n = Start_Page5_NotMatched()
        self.ui_6 = Start_Page6()
        self.ui_6_n = Start_Page6_NotMatched()
        self.ui_7 = Start_Page7()
        self.data = [('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/3.jpg', 18.73), ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 99.94),
                     ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94),('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94),
                     ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94), ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94),
                     ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 80.94),('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94),
                     ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94), ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94),
                     ('/home/anonymous/Documents/FaceAI_GUI_PyQT/models/2.jpg', 88.94)]
        self.drop_count = 0
        self.refined_data = []

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
        self.ui_2.clear()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_3.hide()
        # self.ui_2 = Start_Page2()
        # Click to go page1 from page 2 button
        self.ui_2.pg2_btn3.clicked.connect(self.show_Page1)
        # Click to go page 3 from page 2 button
        self.ui_2.pg2_btn2.clicked.connect(self.show_Page3)
        self.ui_2.showMaximized()

    def show_Page3(self):
        res = self.ui_2.validate_all()
        if res:
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
        if self.ui_3.validate():
            self.ui_3.hide()
            self.MainWindow = QtWidgets.QMainWindow()
            # self.ui_4.showMaximized()
            # runner()
            matched = False
            for i in self.data:
                if i[1] >= 70:
                    matched = True
                    break
            if matched:
                self.ui_5.probe_id.setText(''.join(["{}".format(randint(0, 9)) for num in range(0, 9)]))
                self.ui_5.probe_result.setText("Matched")
                now = datetime.datetime.now()
                formatted_date = now.strftime("%d/%m/%Y %I:%M %p")
                self.ui_5.time.setText(formatted_date)
                self.ui_5.case_number.setText(self.ui_2.case_number.text())
                self.ui_5.examiner_no.setText(self.ui_2.examiner_number.text())
                self.ui_5.examiner_name.setText(self.ui_2.examiner_name.text())
                self.ui_5.remarks.setText(self.ui_2.remarks.text())
                pixmap = QPixmap(self.ui_2.image)
                pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
                self.ui_5.case_image.setPixmap(pixmap)
                self.ui_5.case_image.setStyleSheet("border-radius: 20px")

                layout = QGridLayout()
                num_cols = 3
                for i, item in enumerate(self.data):
                    row = i // num_cols
                    col = i % num_cols
                    probe_data = ItemWidget(image_path=item[0], text=item[1])
                    probe_data.button.clicked.connect(
                        lambda state, r=row, c=col: self.remove_item(layout, r, c))
                    layout.addWidget(probe_data, row, col)


                self.ui_5.layout.setLayout(layout)
                self.show_Page5()
            else:
                self.show_Page5_N()

    def remove_item(self, grid, row, col):
        item = grid.itemAtPosition(row, col)
        if item is not None and self.drop_count < len(self.data)-1:
            item = item.widget()
            grid.removeWidget(item)
            item.deleteLater()
            self.data[3 * row + col] = None
            self.drop_count += 1
        else:
            show_critical_messagebox("Cannot delete last image!")
        print(self.data)

    def show_Page5_N(self):
        self.ui_3.hide()
        self.ui_6.hide()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_5_n.probe_id.setText(''.join(["{}".format(randint(0, 9)) for num in range(0, 9)]))
        self.ui_5_n.probe_result.setText("Matched")
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %I:%M %p")
        self.ui_5_n.time.setText(formatted_date)
        self.ui_5_n.case_number.setText(self.ui_2.case_number.text())
        self.ui_5_n.examiner_no.setText(self.ui_2.examiner_number.text())
        self.ui_5_n.examiner_name.setText(self.ui_2.examiner_name.text())
        self.ui_5_n.remarks.setText(self.ui_2.remarks.text())
        pixmap = QPixmap(self.ui_2.image)
        pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
        self.ui_5_n.case_image.setPixmap(pixmap)
        self.ui_5_n.case_image.setStyleSheet("border-radius: 20px")
        # Click to go page 6 from page 5
        self.ui_5_n.pg5_n_btn3.clicked.connect(self.show_Page3)
        # Click to go page 1 from page 5
        self.ui_5_n.pg5_n_btn2.clicked.connect(self.show_Page1)
        # Click to go page 3 from page 5
        self.ui_5_n.pg5_n_btn1.clicked.connect(self.show_Page6_Not_Matched)
        self.ui_5_n.showMaximized()

    def show_Page5(self):
        # self.ui_4.hide()
        self.ui_3.hide()

        self.ui_6.close()
        self.MainWindow = QtWidgets.QMainWindow()

        # Click to go page 6 from page 5
        self.ui_5.pg5_btn1.clicked.connect(self.show_Page6)
        # Click to go page 1 from page 5
        self.ui_5.pg5_btn2.clicked.connect(self.show_Page1)
        # Click to go page 3 from page 5
        self.ui_5.pg5_btn3.clicked.connect(self.show_Page3)
        self.ui_5.showMaximized()

    def show_Page6_Not_Matched(self):
        self.ui_5_n.hide()

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_6_n.probe_id.setText(self.ui_5_n.probe_id.text())
        self.ui_6_n.probe_result.setText("Matched")
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %I:%M %p")
        self.ui_6_n.time.setText(formatted_date)
        self.ui_6_n.case_number.setText(self.ui_2.case_number.text())
        self.ui_6_n.examiner_no.setText(self.ui_2.examiner_number.text())
        self.ui_6_n.examiner_name.setText(self.ui_2.examiner_name.text())
        self.ui_6_n.remarks.setText(self.ui_2.remarks.text())
        pixmap = QPixmap(self.ui_2.image)
        pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
        self.ui_6_n.case_image.setPixmap(pixmap)
        self.ui_6_n.case_image.setStyleSheet("border-radius: 20px")
        self.ui_6_n.pg6_n_btn3.clicked.connect(self.show_Page5)
        # Click to go page 1 from page 6
        self.ui_6_n.pg6_n_btn2.clicked.connect(self.show_Page1)
        self.ui_6_n.showMaximized()

    def show_Page6(self):
        self.ui_5.hide()

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui_6.probe_id.setText(self.ui_5.probe_id.text())
        self.ui_6.probe_result.setText("Matched")
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %I:%M %p")
        self.ui_6.time.setText(formatted_date)
        self.ui_6.case_number.setText(self.ui_2.case_number.text())
        self.ui_6.examiner_no.setText(self.ui_2.examiner_number.text())
        self.ui_6.examiner_name.setText(self.ui_2.examiner_name.text())
        self.ui_6.remarks.setText(self.ui_2.remarks.text())
        pixmap = QPixmap(self.ui_2.image)
        pixmap = pixmap.scaled(350, 350, aspectRatioMode=Qt.KeepAspectRatio)
        self.ui_6.case_image.setPixmap(pixmap)
        self.ui_6.case_image.setStyleSheet("border-radius: 20px")

        layout = QGridLayout()
        num_cols = 3
        for i in self.data:
            if i is not None:
                print(i)
                self.refined_data.append(i)
        self.refined_data = sorted(self.refined_data, key=lambda x: (-x[1], x[0]))

        for i, item in enumerate(self.refined_data):
            row = i // num_cols
            col = i % num_cols
            probe_data = ItemWidget2(image_path=item[0], text=item[1])

            layout.addWidget(probe_data, row, col)

        self.ui_6.layout.setLayout(layout)
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


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = Start_Page()
    app.exec_()
