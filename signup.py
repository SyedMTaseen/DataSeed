# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(400, 300)
        self.Lpic = QtWidgets.QLabel(SignUp)
        self.Lpic.setGeometry(QtCore.QRect(300, 10, 91, 71))
        self.Lpic.setText("")
        self.Lpic.setPixmap(QtGui.QPixmap("img/signup1.png"))
        self.Lpic.setScaledContents(True)
        self.Lpic.setObjectName("Lpic")
        self.RegisterButton = QtWidgets.QPushButton(SignUp)
        self.RegisterButton.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.RegisterButton.setObjectName("RegisterButton")
        self.SignUp_2 = QtWidgets.QGroupBox(SignUp)
        self.SignUp_2.setGeometry(QtCore.QRect(10, 40, 271, 231))
        self.SignUp_2.setObjectName("SignUp_2")
        self.Temail = QtWidgets.QLineEdit(self.SignUp_2)
        self.Temail.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.Temail.setObjectName("Temail")
        self.LUname = QtWidgets.QLabel(self.SignUp_2)
        self.LUname.setGeometry(QtCore.QRect(17, 61, 61, 20))
        self.LUname.setObjectName("LUname")
        self.LEmail = QtWidgets.QLabel(self.SignUp_2)
        self.LEmail.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.LEmail.setObjectName("LEmail")
        self.Tpass = QtWidgets.QLineEdit(self.SignUp_2)
        self.Tpass.setGeometry(QtCore.QRect(90, 120, 171, 20))
        self.Tpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Tpass.setObjectName("Tpass")
        self.LPassword = QtWidgets.QLabel(self.SignUp_2)
        self.LPassword.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.LPassword.setObjectName("LPassword")
        self.Lphone = QtWidgets.QLabel(self.SignUp_2)
        self.Lphone.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.Lphone.setObjectName("Lphone")
        self.Tphoneno = QtWidgets.QLineEdit(self.SignUp_2)
        self.Tphoneno.setGeometry(QtCore.QRect(90, 150, 171, 20))
        self.Tphoneno.setObjectName("Tphoneno")
        self.TUname = QtWidgets.QLineEdit(self.SignUp_2)
        self.TUname.setGeometry(QtCore.QRect(90, 60, 171, 20))
        self.TUname.setObjectName("TUname")
        self.Lerror = QtWidgets.QLabel(self.SignUp_2)
        self.Lerror.setGeometry(QtCore.QRect(60, 200, 171, 16))
        self.Lerror.setAlignment(QtCore.Qt.AlignCenter)
        self.Lerror.setStyleSheet("QLabel {color:red;}")
        self.Lerror.setObjectName("Lerror")

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)
        ###my func
        self.RegisterButton.clicked.connect(self.registerpressed)
        ##exit 

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Sign Up"))
        self.RegisterButton.setText(_translate("SignUp", "Register"))
        self.SignUp_2.setTitle(_translate("SignUp", "SignUp"))
        self.LUname.setText(_translate("SignUp", "User Name"))
        self.LEmail.setText(_translate("SignUp", "Email"))
        self.LPassword.setText(_translate("SignUp", "Password"))
        self.Lphone.setText(_translate("SignUp", "Phone No."))
        self.Lerror.setText(_translate("SignUp", " "))
        ### my func 
    def registerpressed(self):

        if(self.TUname.text()==""):
            self.Lerror.setText("UserName is required!")
        elif(self.Tpass.text()==""):
            self.Lerror.setText("Password is required!")
        elif(self.Temail.text()==""):
            self.Lerror.setText("Email is required!")
        else:
            self.Lerror.setText("Register Successfull")
        ### exit        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())

