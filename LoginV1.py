from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import smtplib,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import pymongo

app = QtWidgets.QApplication([])

signup=uic.loadUi("signup.ui")
login=uic.loadUi("login.ui")
forgetwindow=uic.loadUi("forgetwindow.ui")

data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
ds_user = ds_db["user"]

# x = ds_user.insert_one({_id:123,"fullname":"DataSeed User","username":"ds", "password":"ds"})
curr_user = ds_user.find_one()
list(curr_user)
# print(curr_user['username'])
# print(curr_user['password'])



def loginpressed():
    if(login.TUname.text()== curr_user["username"] and login.Tpass.text() == curr_user["password"]):
        #login.Lerror.setText("Redirect page is not added")
        # SAAD DB
        login.hide()
        os.system('python mainpage.py')
    else:
        login.Lerror.setText("Invalid Username or password")

       
def signuppressed():
    
    login.hide()
    signup.show()
def forgetpressed():
    forgetwindow.show()

def verifyinfo():
    if (forgetwindow.Tques.text()==forgetwindow.Tans.text()):
        # SAAD DB
        sendmail(forgetwindow.Temail.text(),1)
        
        time.sleep(5)
        forgetwindow.hide()

def sendmail(emailid,flag):
    if (flag==1):
        
        fromaddr="pashaafrozsyed@gmail.com"
        toaddr = emailid
        msgg = "Your Password is: if you havn't request for password reset kindly ignore this mail"
        # SAAD DB
        subj = "Password Reset Mail"

        message = MIMEMultipart()
        message['From'] = fromaddr
        message['To'] = toaddr
        message['Subject'] = subj

        message.attach(MIMEText(msgg, 'plain'))
        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(fromaddr,"Fast1234")
            text = message.as_string()
            ret = server.sendmail(fromaddr, toaddr, text)
            forgetwindow.Lerror.setText("Email regarding password is sent")

        except Exception as e:
                print('some error occured')
                #print(e)
                forgetwindow.Lerror.setText("Some problem occured!")
    
    
    elif(flag==2):
        fromaddr="pashaafrozsyed@gmail.com"
        toaddr = emailid
        msgg = "Your account has been created using this email id. the purpose of this email to notify"
        subj = "Notification Regarding Account Creation"

        message = MIMEMultipart()
        message['From'] = fromaddr
        message['To'] = toaddr
        message['Subject'] = subj

        message.attach(MIMEText(msgg, 'plain'))
        try:
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(fromaddr,"Fast1234")
            text = message.as_string()
            ret = server.sendmail(fromaddr, toaddr, text)
            signup.Lerror.setText("Register Successfull")

        except Exception as e:
            print('some error occured')
            #print(e)
            signup.Lerror.setText("Enable to sendmail")


def registerpressed():

        if(signup.TUname.text()==""):
            signup.Lerror.setText("UserName is required!")
        elif(signup.Tpass.text()==""):
            signup.Lerror.setText("Password is required!")
        elif(signup.Temail.text()==""):
            signup.Lerror.setText("Email is required!")
        elif(signup.Toccu.text()==""):
            signup.Lerror.setText("Enter occupation")
        elif(signup.Torg.text()==""):
            signup.Lerror.setText("Enter organization")
        elif(signup.Tques.text()==""):
            signup.Lerror.setText("Security Question is required")
        elif(signup.Tans.text()==""):
            signup.Lerror.setText("Answer is required")    
        else:
            # SAAD DB
            sendmail(signup.Temail.text(),2)
            signup.Lerror.setText("Register Successfull")

def ini():
    login.LPic.setPixmap(QtGui.QPixmap("img/login.png"))
    login.LPic.setScaledContents(True)
    login.Lerror.setStyleSheet("QLabel {color:red;}")
    signup.Lpic.setPixmap(QtGui.QPixmap("img/signup1.png"))
    signup.Lpic.setScaledContents(True)
    signup.Lerror.setStyleSheet("QLabel {color:red;}")
    forgetwindow.Lerror.setStyleSheet("QLabel {color:red;}")

if __name__ == "__main__":

    ini()
    login.loginButton.clicked.connect(loginpressed)
    login.Signup.clicked.connect(signuppressed)
    login.forgetButton.clicked.connect(forgetpressed)
    signup.RegisterButton.clicked.connect(registerpressed)
    forgetwindow.verifyButton.clicked.connect(verifyinfo)
    login.Tpass.returnPressed.connect(login.loginButton.click)
    login.show()
    app.exec()
