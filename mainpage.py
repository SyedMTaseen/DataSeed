
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets,uic,Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy,QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem,     QHBoxLayout
import pymongo
import datetime

data_client = pymongo.MongoClient("mongodb://localhost/")
ds_db = data_client["dataseed_db"]
ds_db_user = ds_db["curr_user"]
cu = ds_db_user.find({})["_id"]

ds_datasets = ds_db["dataset"]

app = QtWidgets.QApplication([])

mpg=uic.loadUi("main page.ui")
pg1 = uic.loadUi("./individualreq/QAA.ui")
popup = uic.loadUi("./globalreq/addrequest.ui")
dialog = uic.loadUi("warning box.ui")     
flag=0
index=None
    
def CalculateTax( ):
    os.system('python homepage.py')
def CalculateTax2():
    os.system('python selldata.py')
def CalculateTax3():
    os.system('python ./globalreq/main.py')
def CalculateTax4():
    popup.show()
def CalculateTax5():
    os.system('python ./individualreq/main.py')

def renderpurchaselist():
    
    for i in mydic_list:

        if (i["bought_by"]==cu):      
    
    #for i in range(len(mydic_list)):
            layout = QHBoxLayout()
            layout.setSizeConstraint(QLayout.SetMinimumSize)
            
            item = QListWidgetItem(mpg.listWidget_3)
            # SAAD DB DONE COMMENTED

            label = QLabel(str(i+1)+ ") Title:" + i['title'] + "\n" + "     Request By: " + i['Requested By']+"\n" +"     Rating: " + str(i['rating']) + "/5")
            label.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;font-style: normal;font-weight:100")
            label.setWordWrap(True);
            
            label2 = QLabel("No of comments " + i['No of comment'] + '\nStatus: ' + i['status'])
            label2.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;text-align:right")
            label2.setAlignment(QtCore.Qt.AlignCenter)
            label2.setWordWrap(True)

            

            layout.addWidget(label)
            layout.addWidget(label2)
            
            widget = QWidget()
            widget.setStyleSheet("height:fit-content;width:100%");
            widget.setLayout(layout);
            
            item.setSizeHint(layout.sizeHint())
            
            mpg.listWidget_3.addItem(item)
            mpg.listWidget_3.setItemWidget(item,widget)
def renderselllist():
    
    for i in mydic_list:
        if (i["uploaded_by"]==cu and i["status"]=="For Sale"):
#             EVERYTHING HERE with i
#             pass
#         pass

#    for i in range(len(mydic_list)):
            layout = QHBoxLayout()
            layout.setSizeConstraint(QLayout.SetMinimumSize)
            
            item = QListWidgetItem(mpg.listWidget_3)
            # SAAD DB DONE COMMENTED
            label = QLabel(str(i+1)+ ") Title:" + i['title'] + "\n" + "     Request By: " + i['Requested By']+ "\n" +"Rating: " + str(i['rating']) + "/5")
            label.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;font-style: normal;font-weight:100")
            label.setWordWrap(True);
            
            label2 = QLabel("No of comments " + i['No of comment'] + '\nStatus: ' + i['status'])
            label2.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;text-align:right")
            label2.setAlignment(QtCore.Qt.AlignCenter)
            label2.setWordWrap(True)

            

            layout.addWidget(label)
            layout.addWidget(label2)
            
            widget = QWidget()
            widget.setStyleSheet("height:fit-content;width:100%");
            widget.setLayout(layout);
            
            item.setSizeHint(layout.sizeHint())
            
            mpg.listWidget_3.addItem(item)
            mpg.listWidget_3.setItemWidget(item,widget)
