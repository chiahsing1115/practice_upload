from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from mainwindow import Ui_dialog
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.ui.helloButton.clicked.connect(self.clicked_hello)
    def clicked_hello(self):
        print("hello")

if __name__=="__main__":
    app =QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    sys.exit(app.exec_())

