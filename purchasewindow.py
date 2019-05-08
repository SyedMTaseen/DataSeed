# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchase_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy, QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, QHBoxLayout
import pymongo
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(60, 20, 691, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.title.setFont(font)
        self.title.setText("")
        self.title.setObjectName("title")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 430, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 390, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 260, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.descr = QtWidgets.QLabel(self.centralwidget)
        self.descr.setGeometry(QtCore.QRect(70, 80, 681, 171))
        self.descr.setText("")
        self.descr.setObjectName("descr")
        self.cost = QtWidgets.QLabel(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(210, 270, 321, 16))
        self.cost.setObjectName("cost")
        self.categ = QtWidgets.QLabel(self.centralwidget)
        self.categ.setGeometry(QtCore.QRect(210, 310, 321, 16))
        self.categ.setObjectName("categ")
        self.size = QtWidgets.QLabel(self.centralwidget)
        self.size.setGeometry(QtCore.QRect(210, 350, 271, 16))
        self.size.setObjectName("size")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(210, 390, 351, 16))
        self.status.setObjectName("status")
        self.upload = QtWidgets.QLabel(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(210, 440, 351, 16))
        self.upload.setObjectName("upload")
        self.viewdata = QtWidgets.QPushButton(self.centralwidget)
        self.viewdata.setGeometry(QtCore.QRect(200, 500, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewdata.setFont(font)
        self.viewdata.setObjectName("viewdata")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 500, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label_2.setText(_translate("MainWindow", "Uploaded by:"))
        self.label_3.setText(_translate("MainWindow", "Category:"))
        self.label_4.setText(_translate("MainWindow", "Data Size:"))
        self.label_5.setText(_translate("MainWindow", "Status:"))
        self.label_6.setText(_translate("MainWindow", "Cost:"))
        self.cost.setText(_translate("MainWindow", "TextLabel"))
        self.categ.setText(_translate("MainWindow", "TextLabel"))
        self.size.setText(_translate("MainWindow", "TextLabel"))
        self.status.setText(_translate("MainWindow", "TextLabel"))
        self.upload.setText(_translate("MainWindow", "TextLabel"))
        self.viewdata.setText(_translate("MainWindow", "View Sample Data"))
        self.pushButton_2.setText(_translate(
            "MainWindow", "Proceed to Payment"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