def rendersearchlist():
#     mydic_list1 has all the search history. You can iterate with the keywords
#     for i in mydic_list1 
    for i in range(len(mydic_list1)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(mpg.listWidget_2)
        # SAAD DB DONE COMMENTED BELOW in main  
        label = QLabel(str(i+1)+ ") " + mydic_list1[i] )
        label.setStyleSheet("height:fit-content;font-size:12pt;font-family: Segoe UI;font-style: normal;font-weight:100")
        label.setWordWrap(True);
        
        
        

        layout.addWidget(label)
        
        widget = QWidget()
        widget.setStyleSheet("height:fit-content;width:100%");
        widget.setLayout(layout);
        
        item.setSizeHint(layout.sizeHint())
        
        mpg.listWidget_2.addItem(item)
        mpg.listWidget_2.setItemWidget(item,widget)
    
# def deleterequest():
#     if not mpg.listWidget_3.selectedItems():
#         mpg.Lerror1.setStyleSheet("QLabel {color:red;}")
#         mpg.Lerror1.setText("Select any Item")

#     else:
#         mpg.Lerror1.setText(" ")

#         i=0;
#         while i<5:
#             if(mpg.listWidget_3.item(i)== mpg.listWidget_3.currentItem()):
#                 break
#             i=i+1

        
        
#         mpg.listWidget_3.takeItem(i)
#         #SAAD DB ? jo request ith index p h usko del kr do
#         ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
#         #mydic_list.pop(i)
#         #renderlist()
def deleterecord():
    if not mpg.listWidget_2.selectedItems():
        mpg.Lerror2.setStyleSheet("QLabel {color:red;}")
        mpg.Lerror2.setText("Select any Item")

    else:
        mpg.Lerror2.setText(" ") 
        global index  

        i=0;
        while i<5:
            if(mpg.listWidget_2.item(i)== mpg.listWidget_2.currentItem()):
                index=i
                break
            i=i+1

        flag=1
        dialog.show()


def yespressed():
    dialog.hide()
    global index
    if flag==1:

        mpg.listWidget_2.takeItem(index)
        #SAAD DB ? user ke searches ma data ure do 
        ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
        #mydic_list.pop(i)
        #renderlist()
        
    elif flag==2:
        mpg.listWidget.takeItem(index)
        ### SAAD DB ? delete kr do data jo user ko sell kr na h 
        ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
        #mydic_list.pop(i)
        #renderlist()

def nopressed():
    dialog.hide()

def deletedata():
    if not mpg.listWidget.selectedItems():
        mpg.Lerror3.setStyleSheet("QLabel {color:red;}")
        mpg.Lerror3.setText("Select any Item")

    else:
        mpg.Lerror3.setText(" ")
        global index   

        i=0;
        while i<5:
            if(mpg.listWidget.item(i)== mpg.listWidget.currentItem()):
                index=i
                break
            i=i+1

        flag=2
        dialog.show()
        
        
# def itemclicked(iteem):
#     i=0;
#     while i<5:
#         if(mpg.listWidget_3.item(i)== iteem):
#             break
#         i=i+1
#     mpg.hide()
#     pg1.show()
#     pg1.requestButton.hide()
#     ###SAAD DB ?
#     pg1.Ltitle.setText("Saad DB se "+str(i)+"th entry ko show kara do")
#     ###SAAD DB ? request kia thi n kon kon se coment s the sab show karwao 

def savereq():
    if not popup.Ttitle.toPlainText():
        popup.Lerror.setStyleSheet("QLabel {color:red;}")
        popup.Lerror.setText("Title for request is required!")
    elif not popup.desbox.toPlainText():
        popup.Lerror.setStyleSheet("QLabel {color:red;}")
        popup.Lerror.setText("Enter atleast 10 words")
    else:
        #SAAD DB DONE COMMENTED BUT SPECIFY THE FIELDS PLEASE
        q = requested_data.insert({"title": popup.Ttitle.toPlainText(), "description": popup.desbox.toPlainText(), "requested_by":cu,"requested_on": datetime.datetime.now(),"status":"Pending"})
        # insert all info regarding the new requested data
        pg1.Ltitle.setText(popup.Ttitle.toPlainText())
        pg1.desbox.setText(popup.desbox.toPlainText())
        popup.hide()       
        
if __name__ == "__main__":
#   mydic_list = list(ds_datasets.find({"bought_by": cu}))
    mydic_list = list(ds_datasets.find({}))

    mydic_list1= ds_user.find_one({"username":cu}, {"search_history":1,"_id":0})["search_history"]
    mpg.purchase_btn.clicked.connect(CalculateTax)
    mpg.sell_btn.clicked.connect(CalculateTax2)
    mpg.view_req_btn.clicked.connect(CalculateTax3)
    mpg.post_req_btn.clicked.connect(CalculateTax4)
    #mpg.deletereq.clicked.connect(deleterequest)
    # mpg.listWidget_3.itemDoubleClicked.connect(itemclicked)   // pasha lagai ga on list widget 2 
    popup.saveButton.clicked.connect(savereq)
    mpg.deleterecord.clicked.connect(deleterecord)
    mpg.deletedata.clicked.connect(deletedata)
    mpg.myreqButton.clicked.connect(CalculateTax5)
    dialog.yesButton.clicked.connect(yespressed)
    dialog.noButton.clicked.connect(nopressed)

    mpg.show()
    renderpurchaselist()
    rendersearchlist()
    app.exec()

