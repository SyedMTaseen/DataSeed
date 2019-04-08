
# coding: utf-8

# In[1]:


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets,uic,Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy,QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem,     QHBoxLayout


# In[2]:


qtCreatorFile = "main page.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


# In[ ]:


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.purchase_btn.clicked.connect(self.CalculateTax)
        self.sell_btn.clicked.connect(self.CalculateTax2)
     

        
    def CalculateTax(self):
        
        os.system('python homepage.py')
    def CalculateTax2(self):
        
        os.system('python selldata.py')
        
  
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

