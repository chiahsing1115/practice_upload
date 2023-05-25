from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_dialog
import sys

def clicked_press_me():
    x = ui.lineEdit.text()
    value = x.isnumeric()
    if value:
        print("true")
    else:
        print("false")
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText(x)
    message.exec_()

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def clicked_caltulate():
    text1 = ui.num_1.text()
    text2 = ui.num_2.text()
    if is_float(text1) and is_float(text2):
      var1 = float(text1)
      var2 = float(text2)
      ui.label.setText(str(var1+var2))
    else:
        message = QMessageBox()
        message.setWindowTitle("error")
        message.setInformativeText("請輸入數字")
        message.exec_()
def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你按了圖片")
    message.exec_()
    event.x()
    event.y()
    event.button()

def click_radio():
    print("click radio")




app = QApplication(sys.argv)
widge = QWidget()
t = QTranslator()
t.load("chinese.qm")
app.installTranslator(t)



ui = Ui_dialog()
ui.setupUi(widge)

group1 = QButtonGroup(widge)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
ui.radioButton.clicked.connect(click_radio)


def clicked_hello():
    ui.label.setText("hello")
    print(ui.checkBox.isChecked())
    print(ui.comboBox.currentText())
    print(ui.comboBox.currentIndex())
    #ui.progressBar.setValue(40)

def change(i):
    print(i)
    #ui.progressBar.setValue(90)
def slider_change():
    x = ui.horizontalScrollBar.value()
    print("change value is " + str(x))
def slider_release():
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("選擇的數值是 "+ str(ui.horizontalScrollBar.value()))
    message.exec_()
#ui.progressBar.setMaximum(100)
#ui.progressBar.setMinimum(0)
#ui.progressBar.setValue(3)
ui.horizontalScrollBar.setMaximum(110)
ui.horizontalScrollBar.setMinimum(-3)
ui.horizontalScrollBar.valueChanged.connect(slider_change)
ui.horizontalScrollBar.sliderReleased.connect(slider_release)

#ui.pressMeButton.clicked.connect(clicked_press_me)
ui.helloButton.clicked.connect(clicked_hello)
#ui.calculateButton.clicked.connect(clicked_caltulate)
ui.bird.mouseReleaseEvent = pic_click
ui.comboBox.addItems(["cat","dog","bird"])
ui.comboBox.activated.connect(change)

widge.show()
sys.exit(app.exec_())