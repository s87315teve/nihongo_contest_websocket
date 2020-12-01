# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\eric\nihongo_contest.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1085, 754)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_start = QtWidgets.QPushButton(Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(790, 560, 131, 51))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(790, 640, 131, 51))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.textBrowser_question = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_question.setGeometry(QtCore.QRect(170, 180, 181, 61))
        self.textBrowser_question.setObjectName("textBrowser_question")
        self.lineEdit_input = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_input.setGeometry(QtCore.QRect(170, 300, 181, 51))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.lcdNumber_point = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_point.setGeometry(QtCore.QRect(730, 110, 231, 131))
        self.lcdNumber_point.setObjectName("lcdNumber_point")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 190, 51, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 320, 58, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton_input = QtWidgets.QPushButton(Dialog)
        self.pushButton_input.setGeometry(QtCore.QRect(370, 310, 111, 41))
        self.pushButton_input.setObjectName("pushButton_input")
        self.textBrowser_answer = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_answer.setGeometry(QtCore.QRect(470, 180, 181, 61))
        self.textBrowser_answer.setObjectName("textBrowser_answer")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(410, 200, 58, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(820, 80, 58, 15))
        self.label_4.setObjectName("label_4")
        self.lcdNumber_mistake = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_mistake.setGeometry(QtCore.QRect(730, 310, 231, 61))
        self.lcdNumber_mistake.setObjectName("lcdNumber_mistake")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(820, 290, 58, 15))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.pushButton_cancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_start.setText(_translate("Dialog", "スタート"))
        self.pushButton_cancel.setText(_translate("Dialog", "キャンセル"))
        self.label.setText(_translate("Dialog", "問題"))
        self.label_2.setText(_translate("Dialog", "入力"))
        self.pushButton_input.setText(_translate("Dialog", "入力"))
        self.label_3.setText(_translate("Dialog", "答え"))
        self.label_4.setText(_translate("Dialog", "正解"))
        self.label_5.setText(_translate("Dialog", "間違い"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

