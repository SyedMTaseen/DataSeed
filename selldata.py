
# coding: utf-8

# In[1]:


import sys
from PyQt5 import QtCore, QtGui, QtWidgets,uic,Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy,QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem,     QHBoxLayout


# In[2]:


qtCreatorFile = "sell data.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


# In[3]:


filterItem = ['Medical','General']
strr=''


# In[4]:


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.submit_btn.clicked.connect(self.CalculateTax)
        self.category_field.addItems(filterItem)
        self.category_field.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self,i):
        strr+= self.category_field.currentText();
        self.status_field.setText(self.category_field.currentText())
        
    def CalculateTax(self):
        
        str1= self.b_des_field.toPlainText()
        str2= self.l_des_field.toPlainText()
        str3= self.path_field.text()
        str4= self.cost_field.text()
        if (str1 =="" or str2 =="" or str3 =="" or str4 =="" ):
            self.status_field.setText("Detail is missing!")    
        else:
            self.status_field.setText("Successfully Submited!")
        
  
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

