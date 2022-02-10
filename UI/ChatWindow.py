from PyQt5 import QtCore, QtGui, QtWidgets
from components.SenderMsg import SenderMsg
from components.UserMsg import UserMsg
from components.ChatInput import ChatInput


class ChatWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChatWindow, self).__init__()
        self.setupUi()
        self.show()

    def onClick_send(self,message):
        if(len(message) == 0):return
        print(message)
        ##add message and spacer
        hbox1 = UserMsg(parent=self.userWidget,message=message)
        self.verticalLayout_2.insertLayout(len(self.verticalLayout_2)-1, hbox1)


    def setupUi(self):
        self.setObjectName("ChatWindow")
        self.resize(969, 740)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.userScroll = QtWidgets.QScrollArea()
        self.userWidget = QtWidgets.QWidget()

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.userWidget.setLayout(self.verticalLayout_2)
        # Scroll Area Properties
        self.userScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.userScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.userScroll.setWidgetResizable(True)
        self.userScroll.setWidget(self.userWidget)
        self.verticalLayout.addWidget(self.userScroll)
        
        self.verticalLayout.addLayout(self.verticalLayout_2)
        # component to send message
        self.chatHbox = ChatInput(self.centralwidget, self.onClick_send)
        self.verticalLayout.addLayout(self.chatHbox)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ChatWindow", "[Username]"))
        self.chatHbox.pushButton.setText(_translate("ChatWindow", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ChatWindow()
    sys.exit(app.exec_())
