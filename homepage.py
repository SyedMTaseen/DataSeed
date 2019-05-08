
# coding: utf-8

# In[1]:


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy, QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, QHBoxLayout
import pymongo
import datetime
#from __future__ import absolute_import, division, print_function
import datetime
import pandas as pd
import numpy as np
import dfgui


# In[2]:


item_list = list()


data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
ds_user = ds_db["user"]
ds_datasets = ds_db["dataset"]
# curr_datasets = ds_datasets.find_many()

for x in ds_datasets.find():
    print(type(x))
    item_list.append(x)

curr_user = ds_user.find_one()


# In[3]:


qtCreatorFile_pur = "purchase_window.ui"  # Enter file here.

Ui_MainWindow_pur, QtBaseClass = uic.loadUiType(qtCreatorFile_pur)


class PurchaseWindow(QtWidgets.QMainWindow, Ui_MainWindow_pur):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
#         self.purchase_btn.clicked.connect(self.CalculateTax)
#         self.sell_btn.clicked.connect(self.CalculateTax2)


qtCreatorFile_pay = "Payment.ui"  # Enter file here.

Ui_MainWindow_pay, QtBaseClass = uic.loadUiType(qtCreatorFile_pay)


class PaymentWindow(QtWidgets.QMainWindow, Ui_MainWindow_pay):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

# In[ ]:


qtCreatorFile = "homepage.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


filterItem = ['All item', 'Medical', 'Movies', 'General']
path = 0

# dummy_dataset = [{
#     "uploaded_by": 123,
#     "full_description": "This dataset refers to data of genes and etc.",
#     "category":"Medical",
#     "short_description":"This data is nice med.",
#     "data_location": r"C:\Users\SAAD PC\Documents\DSci Project\diabetes.csv",
#     "data_size":"5 GB",
#     "status":"For Sale",
#     "cost":30500,
#     "uploaded_on_date_time":datetime.datetime.now()}]


original_list_item = item_list.copy()

pay_obj = 0


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.clickme.clicked.connect(self.searchItem)
        self.searchBox.setText('')
#         self.ItemListView.addItems(ItemList)
        self.filterBox.addItems(filterItem)
        self.filterBox.currentIndexChanged.connect(self.selectionchange)
#         self.label.setText('DataSeed-Homepage')
#         self.ItemListView.setStyleSheet( "QListWidget::item {margin-bottom:10px}")
        self.renderList()
        self.ItemListView.itemDoubleClicked.connect(self.itemclicked)
        self.purchase_window = uic.loadUi("purchase_window.ui")
        self.searchBox.returnPressed.connect(self.clickme.click)
        self.payment_window = uic.loadUi("payment.ui")

    def itemclicked(self, iteem):
        print("item clicked: ", iteem)

        i = 0
        while i < len(item_list):
            if(self.ItemListView.item(i) == iteem):
                break
            i = i+1

        self.PurchaseWindowOpen(i)
#         mainpg.hide()
#         pg1.show()
#         pg1.requestButton.hide()
#         pg1.Ltitle.setText("Saad DB se "+str(i)+"th entry ka show kara do")

    def PurchaseWindowOpen(self, item_index):
        global path
        print(item_list[item_index])
        global pay_obj
        pay_obj = item_list[item_index]
        self.purchase_window.show()
        self.purchase_window.descr.setText(
            item_list[item_index]['full_description'])
        self.purchase_window.cost.setText(item_list[item_index]['cost'])
        self.purchase_window.size.setText(item_list[item_index]['data_size'])
        self.purchase_window.status.setText(item_list[item_index]['status'])
        self.purchase_window.categ.setText(item_list[item_index]['category'])
        self.purchase_window.upload.setText(
            str(item_list[item_index]['uploaded_by']))
        self.purchase_window.rating.setText(
            str(item_list[item_index]['rating']))
        self.purchase_window.title.setText(
            item_list[item_index]['short_description'])
        self.purchase_window.viewdatabtn.clicked.connect(
            self.viewdata)
        self.purchase_window.paybtn.clicked.connect(
            self.paypage)
        path = item_list[item_index]["data_location"]

    def paypage(self):
        global pay_obj
        self.purchase_window.hide()
        self.payment_window.show()
        self.payment_window.cost.setText(pay_obj['cost'])
        comm = int(pay_obj['cost'])*5
        comm = comm/100
        self.payment_window.comm.setText(str(comm))
        self.payment_window.total.setText(str(comm + int(pay_obj['cost'])))

        self.payment_window.proceedbtn.clicked.connect(
            self.proceed)

    def proceed(self):
        global pay_obj
        cardnum = self.payment_window.cardnum.text()
        exp = self.payment_window.exp.text()
        print(exp)
        print(cardnum)

    def viewdata(self):
        global path
        print(path)
        df = pd.read_csv(path)
        dfgui.show(df.head(10))

    def Search_Query(self, query):
        search_list = []
        search_query = query
        global item_list
        for x in item_list:
            temp = list(x.values())
            for y in temp:
                #                 print(y)
                try:
                    if search_query in y:
                        search_list.append(x)
#                         print('breaking after \n',x)
                        break
                except:
                    pass

        search_list
        item_list = []
        item_list = search_list.copy()
        self.SearchresultLabel.setText(
            str(len(search_list)) + " result(s) found")

    def searchItem(self):
        global original_list_item
        global item_list
        item_list = original_list_item.copy()
        print('check')
        query = self.searchBox.text()
        self.Search_Query(query)
        self.renderList()

    def renderList(self):
        self.ItemListView.clear()
        for i in range(0, len(item_list)):
            self.renderListItem(i)

    def renderListItem(self, i):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)

        item = QListWidgetItem(self.ItemListView)
        label = QLabel(str(i+1) + ") " + item_list[i]['short_description'] + "\n" + "Uploaded By: " + str(
            item_list[i]['uploaded_by']) + "\n" + "Rating: " + str(item_list[i]['rating']) + "/5")
        label.setStyleSheet(
            "height:fit-content;font-size:12pt;font-style: normal;font-weight:100;")
      #  label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        label.setWordWrap(True)

        label2 = QLabel(
            "Data Size: " + item_list[i]['data_size'] + '\nStatus: ' + item_list[i]['status'])
        label2.setStyleSheet(
            "height:fit-content;font-size:12pt;text-align:right;")
#             label2.setStyleSheet("color: white; background: red;,text-align:right;");
        label2.setAlignment(QtCore.Qt.AlignCenter)
#             label2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
      #  label2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        label2.setWordWrap(True)

        layout.addWidget(label)
        layout.addWidget(label2)

        widget = QWidget()
        widget.setStyleSheet("height:fit-content;,width:100%")
        widget.setLayout(layout)

        item.setSizeHint(layout.sizeHint())

        self.ItemListView.addItem(item)
        self.ItemListView.setItemWidget(item, widget)


#         strr=''
#         for i in range(0,3):
#             for item in dummy_dataset:
#                 for key,value in item.items():
#                     strr += key + ' ' + str(value) + '\n'

    def selectionchange(self, i):
        global original_list_item
        global item_list
        strr = self.filterBox.currentText()
#         print(strr)
        item_list = original_list_item.copy()
        if strr != "All item":
            self.Search_Query(strr)

        self.renderList()


if __name__ == "__main__":
    x = 12
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
