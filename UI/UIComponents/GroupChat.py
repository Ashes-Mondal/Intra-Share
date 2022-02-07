from PyQt5 import QtCore, QtGui, QtWidgets

class GroupChat():
    def __init__(self, centralwidget) -> None:
        self.centralwidget = centralwidget
        self.msgInput = QtWidgets.QLineEdit(self.centralwidget)
        self.msgInput.setGeometry(QtCore.QRect(410, 740, 681, 61))
        self.msgInput.setStyleSheet("border: 2px solid black;\n"
        "font-size: 20px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);")
        self.msgInput.setObjectName("msgInput")

        self.grpChat = QtWidgets.QPushButton(self.centralwidget)
        self.grpChat.setGeometry(QtCore.QRect(400, 100, 781, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.grpChat.setFont(font)
        self.grpChat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.grpChat.setStyleSheet("text-align: left;\n"
        "padding-left: 20px;\n"
        "padding-right: 10px;\n"
        "border-top: 2px solid black;\n"
        "border-bottom: 2px solid black;\n"
        "color: rgb(85, 0, 127);")
        self.grpChat.setObjectName("grpChat")
        
        self.allUsers = QtWidgets.QPushButton(self.centralwidget)
        self.allUsers.setGeometry(QtCore.QRect(0, 100, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.allUsers.setFont(font)
        self.allUsers.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.allUsers.setStyleSheet("text-align: left;\n"
        "padding-left: 35;\n"
        "padding-right: 10px;\n"
        "border: 2px solid black;\n"
        "border-left: none;\n"
        "color: rgb(85, 0, 127);")
        self.allUsers.setObjectName("allUsers")

        self.sendGrpMsg = QtWidgets.QPushButton(self.centralwidget)
        self.sendGrpMsg.setGeometry(QtCore.QRect(1100, 740, 71, 61))
        self.sendGrpMsg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendGrpMsg.setStyleSheet("text-align: left;\n"
        "font-size: 20px;\n"
        "border: 2px solid black;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);")
        self.sendGrpMsg.setObjectName("sendGrpMsg")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(410, 160, 761, 571))
        self.textBrowser.setStyleSheet("border: 2px solid black;")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.msgInput.setPlaceholderText(_translate("MainWindow", "Type a message"))
        self.grpChat.setText(_translate("MainWindow", "Group Chat"))
        self.allUsers.setText(_translate("MainWindow", "Users Available Right Now"))
        self.sendGrpMsg.setText(_translate("MainWindow", "Send"))
