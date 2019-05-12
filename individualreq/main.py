
from PyQt5 import QtWidgets, uic,QtCore, QtGui,Qt
from PyQt5.QtWidgets import *
import ctypes
app = QtWidgets.QApplication([])
import pymongo
 
data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
ds_user = ds_db["user"]
curr_ds_user = ds_db["curr_user"]
requested_data = ds_db["requested_data"]
deleted_request = ds_db["deleted_request"]
cu = curr_ds_user.find_one({})["_id"]

pg1 = uic.loadUi("./individualreq/QAA.ui")
#pg1 = uic.loadUi("QAA.ui")
#pg2 = uic.loadUi("myrequest.ui")
#dialog=uic.loadUi("Lwarning box.ui")
index=None
pg2 = uic.loadUi("./individualreq/myrequest.ui")
dialog=uic.loadUi("./individualreq/Lwarning box.ui")

def itemclicked(iteem):
    global index 
    i=0;
    while i<5:
        if(pg2.listWidget.item(i)== iteem):
            index=i

            break
        i=i+1
    pg2.hide()
    pg1.show()
    pg1.requestButton.hide()
    pg1.Ltitle.setText("Saad DB se "+str(i)+"th entry ko show kara do")
    
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
    # if (request["status"]=='Fulfilled'):
    
    pg1.Ltitle.setText(request['title'])
    pg1.desbox.setText(request['description'])

    for k in comments_of_request:
        pg1.textEdit = QtWidgets.QTextEdit(pg1.centralwidget)
        pg1.textEdit.setGeometry(QtCore.QRect(10, 390, 721, 71))

        pg1.textEdit.setMinimumHeight(31)
        pg1.textEdit.setMaximumHeight(31)

        pg1.label_3 = QtWidgets.QLabel(pg1.centralwidget)
        pg1.label_3.setMinimumHeight(24)
        pg1.label_3.setMaximumHeight(28)
        
             
        pg1.label_3.setText("Commented by:", ds_user.find_one({"_id": k["commented_by"]})["username"])
        pg1.textEdit.setText(k["comment"])
        #pg1.layout.addWidget(pg1.label_3)

        #pg1.layout.addWidget(pg1.textEdit)
        mylayout = pg1.scroll.layout()
        mylayout.addWidget(pg1.label_3)
        mylayout.addWidget(pg1.textEdit)


def changestatus():
    ###check author h toh show kr do
    
    # Updates status of the ith request to "Fulfilled"
    global index
    x = requested_data.update({"_id": mydic_list[index]["_id"]}, {'$set': {"status":"Fulfilled"}})
    
    print("Simply DB se value modify krni h")
    pg1.Bresolve.hide()
    
def renderlist():

    for i in range(len(mydic_list)):
        print(mydic_list[i])
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(pg2.listWidget)
        ####SAAD DB currently login user keh comment dikhao
        label = QLabel(str(i+1)+ ") Title:" + mydic_list[i]['title'] + "\n" + "     Request By: " + ds_user.find_one({"_id": mydic_list[i]['requested_by']})["username"])
        label.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;font-style: normal;font-weight:100")
        label.setWordWrap(True);
        
        label2 = QLabel("No of comments " + str(len(mydic_list[i]['comments'])) + '\nStatus: ' + mydic_list[i]['status'])
        label2.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;text-align:right")
        label2.setAlignment(QtCore.Qt.AlignCenter)
        label2.setWordWrap(True)

        

        layout.addWidget(label)
        layout.addWidget(label2)
        
        widget = QWidget()
        widget.setStyleSheet("height:fit-content;width:100%");
        widget.setLayout(layout);
        
        item.setSizeHint(layout.sizeHint())
        
        pg2.listWidget.addItem(item)
        pg2.listWidget.setItemWidget(item,widget)


def deleteitem():
    
    if not pg2.listWidget.selectedItems():
        pg2.Lerror.setStyleSheet("QLabel {color:red;}")
        pg2.Lerror.setText("Select any Item")

    else:
        global index
        pg2.Lerror.setText(" ")   

        i=0;
        while i<5:
            if(pg2.listWidget.item(i)== pg2.listWidget.currentItem()):
                index=i;
                break
            i=i+1


        print(index)
        dialog.show()
        
    
def yespressed():
    dialog.hide()
    global index
    pg2.listWidget.takeItem(index)
    
    # Delete current request directly from database
    y = deleted_request.insert(mydic_list[index])
    x = requested_data.remove_one({"_id": mydic_list[index]["_id"]})
    
    # Delete current request from provided mydic_list
    mydic_list.pop(index)
    
    #renderlist()
    

def nopressed():
    dialog.hide()


if __name__=="__main__":
    
    mydic_list = list(requested_data.find({"requested_by":cu}))

    pg1.layout.setAlignment(QtCore.Qt.AlignTop)
    pg1.scrollArea.setWidgetResizable(True)

    pg1.scrollArea.setWidget(pg1.scroll)
    pg1.scroll.setLayout(pg1.layout)

    pg2.listWidget.itemDoubleClicked.connect(itemclicked)
    pg2.deleteButton.clicked.connect(deleteitem)
    pg1.Bresolve.clicked.connect(changestatus)
    dialog.yesButton.clicked.connect(yespressed)
    dialog.noButton.clicked.connect(nopressed)

    pg2.show()
    renderlist()
    
    app.exec()

