# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:29:52 2019

@author: Taseen Syed
"""
   

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication([])

dlg = uic.loadUi("profile.ui")



def main():
    dlg.UsernameTxt.setText("Username Dummy")
    
    
def OpenEditInfo():
   print("edit")
    
    
def BackToMain():   
    print("Main")

if __name__=="__main__":
    main()
dlg.EditInfoBtn.clicked.connect(OpenEditInfo)
dlg.BackBtn.clicked.connect(BackToMain)

dlg.show()
app.exec()

