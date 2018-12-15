# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from law import returning

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1905, 998)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(820, 10, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(190, 120, 1191, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1570, 130, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.after_click)  # 연결 !
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 240, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 440, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1320, 240, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(23, 300, 901, 131))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("QLabel { background-color: white;  border:1px solid black; }")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(23, 500, 901, 470))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("QLabel { background-color: white;  border:1px solid black; }")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(940, 300, 931, 670))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("QLabel { background-color: white;  border:1px solid black; }")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1905, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "상황 입력하기"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.label_2.setText(_translate("MainWindow", "유사한 질문"))
        self.label_3.setText(_translate("MainWindow", "유사한 답변"))
        self.label_4.setText(_translate("MainWindow", "관련 법 조항"))
        self.label_5.setText(_translate("MainWindow", " "))
        self.label_6.setText(_translate("MainWindow", " "))
        self.label_7.setText(_translate("MainWindow", " "))

    def after_click(self):
        text = self.textEdit.text()
        result = returning(text) # q, a ,law 순으로 반환
        self.label_5.setText(result[0]) #
        self.label_6.setText(result[1]) # q
        self.label_7.setText(result[2]) # s,


if __name__ == "__main__":
    import sys
    # print(returning("안녕하세요"))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

