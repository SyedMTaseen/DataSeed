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
curr_db_user = ds_db["curr_user"]
cu = curr_db_user.find_one({})
# list(curr_user)
# print(curr_user['username'])
# print(curr_user['password'])


def loginpressed():
    curr_user = ds_user.find_one({"username": login.TUname.text(), "password": login.Tpass.text()})
    print(login.TUname.text())
    print(curr_user)
    print(login.Tpass.text())

    if (list(curr_user) == []):
        login.Lerror.setText("The username/password is incorrect. Please try again.")
        pass
    else:
        x = curr_db_user.insert({"_id": curr_user['_id']}) # Saving the unique logged in ID
        # y = curr_db_user.remove({}) # Deleting the unique logged in ID at sign out
        # SAAD DB DONE
        login.hide()
        os.system('python mainpage.py')
        pass

       
def signuppressed():
    
    login.hide()
    signup.show()
def forgetpressed():
    forgetwindow.show()

def verifyinfo():
    
#     curr_user_ques = ds_user.find_one({"_id":curr_user_id},{"security_question":1, "_id":0})["security_question"]

#     curr_user_ans = ds_user.find_one({"_id":curr_user_id},{"security_answer":1, "_id":0})["security_answer"]
    if (forgetwindow.Tques.text()==forgetwindow.Tans.text()):
        # SAAD DB COMMENTED
        sendmail(forgetwindow.Temail.text(),1)
        
        #time.sleep(5)
        #forgetwindow.hide()
def setquestion():
    if not forgetwindow.Temail.text:
        forgetwindow.Lerror.setText("Enter email address")
        ###SAAD DB
    # check kro forgetwindow.Temail.text koi valid email return krna rha h??
    ##yes then forgetwindow.Tques.setText(question) else: forgetwindow.Lerror.setText("No email address found")
    ##question->db se ae ga  


def sendmail(emailid,flag):
    if (flag==1):
        
        fromaddr="pashaafrozsyed@gmail.com"
        toaddr = emailid
        
        # SAAD DB COMMENTED
        curr_user = ds_user.find_one({"email":emailid}, {"password":1, "_id":0})
        forgot_password = curr_user['password']
        
        msgg = "Your Password is:"+forget_password+" if you havn't request for password reset kindly ignore this mail"
        
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
            z=ds_user.insert_one({"username":signup.TUname.text(), "password":signup.Tpass.text(), "phone" : "+923312042409", "email": signup.Temail.text(), "full_name" : "Soman Maqai", "address" : "House 1234 Model Colony Karachi Pakistan", "category": signup.Toccu.text(), "organization":signup.Torg.text(), "security_question":signup.Tques.text(), "security_answer":signup.Tans.text()})
            # SAAD DB DONE

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
    forgetwindow.askButton.clicked.connect(setquestion)
    login.Tpass.returnPressed.connect(login.loginButton.click)
    login.show()
    app.exec()
