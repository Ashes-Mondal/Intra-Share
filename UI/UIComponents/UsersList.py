from PyQt5 import QtCore, QtWidgets, QtGui

class ButtonComponent:
    def __init__(self, centralwidget, index, clientOBJ) -> None:
        centralwidget.setObjectName("centralwidget")
        self.userButton = QtWidgets.QPushButton(centralwidget)
        self.userButton.setGeometry(QtCore.QRect(30, 160 + (index * 90), 341, 61))
        self.userButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.userButton.setStyleSheet("text-align: left;\n"
        "font-size: 20px;\n"
        "border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);")
        self.userButton.setObjectName("userButton" + str(index + 1))

        _translate = QtCore.QCoreApplication.translate
        self.label = clientOBJ.username
        self.userButton.setText(_translate("MainWindow", self.label))
        # self.userButton.clicked.connect(self.setCurrentUser)
    
    # def setCurrentUser(self):
    #     self.msgInput.setGeometry(QtCore.QRect(420, 720, 671, 61))
    #     self.sendMsg.setGeometry(QtCore.QRect(1110, 730, 51, 41))
    #     self.sentMsg_1.setGeometry(QtCore.QRect(420, 160, 151, 51))
    #     self.msgTab.setGeometry(QtCore.QRect(880, 100, 151, 51))
    #     self.fileTab.setGeometry(QtCore.QRect(1030, 100, 151, 51))
    #     self.recvMsg_1.setGeometry(QtCore.QRect(420, 220, 271, 51))

    #     _translate = QtCore.QCoreApplication.translate
    #     self.currentUser.setText(_translate("MainWindow", self.label))
    #     self.msgTab.setText(_translate("MainWindow", "Send Message"))
    #     self.fileTab.setText(_translate("MainWindow", "Send Files"))
    #     self.msgInput.setPlaceholderText(_translate("MainWindow", "Type a message"))
    #     self.sendMsg.setText(_translate("MainWindow", "CommandLinkButton"))
    #     self.sentMsg_1.setText(_translate("MainWindow", "Message Sent"))
    #     self.recvMsg_1.setText(_translate("MainWindow", "Message Received"))