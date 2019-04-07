
# coding: utf-8

# In[1]:


import sys
from PyQt5 import QtCore, QtGui, QtWidgets,uic,Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy,QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem,     QHBoxLayout


# In[2]:


qtCreatorFile = "homepage.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


# In[3]:


ItemList = ['Movie Data','Stock Data','Phone Data']
filterItem = ['Date','Name']
import datetime

dummy_dataset = [{
    "uploaded_by": 123, 
    "full_description": "This dataset refers to data of genes and etc.",
    "category":"Medical",
    "short_description":"This data is nice med.",
    "data_location": r"C:\Users\SAAD PC\Documents\DSci Project\diabetes.csv",
    "data_size":"5 GB", 
    "status":"For Sale",
    "cost":30500, 
    "uploaded_on_date_time":datetime.datetime.now()}]


strr=''
for item in dummy_dataset:
    for key,value in item.items():
        strr += key + ' ' + str(value) + '\n'

print(strr)
#ItemList.append(strr)
dummy_dataset[0]['cost']


# In[4]:



class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.clickme.clicked.connect(self.CalculateTax)
        self.searchBox.setText('serch me')
#         self.ItemListView.addItems(ItemList)
        self.filterBox.addItems(filterItem)
        self.filterBox.currentIndexChanged.connect(self.selectionchange)
#         self.label.setText('DataSeed-Homepage')
#         self.ItemListView.setStyleSheet( "QListWidget::item {margin-bottom:10px}")
        self.renderList()

        
    def CalculateTax(self):
        print('check')
        
    def renderList(self):
        for i in range(0,10):
            self.renderListItem(i)
        

    def renderListItem(self,i):
            layout = QHBoxLayout()
            layout.setSizeConstraint(QLayout.SetMinimumSize);
            
            item = QListWidgetItem(self.ItemListView)
            label = QLabel(str(i+1)+ ") " + dummy_dataset[0]['short_description'] + "\n" + "Uploaded By: " + str(dummy_dataset[0]['uploaded_by']))
            label.setStyleSheet("height:fit-content;font-size:12pt;font-style: normal;font-weight:100;");
          #  label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            label.setWordWrap(True);
            
            label2 = QLabel("Data Size: " + dummy_dataset[0]['data_size'] + '\nStatus: ' + dummy_dataset[0]['status'])
            label2.setStyleSheet("height:fit-content;font-size:12pt;text-align:right;");
#             label2.setStyleSheet("color: white; background: red;,text-align:right;");
            label2.setAlignment(QtCore.Qt.AlignCenter)
#             label2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
          #  label2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

            label2.setWordWrap(True)

            

            layout.addWidget(label)
            layout.addWidget(label2)
            
            widget = QWidget()
            widget.setStyleSheet("height:fit-content;,width:'100%'");
            widget.setLayout(layout);
            
            item.setSizeHint(layout.sizeHint())
            
            self.ItemListView.addItem(item)
            self.ItemListView.setItemWidget(item,widget)
        
        
#         strr=''
#         for i in range(0,3):
#             for item in dummy_dataset:
#                 for key,value in item.items():
#                     strr += key + ' ' + str(value) + '\n'
    
        
    def selectionchange(self,i):
        self.searchBox.setText(self.filterBox.currentText())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

