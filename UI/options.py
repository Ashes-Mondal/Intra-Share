from http import client
from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonComponent:
    def __init__(self, centralwidget, index, clientOBJ, user_label_heading) -> None:
        self.user_label_heading = user_label_heading
        self.label = clientOBJ.username
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
        self.userButton.setText(_translate("MainWindow", self.label))
        self.userButton.clicked.connect(self.setCurrentUser)
    
    def setCurrentUser(self):
        self.user_label_heading.setText(self.label)
        self.user_label_heading.adjustSize()

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
        self.user_label_heading = QtWidgets.QLabel(self.centralwidget)
        self.user_label_heading.setGeometry(QtCore.QRect(490, 110, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.user_label_heading.setFont(font)
        self.user_label_heading.setStyleSheet("color: rgb(85, 0, 127)")
        self.user_label_heading.setObjectName("user_label_heading")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 90, 20, 731))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_heading_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_heading_4.setGeometry(QtCore.QRect(30, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_heading_4.setFont(font)
        self.label_heading_4.setStyleSheet("color: rgb(85, 0, 127)")
        self.label_heading_4.setObjectName("label_heading_4")

        self.buttonObjs = []
        index = 0
        for clientID,clientOBJ in userDict.items():
            btnObj = ButtonComponent(self.centralwidget, index, clientOBJ, self.user_label_heading)
            self.buttonObjs.append(btnObj)
            index += 1
        # for i in range(0, len(userlist)):
        #     btnObj = ButtonComponent(self.centralwidget, i, str(i + 1) + ". " + userlist[i]["username"], self.user_label_heading)
        #     self.buttonObjs.append(btnObj)

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
        self.user_label_heading.setText(_translate("MainWindow", "<Selected User>"))
        self.label_heading_4.setText(_translate("MainWindow", "Users Available Right Now"))
