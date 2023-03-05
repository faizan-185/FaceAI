from Pages.src.crud import readLisences, isLocked, matchLisence, removeLisence, updateData, insertData
from Pages.src.core.config import conf
from Pages.src.core.db import session, settings_table
import platform, subprocess, re


import os
from PyQt5 import uic
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Pages.Page2_load import Start_Page2
from Pages.page3_load import Start_Page3
from Pages.Page7_load import Start_Page7
from Pages.Page4_load import Start_Page4
from Pages.Page5_load import Start_Page5
from Pages.Page6_load import Start_Page6

BASE_PATH = os.path.abspath(os.getcwd())

class WorkerThread(QThread):
    progress_update = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        # Perform some long-running task
        for i in range(100):
            # Emit a signal to update the progress bar
            self.progress_update.emit(i)
            self.msleep(100)

class MainWindow(QMainWindow):
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
        self.ui_6 = Start_Page6()
        self.ui_7 = Start_Page7()

        # Click to go page2 from page 1 button
        self.btn1.clicked.connect(self.show_Page2)
        # Click to go to page 7 from page 1 button
        self.pg1_btn2.clicked.connect(self.show_Page7)

        # Create a worker thread
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_update.connect(self.showMaximized())
        self.worker_thread.start()



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
            self.ui_4.showMaximized()
            runner()
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


def getProcessor_batch_serial_info(cmd):

    if platform.system() == "Windows":
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        if completed.stdout != "":
            info = completed.stdout
            info = info.strip()
            info = info.decode('utf-8')
            infoObj = dict(item.split(":") for item in re.sub('\s+', '', re.sub('\n', ';', info)).split(";"))
            return infoObj


def main():
    app = QApplication(sys.argv)

    # Create the main window and show it
    window = MainWindow()
    window.show()

    # Run the event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    # print(getProcessor_batch_serial_info("p"))


    if not isLocked(session=session, table=settings_table):
        main()
    else:
        license_key = input("Enter License Key: ")
        licenses = readLisences(conf.LISENCES_PATH)
        result = matchLisence(lisences=licenses, my_lisence=license_key)
        if result:
            removeLisence(path=conf.LISENCES_PATH, lisences=licenses, my_lisence="abcd")
            updateData(session=session, table=settings_table, key="Locked", value="No")
            insertData(session=session, table=settings_table, data=("validity time", "one year"))

        else:
            print("Incorrect License Key")
