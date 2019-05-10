
from PyQt5 import QtWidgets, uic,QtCore, QtGui,Qt
from PyQt5.QtWidgets import *
import ctypes
app = QtWidgets.QApplication([])
import pymongo

data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
curr_db_user = ds_db["curr_user"]
cu = curr_db_user.find_one({})["_id"]

pg1 = uic.loadUi("./individualreq/QAA.ui")
#pg1 = uic.loadUi("QAA.ui")
#pg2 = uic.loadUi("myrequest.ui")
#dialog=uic.loadUi("Lwarning box.ui")
index=None
pg2 = uic.loadUi("./individualreq/myrequest.ui")
dialog=uic.loadUi("./individualreq/Lwarning box.ui")

def itemclicked(iteem):
    i=0;
    while i<5:
        if(pg2.listWidget.item(i)== iteem):
            break
        i=i+1
    pg2.hide()
    pg1.show()
    pg1.requestButton.hide()
    pg1.Ltitle.setText("Saad DB se "+str(i)+"th entry ko show kara do")
    # dataset = requested_data.find({mydic_list[i]["_id"]})
    # mydic_list[i]

    # for com in mydic_list[i]["comments"].items()
    # com["comment"] ; com["commented_by"]
    ###SAAD DB request kia thi n kon kon se coment s the sab show karwao
    ##SAAD DB se status fullfil h Ith request ke toh true ya false ma store kara do ek new varaible bana kr 
    
    pg1.Ltitle.setText(mydic_list2[i]['title'])
    pg1.desbox.setText(mydic_list2[i]['request'])
    ###SAAD DB ....dekh len kese coments access hongy mjhe smjh ni arha 

    for k in mydic_list2[i]['comment']:
        pg1.textEdit = QtWidgets.QTextEdit(pg1.centralwidget)
        pg1.textEdit.setGeometry(QtCore.QRect(10, 390, 721, 71))

        pg1.textEdit.setMinimumHeight(31)
        pg1.textEdit.setMaximumHeight(31)

        pg1.label_3 = QtWidgets.QLabel(pg1.centralwidget)
        pg1.label_3.setMinimumHeight(24)
        pg1.label_3.setMaximumHeight(28)


        # cu = user.find_one({"_id":curr_user["_id"])}
        # abc will be: cu["username"]
        pg1.label_3.setText( "Comment By:")
        pg1.textEdit.setText(k)
        #pg1.layout.addWidget(pg1.label_3)

        #pg1.layout.addWidget(pg1.textEdit)
        mylayout = pg1.scroll.layout()
        mylayout.addWidget(pg1.label_3)
        mylayout.addWidget(pg1.textEdit)


def changestatus():
    ###check author h toh show kr do
    # x = requested_data.update({"_id": mydic_list[i]["_id"]}, {$set: {"status":"Fulfilled"}})
    print("Simply DB se value modify krni h")
    pg1.Bresolve.hide()

    ###SAAD DB status change kr do
def renderlist():
    for i in range(len(mydic_list)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(pg2.listWidget)
        ####SAAD DB currently login user keh comment dikhao
        label = QLabel(str(i+1)+ ") Title:" + mydic_list[i]['title'] + "\n" + "     Request By: " + mydic_list[i]['Requested By'])
        label.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;font-style: normal;font-weight:100")
        label.setWordWrap(True);
        
        label2 = QLabel("No of comments " + mydic_list[i]['No of comment'] + '\nStatus: ' + mydic_list[i]['status'])
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


if __name__=="__main__":
    mydic_list = list(requested_data.find({"requested_by":cu}))
        print(index)
        dialog.show()
        
    
def yespressed():
    dialog.hide()
    global index
    pg2.listWidget.takeItem(index)
    ###SAAD DB currently login ke ith index wali request delete krwa do
    ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
    #mydic_list.pop(i)
    #renderlist()
    

def nopressed():
    dialog.hide()


if __name__=="__main__":
    mydic_list=(
        {"_id": "234wd",
        "title":"Request 2",
            "No of comment":"5",
            "Requested By":"Hamzaaa",
            "status":"Fullfilled"}, 

        {"title":"Request 3",
            "No of comment":"9",
            "Requested By":"Aomore",
            "status":"pending"})
    mydic_list2=(
        {"title":"Request 2",
        "request":"Help me tatata",
        "comment by":"testing1",
        "comment":"check1",
        "comment by":"testing2",
        "comment":"check2",
        "comment by":"testing3",
        "comment":"check3"}, 

        {"title":"Request 3",
        "request":"Help me urgent",
        "comment by":"testing5",
        "comment":"check5",
        "comment by":"testing6",
        "comment":"check6",
        "comment by":"testing7",
        "comment":"check7"})

    mydic_list[0]['_id']


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