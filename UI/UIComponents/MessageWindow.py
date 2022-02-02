from PyQt5 import QtCore, QtGui, QtWidgets

class MessageWindow():
    def __init__(self, centralwidget, label) -> None:
        self.centralwidget = centralwidget
        self.label = label
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_heading.setText(_translate("MainWindow", "WELCOME TO THE LOCAL DC++ PROJECT"))
        self.msgInput.setPlaceholderText(_translate("MainWindow", "Type a message"))
        self.currentUser.setText(_translate("MainWindow", self.label))
        self.sendMsgBtn.setText(_translate("MainWindow", "SEND"))

# from PyQt5 import QtCore, QtWidgets, QtGui

# class AppendMessage():
#     def __init__(self, centralwidget, index, message) -> None:
#         self.centralwidget = centralwidget
#         self.sentMsg = QtWidgets.QLabel(self.centralwidget)
#         self.sentMsg.setGeometry(QtCore.QRect(420, 160 + (index * 60), 151, 51))
#         self.sentMsg.setStyleSheet("border: 2px solid black;\n"
#         "border-radius: 5px;\n"
#         "font-size: 18px;\n"
#         "padding-left: 5;\n"
#         "padding-right: 10;\n"
#         "color: rgb(85, 0, 127);\n"
#         "background-color: rgb(85, 255, 255);")
#         self.sentMsg.setObjectName("sentMsg_" + str(index))

#         _translate = QtCore.QCoreApplication.translate
#         self.sentMsg.setText(_translate("MainWindow", message))
#         self.sentMsg.adjustSize()

# class MessageWindow():
#     def __init__(self, centralwidget, label) -> None:
#         self.centralwidget = centralwidget
#         self.label = label
#         self.currentUser = QtWidgets.QPushButton(self.centralwidget)
#         self.currentUser.setGeometry(QtCore.QRect(400, 100, 481, 51))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.currentUser.setFont(font)
#         self.currentUser.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#         self.currentUser.setStyleSheet("text-align: left;\n"
#         "padding-left: 20px;\n"
#         "padding-right: 10px;\n"
#         "border-top: 2px solid black;\n"
#         "border-bottom: 2px solid black;\n"
#         "color: rgb(85, 0, 127);")
#         self.currentUser.setObjectName("currentUser")

#         self.msgInput = QtWidgets.QLineEdit(self.centralwidget)
#         self.msgInput.setStyleSheet("border: 2px solid black;\n"
#         "border-radius: 10px;\n"
#         "font-size: 20px;\n"
#         "padding-left: 10;\n"
#         "padding-right: 10;\n"
#         "color: rgb(85, 0, 127);\n"
#         "background-color: rgb(85, 255, 255);")
#         self.msgInput.setObjectName("msgInput")

#         self.sentMsg_1 = QtWidgets.QLabel(self.centralwidget)
#         self.sentMsg_1.setStyleSheet("border: 2px solid black;\n"
#         "border-radius: 5px;\n"
#         "font-size: 18px;\n"
#         "padding-left: 5;\n"
#         "padding-right: 10;\n"
#         "color: rgb(85, 0, 127);\n"
#         "background-color: rgb(85, 255, 255);")
#         self.sentMsg_1.setObjectName("sentMsg_1")

#         self.line_2 = QtWidgets.QFrame(self.centralwidget)
#         self.line_2.setGeometry(QtCore.QRect(400, 100, 781, 3))
#         self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_2.setObjectName("line_2")

#         self.line_3 = QtWidgets.QFrame(self.centralwidget)
#         self.line_3.setGeometry(QtCore.QRect(400, 150, 781, 3))
#         self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_3.setObjectName("line_3")

#         self.msgTab = QtWidgets.QPushButton(self.centralwidget)
#         self.msgTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.msgTab.setStyleSheet("font-size: 20px;\n"
#         "border: 2px solid black;\n"
#         "padding-left: 10;\n"
#         "padding-right: 10;\n"
#         "color: rgb(85, 0, 127);\n"
#         "background-color: rgb(255, 255, 127);")
#         self.msgTab.setObjectName("msgTab")

#         self.recvMsg_1 = QtWidgets.QLabel(self.centralwidget)
#         self.recvMsg_1.setStyleSheet("border: 2px solid black;\n"
#         "border-radius: 5px;\n"
#         "font-size: 18px;\n"
#         "padding-left: 5;\n"
#         "padding-right: 10;\n"
#         "color: rgb(85, 0, 127);\n"
#         "background-color: rgb(255, 255, 127);")
#         self.recvMsg_1.setObjectName("recvMsg_1")

#         self.sendMsgBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
#         self.sendMsgBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.sendMsgBtn.setStyleSheet("border: 3px solid rgb(85, 0, 127);\n"
#         "border-radius: 10px;\n"
#         "color: rgb(255, 255, 127);\n"
#         "background-color: rgb(255, 255, 127);")
#         self.sendMsgBtn.setObjectName("sendMsgBtn")

#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
#         self.textBrowser.setHtml(
#             """<body>
#             <h1>Key</h1>
#             <div style='color:red;'>
#             GREEN = Overall Progress is 80% or above
#             YELLOW = Overall Progress between 65%-79%
#             Orange = Overall Progress is 64% or below
#             </div>
#             </body>"""
#         )
#         self.textBrowser.setObjectName("textBrowser")

#         self.retranslateUi()

#     def retranslateUi(self):
#         self.msgInput.setGeometry(QtCore.QRect(420, 720, 671, 61))
#         self.sendMsgBtn.setGeometry(QtCore.QRect(1110, 730, 51, 41))
#         self.msgTab.setGeometry(QtCore.QRect(880, 100, 151, 51))
#         self.sentMsg_1.setGeometry(QtCore.QRect(420, 160, 151, 51))
#         self.recvMsg_1.setGeometry(QtCore.QRect(420, 220, 271, 51))

#         _translate = QtCore.QCoreApplication.translate
#         self.currentUser.setText(_translate("MainWindow", "Please Select a User"))
#         self.currentUser.setText(_translate("MainWindow", self.label))
#         self.msgTab.setText(_translate("MainWindow", "Send Message"))
#         self.msgInput.setPlaceholderText(_translate("MainWindow", "Type a message"))
#         self.sendMsgBtn.setText(_translate("MainWindow", "CommandLinkButton"))
#         self.sentMsg_1.setText(_translate("MainWindow", "Message Sent"))
#         self.recvMsg_1.setText(_translate("MainWindow", "Message Received"))
