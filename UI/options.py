from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonComponent:
    def __init__(self, centralwidget, buttonDimension, index, label, mainLabel, msgList) -> None:
        self.mainLabel = mainLabel
        self.msgList = msgList
        self.index = index
        self.button = QtWidgets.QPushButton(centralwidget)
        self.button.setGeometry(
            QtCore.QRect(buttonDimension[0], buttonDimension[1], buttonDimension[2], buttonDimension[3])
        )
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setObjectName("pushButton" + str(index))

        _translate = QtCore.QCoreApplication.translate
        self.button.setText(_translate("MainWindow", label))
        self.button.clicked.connect(self.sendMessage)
    
    def sendMessage(self):
        self.mainLabel.setText(self.msgList[self.index])
        self.mainLabel.adjustSize()

class Options_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(1183)
        MainWindow.setFixedHeight(855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 10, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.counter = 0
        self.msgList = ["Send Message Function initiated...", "Send File Function initiated...", "Exit Function initiated..."]
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 60, 391, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setUnderline(False)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setGeometry(QtCore.QRect(10, 220, 461, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setUnderline(False)
        self.mainLabel.setFont(font)
        self.mainLabel.setObjectName("mainLabel")

        self.buttonObjs = []
        labelList = ["Send a Message", "Send a File", "Exit"]
        self.msgList = ["Send Message Function initiated...", "Send File Function initiated...", "Exit Function initiated..."]
        for i in range(0, 3):
            buttonDimension = [10 + (i * 180), 130, 151, 41]
            btnObj = ButtonComponent(self.centralwidget, buttonDimension, i, labelList[i], self.mainLabel, self.msgList)
            self.buttonObjs.append(btnObj)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 26))
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
        self.label1.setText(_translate("MainWindow", "Local DC++ Project"))
        self.label2.setText(_translate("MainWindow", "Select any one option from the following:"))
        self.mainLabel.setText(_translate("MainWindow", "HI, WELCOME TO THE LOCAL DC++ PROJECT."))
