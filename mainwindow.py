# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 310)
        dialog.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.bird = QtWidgets.QLabel(dialog)
        self.bird.setGeometry(QtCore.QRect(0, 20, 171, 111))
        self.bird.setStyleSheet("font: 12pt \"Agency FB\";")
        self.bird.setText("")
        self.bird.setPixmap(QtGui.QPixmap("bird.jpg"))
        self.bird.setScaledContents(True)
        self.bird.setAlignment(QtCore.Qt.AlignCenter)
        self.bird.setObjectName("bird")
        self.helloButton = QtWidgets.QPushButton(dialog)
        self.helloButton.setGeometry(QtCore.QRect(70, 160, 102, 42))
        self.helloButton.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"font: 11pt \"華康秀風體W3(P)\";\n"
"font: 11pt \"Agency FB\";")
        self.helloButton.setObjectName("helloButton")
        self.pressmeButton_2 = QtWidgets.QPushButton(dialog)
        self.pressmeButton_2.setGeometry(QtCore.QRect(250, 160, 102, 42))
        self.pressmeButton_2.setStyleSheet("background-color: rgb(130, 135, 139);\n"
"font: 11pt \"華康秀風體W3(P)\";\n"
"font: 11pt \"Agency FB\";")
        self.pressmeButton_2.setObjectName("pressmeButton_2")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(72, 131, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(170, 80, 150, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(dialog)
        self.radioButton.setGeometry(QtCore.QRect(70, 220, 81, 16))
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 240, 71, 31))
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 212, 81, 21))
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(180, 240, 81, 31))
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.num_1 = QtWidgets.QLineEdit(dialog)
        self.num_1.setGeometry(QtCore.QRect(260, 10, 113, 20))
        self.num_1.setObjectName("num_1")
        self.num_2 = QtWidgets.QLineEdit(dialog)
        self.num_2.setGeometry(QtCore.QRect(260, 50, 113, 20))
        self.num_2.setObjectName("num_2")
        self.checkBox = QtWidgets.QCheckBox(dialog)
        self.checkBox.setGeometry(QtCore.QRect(223, 119, 131, 31))
        self.checkBox.setStyleSheet("font: 11pt \"Agency FB\";")
        self.checkBox.setAutoRepeatInterval(100)
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 20, 53, 22))
        self.comboBox.setObjectName("comboBox")
        self.horizontalScrollBar = QtWidgets.QScrollBar(dialog)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(30, 280, 160, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "你好"))
        self.helloButton.setText(_translate("dialog", "show string"))
        self.pressmeButton_2.setText(_translate("dialog", "press me"))
        self.label.setText(_translate("dialog", "please enter value"))
        self.radioButton.setText(_translate("dialog", "+"))
        self.radioButton_2.setText(_translate("dialog", "-"))
        self.radioButton_3.setText(_translate("dialog", "*"))
        self.radioButton_4.setText(_translate("dialog", "/"))
        self.pushButton.setText(_translate("dialog", "PushButton"))
        self.checkBox.setText(_translate("dialog", "CheckBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
