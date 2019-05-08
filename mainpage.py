
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets,uic,Qt
from PyQt5.QtWidgets import QLayout, QSizePolicy,QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem,     QHBoxLayout



app = QtWidgets.QApplication([])

mpg=uic.loadUi("main page.ui")
pg1 = uic.loadUi("./individualreq/QAA.ui")
popup = uic.loadUi("./globalreq/addrequest.ui")
     

    
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
    for i in range(len(mydic_list)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(mpg.listWidget_3)
        # SAAD DB user purchase history
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
        
        mpg.listWidget_3.addItem(item)
        mpg.listWidget_3.setItemWidget(item,widget)
def renderselllist():
    for i in range(len(mydic_list)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(mpg.listWidget_3)
        # SAAD DB user want to sell
        label = QLabel(str(i+1)+ ") Title:" + mydic_list2[i]['title'] + "\n" + "     Request By: " + mydic_list[i]['Requested By'])
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
        
        mpg.listWidget_3.addItem(item)
        mpg.listWidget_3.setItemWidget(item,widget)
def rendersearchlist():
    for i in range(len(mydic_list1)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(mpg.listWidget_2)
        # SAAD DB user had already searches 
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
    
def deleterequest():
    if not mpg.listWidget_3.selectedItems():
        mpg.Lerror1.setStyleSheet("QLabel {color:red;}")
        mpg.Lerror1.setText("Select any Item")

    else:
        mpg.Lerror1.setText(" ")

        i=0;
        while i<5:
            if(mpg.listWidget_3.item(i)== mpg.listWidget_3.currentItem()):
                break
            i=i+1

        
        
        mpg.listWidget_3.takeItem(i)
        #SAAD DB jo request ith index p h usko del kr do
        ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
        #mydic_list.pop(i)
        #renderlist()
def deleterecord():
    if not mpg.listWidget_2.selectedItems():
        mpg.Lerror2.setStyleSheet("QLabel {color:red;}")
        mpg.Lerror2.setText("Select any Item")

    else:
        mpg.Lerror2.setText(" ")   

        i=0;
        while i<5:
            if(mpg.listWidget_2.item(i)== mpg.listWidget_2.currentItem()):
                break
            i=i+1

        
        
        mpg.listWidget_2.takeItem(i)
        #SAAD DB user ke searches ma data ure do 
        ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
        #mydic_list.pop(i)
        #renderlist()

def deletedata():
    if not mpg.listWidget.selectedItems():
        mpg.Lerror3.setStyleSheet("QLabel {color:red;}")
        mpg.Lerror3.setText("Select any Item")

    else:
        mpg.Lerror3.setText(" ")   

        i=0;
        while i<5:
            if(mpg.listWidget.item(i)== mpg.listWidget.currentItem()):
                break
            i=i+1

        
        
        mpg.listWidget.takeItem(i)
        ### SAAD DB delete kr do data jo user ko sell kr na h 
        ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
        #mydic_list.pop(i)
        #renderlist()
def itemclicked(iteem):
    i=0;
    while i<5:
        if(mpg.listWidget_3.item(i)== iteem):
            break
        i=i+1
    mpg.hide()
    pg1.show()
    pg1.requestButton.hide()
    ###SAAD DB 
    pg1.Ltitle.setText("Saad DB se "+str(i)+"th entry ko show kara do")
    ###SAAD DB request kia thi n kon kon se coment s the sab show karwao 

def savereq():
    if not popup.Ttitle.toPlainText():
        popup.Lerror.setStyleSheet("QLabel {color:red;}")
        popup.Lerror.setText("Title for request is required!")
    elif not popup.desbox.toPlainText():
        popup.Lerror.setStyleSheet("QLabel {color:red;}")
        popup.Lerror.setText("Enter atleast 10 words")
    else:
         ### baad ma db ajae ga yhn
         # SAAD DB request save karo user ke 
        pg1.Ltitle.setText(popup.Ttitle.toPlainText())
        pg1.desbox.setText(popup.desbox.toPlainText())
        popup.hide()       
        
if __name__ == "__main__":
    mydic_list=(
        {"title":"Request 2",
            "No of comment":"5",
            "Requested By":"Hamzaaa",
            "status":"Fullfilled"}, 

        {"title":"Request 3",
            "No of comment":"9",
            "Requested By":"Aomore",
            "status":"pending"})
    mydic_list1=['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
    mpg.purchase_btn.clicked.connect(CalculateTax)
    mpg.sell_btn.clicked.connect(CalculateTax2)
    mpg.view_req_btn.clicked.connect(CalculateTax3)
    mpg.post_req_btn.clicked.connect(CalculateTax4)
    #mpg.deletereq.clicked.connect(deleterequest)
    mpg.listWidget_3.itemDoubleClicked.connect(itemclicked)
    popup.saveButton.clicked.connect(savereq)
    mpg.deleterecord.clicked.connect(deleterecord)
    mpg.deletedata.clicked.connect(deletedata)
    mpg.myreqButton.clicked.connect(CalculateTax5)

    mpg.show()
    renderpurchaselist()
    rendersearchlist()
    app.exec()

