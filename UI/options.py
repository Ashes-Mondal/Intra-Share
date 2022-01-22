from http import client
from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonComponent:
    def __init__(self, centralwidget, index, clientOBJ, userComponents) -> None:
        self.currentUser = userComponents[0]
        self.msgInput = userComponents[1]
        self.sendMsg = userComponents[2]
        self.sentMsg_1 = userComponents[3]
        self.line_2 = userComponents[4]
        self.line_3 = userComponents[5]
        self.msgTab = userComponents[6]
        self.fileTab = userComponents[7]
        self.recvMsg_1 = userComponents[8]
        
        self.centralwidget = centralwidget
        self.label = clientOBJ.username
        self.userButton = QtWidgets.QPushButton(self.centralwidget)
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
        self.userButton.setText(_translate("MainWindow", self.label))
        self.userButton.clicked.connect(self.setCurrentUser)
    
    def setCurrentUser(self):
        self.msgInput.setGeometry(QtCore.QRect(420, 720, 671, 61))
        self.sendMsg.setGeometry(QtCore.QRect(1110, 730, 51, 41))
        self.sentMsg_1.setGeometry(QtCore.QRect(420, 160, 151, 51))
        self.msgTab.setGeometry(QtCore.QRect(880, 100, 151, 51))
        self.fileTab.setGeometry(QtCore.QRect(1030, 100, 151, 51))
        self.recvMsg_1.setGeometry(QtCore.QRect(420, 220, 271, 51))

        _translate = QtCore.QCoreApplication.translate
        self.currentUser.setText(_translate("MainWindow", self.label))
        self.msgTab.setText(_translate("MainWindow", "Send Message"))
        self.fileTab.setText(_translate("MainWindow", "Send Files"))
        self.msgInput.setPlaceholderText(_translate("MainWindow", "Type a message"))
        self.sendMsg.setText(_translate("MainWindow", "CommandLinkButton"))
        self.sentMsg_1.setText(_translate("MainWindow", "Message Sent"))
        self.recvMsg_1.setText(_translate("MainWindow", "Message Received"))
        

class Options_MainWindow():
    def __init__(self, clientIns) -> None:
        self.clientIns = clientIns

    def setupUi(self, MainWindow):
        # temp data from the server
        # print(self.clientIns.activeClients) #dict
        userDict = self.clientIns.activeClients

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(260, 30, 641, 61))
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
        
        self.currentUser = QtWidgets.QPushButton(self.centralwidget)
        self.currentUser.setGeometry(QtCore.QRect(400, 100, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currentUser.setFont(font)
        self.currentUser.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.currentUser.setStyleSheet("text-align: left;\n"
        "padding-left: 20px;\n"
        "padding-right: 10px;\n"
        "border-top: 2px solid black;\n"
        "border-bottom: 2px solid black;\n"
        "color: rgb(85, 0, 127);")
        self.currentUser.setObjectName("currentUser")

        self.msgInput = QtWidgets.QLineEdit(self.centralwidget)
        self.msgInput.setStyleSheet("border: 2px solid black;\n"
        "border-radius: 10px;\n"
        "font-size: 20px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);")
        self.msgInput.setObjectName("msgInput")

        self.sendMsg = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.sendMsg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendMsg.setStyleSheet("border: 3px solid rgb(85, 0, 127);\n"
        "border-radius: 10px;\n"
        "color: rgb(255, 255, 127);\n"
        "background-color: rgb(255, 255, 127);")
        self.sendMsg.setObjectName("sendMsg")

        self.sentMsg_1 = QtWidgets.QLabel(self.centralwidget)
        self.sentMsg_1.setStyleSheet("border: 2px solid black;\n"
        "border-radius: 5px;\n"
        "font-size: 18px;\n"
        "padding-left: 5;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(85, 255, 255);")
        self.sentMsg_1.setObjectName("sentMsg_1")

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

        self.msgTab = QtWidgets.QPushButton(self.centralwidget)
        self.msgTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.msgTab.setStyleSheet("font-size: 20px;\n"
        "border: 2px solid black;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);")
        self.msgTab.setObjectName("msgTab")

        self.fileTab = QtWidgets.QPushButton(self.centralwidget)
        self.fileTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileTab.setStyleSheet("font-size: 20px;\n"
        "border: 2px solid black;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);")
        self.fileTab.setObjectName("fileTab")

        self.recvMsg_1 = QtWidgets.QLabel(self.centralwidget)
        self.recvMsg_1.setStyleSheet("border: 2px solid black;\n"
        "border-radius: 5px;\n"
        "font-size: 18px;\n"
        "padding-left: 5;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 0, 127);\n"
        "background-color: rgb(255, 255, 127);")
        self.recvMsg_1.setObjectName("recvMsg_1")

        self.buttonObjs = []
        self.userComponents = [self.currentUser, self.msgInput, self.sendMsg, self.sentMsg_1, self.line_2, self.line_3, self.msgTab, self.fileTab, self.recvMsg_1]
        index = 0
        for clientID,clientOBJ in userDict.items():
            btnObj = ButtonComponent(self.centralwidget, index, clientOBJ, self.userComponents)
            self.buttonObjs.append(btnObj)
            index += 1

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_heading.setText(_translate("MainWindow", "WELCOME TO THE LOCAL DC++ PROJECT"))
        self.allUsers.setText(_translate("MainWindow", "Users Available Right Now"))
        self.currentUser.setText(_translate("MainWindow", "Please Select a User"))
