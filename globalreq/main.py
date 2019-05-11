
from PyQt5 import QtWidgets, uic,QtCore, QtGui,Qt
from PyQt5.QtWidgets import *
import ctypes
app = QtWidgets.QApplication([])
import pymongo
import datetime

data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
ds_user = ds_db["user"]
curr_ds_user = ds_db["curr_user"]
requested_data = ds_db["requested_data"]
deleted_request = ds_db["deleted_request"]
cu = curr_ds_user.find_one({})["_id"]

 pg1 = uic.loadUi("./globalreq/QAA.ui")
 popup = uic.loadUi("./globalreq/addrequest.ui")
 mainpg = uic.loadUi("./globalreq/Requestpg.ui")
# pg1 = uic.loadUi("QAA.ui")
# popup = uic.loadUi("addrequest.ui")
# mainpg = uic.loadUi("Requestpg.ui")

def addcoment():
    
    pg1.comentButton.hide()
    pg1.saveButton.show()
    pg1.textEdit = QtWidgets.QTextEdit(pg1.centralwidget)
    pg1.textEdit.setGeometry(QtCore.QRect(10, 390, 721, 71))
    
    pg1.textEdit.setMinimumHeight(31)
    pg1.textEdit.setMaximumHeight(31)
    
    pg1.label_3 = QtWidgets.QLabel(pg1.centralwidget)
    pg1.label_3.setMinimumHeight(24)
    pg1.label_3.setMaximumHeight(28)
    
    # For current user: abc will be: cu
    pg1.label_3.setText( "Comment By:"+"abc")
    #pg1.layout.addWidget(pg1.label_3)
    
    #pg1.layout.addWidget(pg1.textEdit)
    mylayout = pg1.scroll.layout()
    mylayout.addWidget(pg1.label_3)
    mylayout.addWidget(pg1.textEdit)


def addrequest():

    popup.show()

def savereq():
    if not popup.Ttitle.toPlainText():
        popup.Lerror.setStyleSheet("QLabel {color:red;}")
        popup.Lerror.setText("Title for request is required!")
    elif not popup.desbox.toPlainText():
        popup.Lerror.setStyleSheet("QLabel {color:red;}")
        popup.Lerror.setText("Enter atleast 10 words")
    else:
        # Saving request in DB
        # requested_data.insert({"title": popup.Ttitle.toPlainText(), "description": popup.desbox.toPlainText(), "requested_by": cu, "requested_on": datetime.datetime.now(), "status":"Pending", "comments":[]}) 
        pg1.Ltitle.setText(popup.Ttitle.toPlainText())
        pg1.desbox.setText(popup.desbox.toPlainText())
        popup.hide()
def savecmnt():
    if not pg1.textEdit.toPlainText():
        pg1.Lerror.setStyleSheet("QLabel {color:red;}")
        pg1.Lerror.setText("Enter something!!")
    else:
        pg1.Lerror.setText("")
        pg1.comentButton.show()
        pg1.saveButton.hide()
        ##SAAD DB PENDING
        pg1.textEdit.setReadOnly(True)
        
        # y = requested_data.update({}) with cu and comment text
        # jo user logged in, jo requested_data hai, us pe comment add hoga ussi user ke naam se

def renderlist():
    for i in range(len(mydic_list)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(mainpg.listWidget)
        # SAAD DB REPLY: KINDLY CHECK itemclicked()
        label = QLabel(str(i+1)+ ") Title:" + mydic_list[i]['title'] + "\n" + "     Requested By: " + mydic_list[i]['requested_by'])
        label.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;font-style: normal;font-weight:100")
        label.setWordWrap(True);
        
        
        label2 = QLabel("No of comments " + len(mydic_list[i]["comments"]) + '\nStatus: ' + mydic_list[i]['status'])
        label2.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;text-align:right")
        label2.setAlignment(QtCore.Qt.AlignCenter)
        label2.setWordWrap(True)

        

        layout.addWidget(label)
        layout.addWidget(label2)
        
        widget = QWidget()
        widget.setStyleSheet("height:fit-content;width:100%");
        widget.setLayout(layout);
        
        item.setSizeHint(layout.sizeHint())
        
        mainpg.listWidget.addItem(item)
        mainpg.listWidget.setItemWidget(item,widget)
 
def initialization():
    pg1.saveButton.hide()
    pg1.layout.setAlignment(QtCore.Qt.AlignTop)
    pg1.scrollArea.setWidgetResizable(True)

    pg1.scrollArea.setWidget(pg1.scroll)
    pg1.scroll.setLayout(pg1.layout)
    pg1.saveButton.hide()

def itemclicked(iteem):
    i=0;
    while i<5:
        if(mainpg.listWidget.item(i)== iteem):
            break
        i=i+1
    mainpg.hide()
    pg1.show()
    pg1.requestButton.hide()

    # Current Request directly from database
    # request = requested_data.find_one({"_id": mydic_list[i]["_id"]})
    
    # Current Request from provided mydic_list
    request = mydic_list[i]
    
    # Comments of Current Request directly from database
    # comments_of_request = requested_data.find_one({"_id":mydic_list[i]["_id"]}, {"_id":0, "comments":1})["comments"]
    
    # Comments of Current Request from mydic_list
    comments_of_request = mydic_list[i]["comments"]
    
    # STATUS: True or false = "Fulfilled" or "Pending"
    # Accessing status of the current request:
    # request["status"]


    pg1.Ltitle.setText(request['title'])
    pg1.desbox.setText(request['description'])
    
    for k in comments_of_request::
        pg1.textEdit = QtWidgets.QTextEdit(pg1.centralwidget)
        pg1.textEdit.setGeometry(QtCore.QRect(10, 390, 721, 71))

        pg1.textEdit.setMinimumHeight(31)
        pg1.textEdit.setMaximumHeight(31)

        pg1.label_3 = QtWidgets.QLabel(pg1.centralwidget)
        pg1.label_3.setMinimumHeight(24)
        pg1.label_3.setMaximumHeight(28)
        
        # Comment: k["comment"]

        pg1.label_3.setText("Commented by:" ds_user.find_one({"_id": k["commented_by"]})["username"])
        pg1.textEdit.setText(k)
        #pg1.layout.addWidget(pg1.label_3)

        #pg1.layout.addWidget(pg1.textEdit)
        mylayout = pg1.scroll.layout()
        mylayout.addWidget(pg1.label_3)
        mylayout.addWidget(pg1.textEdit)
    
if __name__=="__main__":
    
    mydic_list = list(requested_data.find({}))
    
    initialization()
    pg1.comentButton.clicked.connect(addcoment)
    pg1.requestButton.clicked.connect(addrequest)
    popup.saveButton.clicked.connect(savereq)
    pg1.saveButton.clicked.connect(savecmnt)
    
    mainpg.listWidget.itemDoubleClicked.connect(itemclicked)

    mainpg.show()
    renderlist()
    app.exec()
