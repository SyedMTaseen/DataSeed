
from PyQt5 import QtWidgets, uic,QtCore, QtGui,Qt
from PyQt5.QtWidgets import *
import ctypes
app = QtWidgets.QApplication([])


pg1 = uic.loadUi("./globalreq/QAA.ui")
popup = uic.loadUi("./globalreq/addrequest.ui")
mainpg = uic.loadUi("./globalreq/Requestpg.ui")

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
    ###DB se value ae gy
    ###SAAD DB currently login user ko abc se replace krna h
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
         ### baad ma db ajae ga yhn 
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
        ##SAAD DB coment ko store krwana h DB ma
        pg1.textEdit.setReadOnly(True)

def renderlist():
    for i in range(len(mydic_list)):
        layout = QHBoxLayout()
        layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        item = QListWidgetItem(mainpg.listWidget)
        ###SAAD DB mydic_list add all total requests!
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
        
        mainpg.listWidget.addItem(item)
        mainpg.listWidget.setItemWidget(item,widget)
def changestatus():
    ###check author h toh show kr do
    print("Simply DB se value modify krni h")
    ###SAAD DB status change kr do 
    pg1.Bresolve.hide()
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
    pg1.Ltitle.setText("Saad DB se "+str(i)+"th entry ka show kara do")
    ###SAAD DB request kia thi n kon kon se coment s the sab show karwao 

if __name__=="__main__":
    mydic_list=(
        {"title":"Request 1",
            "No of comment":"3",
            "Requested By":"Muaaz",
            "status":"Fullfilled"}, 

        {"title":"Request 2",
            "No of comment":"5",
            "Requested By":"Afroz",
            "status":"pending"})


    
    
    initialization()
    pg1.comentButton.clicked.connect(addcoment)
    pg1.requestButton.clicked.connect(addrequest)
    popup.saveButton.clicked.connect(savereq)
    pg1.saveButton.clicked.connect(savecmnt)
    pg1.Bresolve.clicked.connect(changestatus)
    mainpg.listWidget.itemDoubleClicked.connect(itemclicked)

    mainpg.show()
    renderlist()
    
    app.exec()
