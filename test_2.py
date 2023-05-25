from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from calculate import Ui_Dialog
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def clicked_Add():
    text1 = ui.number_1.text()
    text2 = ui.number_2.text()
    if isfloat(text1) and isfloat(text2):
        x=float(ui.number_1.text())
        y=float(ui.number_2.text())
        ui.label.setText(str(x+y))
    else:
        message = QMessageBox()
        message.setWindowTitle("error")
        message.setInformativeText("請輸入數字")
        message.exec_()
    #message = QMessageBox()
    #message.setWindowTitle("Anwser")
    #message.setInformativeText(str(x+y))
    #message.exec_()

app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)
ui.AddButton.clicked.connect(clicked_Add)
widge.show()
app.exec_()
