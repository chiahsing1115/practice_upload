from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_dialog
import sys


app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_dialog()
ui.setupUi(widge)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
    def bird_click(self.event):
        self.message = QMessageBox()
        self.message.setWindowTitle("surprise")
        self.message.setInformativeText("你按了圖片")
        self.message.exec_()
        print(self.event.x())
        print(self.event.y())
        print(self.event.button())
    
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def press(self):
        x = ui.num_1.text()
        y = ui.num_2.text()
        """if not isfloat(x) or not isfloat(y):
            message = QMessageBox()
            message.setWindowTitle("error")
            message.setInformativeText("請輸入數字")
            message.exec_()
            return
        if ui.radioButton.isChecked():
            ans = float(x)+float(y) 
        """
        if self.isfloat(x) and self.isfloat(y):
            if ui.radioButton.isChecked():
                ans = float(x)+float(y)
            elif ui.radioButton_2.isChecked():
                ans = float(x)-float(y)
            elif ui.radioButton_3.isChecked():
                ans = float(x)*float(y)
            elif ui.radioButton_4.isChecked():
                ans = float(x)/float(y)
            ui.label.setText(str(ans))
        else:
            message = QMessageBox()
            message.setWindowTitle("error")
            message.setInformativeText("請輸入數字")
            message.exec_()

        self.ui.bird.mouseReleaseEvent = bird_click(self.event)
        group1 = QButtonGroup(widge)
        group1.addButton(self.ui.radioButton)
        group1.addButton(self.ui.radioButton_2)
        group1.addButton(self.ui.radioButton_3)
        group1.addButton(self.ui.radioButton_4)
        ui.radioButton.clicked.connect(self.press)
        ui.radioButton_2.clicked.connect(self.press)
        ui.radioButton_3.clicked.connect(self.press)
        ui.radioButton_4.clicked.connect(self.press)
        ui.pushButton.clicked.connect(self.press)

if __name__=="__main__":
    app =QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    sys.exit(app.exec_())