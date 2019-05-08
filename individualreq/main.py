
from PyQt5 import QtWidgets, uic,QtCore, QtGui,Qt
from PyQt5.QtWidgets import *
import ctypes
app = QtWidgets.QApplication([])


pg1 = uic.loadUi("./individualreq/QAA.ui")
pg2 = uic.loadUi("./individualreq/myrequest.ui")

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
    ###SAAD DB request kia thi n kon kon se coment s the sab show karwao 

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
        pg2.Lerror.setText(" ")   

        i=0;
        while i<5:
            if(pg2.listWidget.item(i)== pg2.listWidget.currentItem()):
                break
            i=i+1

        print(i)
        
        pg2.listWidget.takeItem(i)
        ###SAAD DB currently login ke ith index wali request delete krwa do
        ###delete from DB also!!!.....foran hone zarori h wrna index ma msle ajen gy
        #mydic_list.pop(i)
        #renderlist()




if __name__=="__main__":
    mydic_list=(
        {"title":"Request 2",
            "No of comment":"5",
            "Requested By":"Hamzaaa",
            "status":"Fullfilled"}, 

        {"title":"Request 3",
            "No of comment":"9",
            "Requested By":"Aomore",
            "status":"pending"})

    pg2.listWidget.itemDoubleClicked.connect(itemclicked)
    pg2.deleteButton.clicked.connect(deleteitem)

    pg2.show()
    renderlist()
    
    app.exec()

