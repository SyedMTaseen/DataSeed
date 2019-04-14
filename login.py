# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


import pymongo

data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
ds_user = ds_db["user"]

# x = ds_user.insert_one({_id:123,"fullname":"DataSeed User","username":"ds", "password":"ds"})
curr_user = ds_user.find_one()
list(curr_user)
# print(curr_user['username'])
# print(curr_user['password'])





class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(Login)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 10, 241, 231))
        self.groupBox.setObjectName("groupBox")
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.Signup = QtWidgets.QPushButton(self.groupBox)
        self.Signup.setGeometry(QtCore.QRect(132, 181, 75, 23))
        self.Signup.setObjectName("Signup")
        self.LUname = QtWidgets.QLabel(self.groupBox)
        self.LUname.setGeometry(QtCore.QRect(27, 41, 52, 16))
        self.LUname.setObjectName("LUname")
        self.TUname = QtWidgets.QLineEdit(self.groupBox)
        self.TUname.setGeometry(QtCore.QRect(85, 41, 133, 20))
        self.TUname.setObjectName("TUname")
        self.Lpass = QtWidgets.QLabel(self.groupBox)
        self.Lpass.setGeometry(QtCore.QRect(28, 92, 52, 16))
        self.Lpass.setObjectName("Lpass")
        self.Tpass = QtWidgets.QLineEdit(self.groupBox)
        self.Tpass.setGeometry(QtCore.QRect(86, 92, 131, 20))
        self.Tpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Tpass.setObjectName("Tpass")
        self.Lerror = QtWidgets.QLabel(self.groupBox)
        self.Lerror.setGeometry(QtCore.QRect(40, 140, 150, 16))
        self.Lerror.setObjectName("Lerror")
        self.Lerror.setStyleSheet("QLabel {color:red;}")
        self.LPic = QtWidgets.QLabel(self.centralWidget)
        self.LPic.setGeometry(QtCore.QRect(20, 50, 121, 151))
        self.LPic.setText("")
        self.LPic.setPixmap(QtGui.QPixmap("img/login.png"))
        self.LPic.setScaledContents(True)
        self.LPic.setObjectName("LPic")
        Login.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Login)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        Login.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Login)
        self.mainToolBar.setObjectName("mainToolBar")
        Login.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Login)
        self.statusBar.setObjectName("statusBar")
        Login.setStatusBar(self.statusBar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        ### func 
        self.loginButton.clicked.connect(self.loginpressed)
        self.Signup.clicked.connect(self.signuppressed)
	###	exit

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.groupBox.setTitle(_translate("Login", "Sign In"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.Signup.setText(_translate("Login", "Sign Up"))
        self.LUname.setText(_translate("Login", "User Name"))
        self.Lpass.setText(_translate("Login", "Password  "))
        self.Lerror.setText(_translate("Login", "<html><head/><body><p><br/></p></body></html>"))
        ##my func	
    def loginpressed(self):
        if(self.TUname.text()== curr_user["username"] and self.Tpass.text() == curr_user["password"]):
            self.Lerror.setText("Redirect page is not added")
            os.system('python mainpage.py')
        else:
        	self.Lerror.setText("Invalid Username or password")

       
             
    def signuppressed(self):
        
        os.system('python signup.py')          
       
         #sys.exit()# not best way

     	##exit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

