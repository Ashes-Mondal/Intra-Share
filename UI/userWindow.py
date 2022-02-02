from threading import Thread
from PyQt5 import QtCore, QtWidgets, QtGui
from .UIComponents.MainHeading import MainHeading
from .UIComponents.MessageWindow import MessageWindow

class ButtonComponent:
    def __init__(self, centralwidget, index, clientOBJ, clientID, clientIns) -> None:
        centralwidget.setObjectName("centralwidget")
        self.clientID = clientID
        self.clientIns = clientIns
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

        self._translate = QtCore.QCoreApplication.translate
        self.label = clientOBJ.username
        self.userButton.setText(self._translate("MainWindow", self.label))
        self.userButton.clicked.connect(self.setCurrentUser)

    def setCurrentUser(self):
        self.UserWindow = QtWidgets.QMainWindow()
        self.UserWindow.setObjectName("ChatWindow2")
        self.UserWindow.resize(801, 830)
        self.msg_centralwidget = QtWidgets.QWidget(self.UserWindow)
        self.msg_centralwidget.setObjectName("msg_centralwidget")

        self.msg_index = 0
        self.user = MessageWindow(self.msg_centralwidget, self.label)
        self.user.msgInput.returnPressed.connect(self.sendMessageFunc)
        self.user.sendMsgBtn.clicked.connect(self.sendMessageFunc)

        self.UserWindow.setCentralWidget(self.msg_centralwidget)
        try:
            self.__startSendingMessages(self.clientID)
        except Exception as err:
            print(err)
        self.UserWindow.show()

    def sendMessageFunc(self):
        message = self.user.msgInput.text()
        print(str(self.msg_index) + " " + message + "\n")
        if len(message) != 0:
            self.user.msgInput.clear()
            self.user.textBrowser.append(message)
            try:
                print(self.clientID, message)
                self.clientIns.sendMessage(self.clientID, message)
                print("SENT\n")
            except Exception as err:
                print(err)
            self.msg_index += 1

    def __receiveMessages(self, clientID: int):
        while True:
            message = self.clientIns.activeClients[clientID].messages.get()
            username = self.clientIns.activeClients[clientID].username
            self.user.textBrowser.append(username + ": " + message)

    def __startSendingMessages(self, clientID: int):
        receiveMessages_thread = Thread(target=self.__receiveMessages, args=(
            clientID,), daemon=True, name=f'receiveMessages_thread{clientID}')
        receiveMessages_thread.start()

        # display unread messages
        while self.clientIns.activeClients[clientID].messages.empty() == False:
            message = self.clientIns.activeClients[clientID].messages.get()
            username = self.clientIns.activeClients[clientID].username
            self.user.textBrowser.append(username + ": " + message)

class UserWindow(object):
    def __init__(self, clientIns) -> None:
        self.userDict = clientIns.activeClients
        self.clientIns = clientIns

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()

    def setupUi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow2")
        self.MainWindow.setFixedWidth(1183)
        self.MainWindow.setFixedHeight(855)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        _translate = QtCore.QCoreApplication.translate

        self.label_heading = MainHeading(self.centralwidget)

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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 90, 20, 731))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.allUsers.setText(_translate("MainWindow", "Users Available Right Now"))

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(400, 100, 781, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(400, 150, 781, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        # self.usersWidget = QtWidgets.QWidget(self.MainWindow)
        self.buttonObjs = []
        # self.userComponents = [self.currentUser, self.msgInput, self.sendMsg, self.sentMsg_1, self.line_2, self.line_3, self.msgTab, self.fileTab, self.recvMsg_1]
        index = 0
        for clientID, clientOBJ in self.userDict.items():
            btnObj = ButtonComponent(self.centralwidget, index, clientOBJ, clientID, self.clientIns)
            self.buttonObjs.append(btnObj)
            index += 1

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.MainWindow.show()

        # while True:
        #     # self.usersWidget = QtWidgets.QWidget(self.MainWindow)
        #     self.buttonObjs = []
        #     # self.userComponents = [self.currentUser, self.msgInput, self.sendMsg, self.sentMsg_1, self.line_2, self.line_3, self.msgTab, self.fileTab, self.recvMsg_1]
        #     index = 0
        #     for clientID, clientOBJ in self.userDict.items():
        #         btnObj = ButtonComponent(self.centralwidget, index, clientOBJ)
        #         self.buttonObjs.append(btnObj)
        #         index += 1
        #     time.sleep(5)Ui_MainWindow
