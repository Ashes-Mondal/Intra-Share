from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, currentThread

class MessageWindow(QtWidgets.QMainWindow):
    def __init__(self, label, clientIns, clientID, userid, parent) -> None:
        super(MessageWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.label = label
        self.clientIns = clientIns
        self.clientID = clientID
        # self.parent = parent
        self.setParent(parent)

        try:
            self.__startSendingMessages(clientID)
        except Exception as err:
            print(err)
            self.close()


        self.setObjectName("ChatWindow2")
        self.setFixedWidth(801)
        self.setFixedHeight(830)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("msg_centralwidget")

        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(80, 10, 641, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setStyleSheet("border: 2px solid red;\n"
        "border-radius: 10px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 255, 255);\n"
        "background-color: rgb(85, 0, 127);")
        self.label_heading.setObjectName("label_heading")

        self.msgInput = QtWidgets.QLineEdit(self.centralwidget)
        self.msgInput.setGeometry(QtCore.QRect(10, 710, 671, 61))
        self.msgInput.setStyleSheet("border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "font-size: 20px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);")
        self.msgInput.setObjectName("msgInput")

        self.currentUser = QtWidgets.QPushButton(self.centralwidget)
        self.currentUser.setGeometry(QtCore.QRect(10, 80, 781, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currentUser.setFont(font)
        self.currentUser.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.currentUser.setStyleSheet("text-align: left;\n"
        "padding-left: 20px;\n"
        "padding-right: 10px;\n"
        "border: 2px solid black;\n"
        "color: rgb(85, 0, 127);")
        self.currentUser.setObjectName("currentUser")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 130, 781, 571))
        self.textBrowser.setStyleSheet("font-size: 18px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n")  # rgb(255, 255, 0);
        self.textBrowser.setObjectName("textBrowser")

        self.sendMsgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendMsgBtn.setGeometry(QtCore.QRect(690, 710, 101, 61))
        self.sendMsgBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendMsgBtn.setStyleSheet("border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "font-size: 18px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);")
        self.sendMsgBtn.setObjectName("sendMsgBtn")

        self.retranslateUi()
        self.setWindowTitle(userid + " calling " + self.label)
        self.setCentralWidget(self.centralwidget)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_heading.setText(_translate("MainWindow", "WELCOME TO THE LOCAL DC++ PROJECT"))
        self.msgInput.setPlaceholderText(_translate("MainWindow", "Type a message"))
        self.currentUser.setText(_translate("MainWindow", self.label))
        self.sendMsgBtn.setText(_translate("MainWindow", "SEND"))
        self.msgInput.returnPressed.connect(self.sendMessageFunc)
        self.sendMsgBtn.clicked.connect(self.sendMessageFunc)

    def closeEvent(self, event):
        event.accept()
        print('Message Window closed')
        try:
            # TODO: Lock to be applied
            print("Before: ", len(self.clientIns.activeMessagingClient))
            if self.clientID in self.clientIns.activeMessagingClient.keys():
                del self.clientIns.activeMessagingClient[self.clientID]
            print("After: ", len(self.clientIns.activeMessagingClient))
        except Exception as err:
            print(err)

    def sendMessageFunc(self):
        message = self.msgInput.text()
        msg_index = 0
        print(str(msg_index) + " " + message + "\n")
        if len(message) != 0:
            try:
                print(self.clientID, message)
                self.clientIns.sendMessage(self.clientID, message)
                print("SENT\n")
                self.msgInput.clear()
                print(self)
                self.textBrowser.append(message)
                msg_index += 1
            except Exception as err:
                print(err)

    def __receiveMessages(self, clientID: int):
        try:
            while True:
                message = self.clientIns.activeClients[clientID].messages.get()
                username = self.clientIns.activeClients[clientID].username
                msg_str = username + ": " + message
                print(self)
                self.textBrowser.append(msg_str)
                print(username + ": " + message)
        except Exception as err:
            print(currentThread().getName())
            print(f"Thread Closed, ", err)

    def __startSendingMessages(self, clientID: int):
        receiveMessages_thread = Thread(target=self.__receiveMessages, args=(
            clientID,), daemon=True, name=f'receiveMessages_thread{clientID}')
        receiveMessages_thread.start()

        self.clientIns.activeMessagingClient[clientID] = 1

        # display unread messages
        while self.clientIns.activeClients[clientID].messages.empty() == False:
            message = self.clientIns.activeClients[clientID].messages.get()
            username = self.clientIns.activeClients[clientID].username
            self.textBrowser.append(username + ": " + message)
