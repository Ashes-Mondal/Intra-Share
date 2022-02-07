import time
# from threading import Thread
from PyQt5 import QtCore, QtWidgets, QtGui
from .UIComponents.MainHeading import MainHeading
from .UIComponents.MessageWindow import MessageWindow
from .UIComponents.GroupChat import GroupChat

class BtnThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal()
    def run(self):
        while True:
            print("BtnThread:\n")
            self.my_signal.emit()
            time.sleep(5)


# class BtnThread(QtCore.QThread):
#     def __init__(self, centralwidget, userDict, clientIns, userid) -> None:
#         super(BtnThread, self).__init__()
#         print("\nEntered BtnThread class")
#         self.centralwidget = centralwidget
#         self.userDict = userDict
#         self.clientIns = clientIns
#         self.userid = userid

#     def run(self):
#         while True:
#             self.buttonObjs = []
#             index = 0
#             # print("checking:\n")
#             try:
#                 time.sleep(0.02)
#                 for clientID, clientOBJ in self.userDict.items():
#                     if clientOBJ.online:
#                         print(index)
#                         btnObj = ButtonComponent(self.centralwidget, index, clientOBJ, clientID, self.clientIns, self.userid)
#                         self.buttonObjs.append(btnObj)
#                         index += 1
#             except Exception as err:
#                 print("ERROR: ", err)
#             time.sleep(5)


class ButtonComponent():
    def __init__(self, vbox, index, clientOBJ, clientID, clientIns, userid) -> None:
        # vbox.setObjectName("centralwidget")
        self.clientID = clientID
        self.clientIns = clientIns
        self.userid = userid
        self.userButton = QtWidgets.QPushButton()
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

        vbox.addWidget(self.userButton)
        print(clientID, clientOBJ.username)

    def setCurrentUser(self):
        self.user = MessageWindow(self.label, self.clientIns, self.clientID, self.userid)
        # self.user.msgInput.returnPressed.connect(self.sendMessageFunc)
        # self.user.sendMsgBtn.clicked.connect(self.sendMessageFunc)
        # try:
        #     self.__startSendingMessages(self.clientID)
        # except Exception as err:
        #     print(err)
        self.user.show()


class SetUI():
    def __init__(self, MainSelf) -> None:
        self.mainwindow = MainSelf

    def setupUi(self, widget, userid):
        self.mainwindow.setObjectName("MainWindow")
        self.mainwindow.setFixedWidth(1183)
        self.mainwindow.setFixedHeight(855)
        self.centralwidget = widget
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

class UserWindow(QtWidgets.QMainWindow):
    def __init__(self, clientIns, userid):
        super(UserWindow, self).__init__()
        self.userDict = clientIns.activeClients
        self.clientIns = clientIns
        self.userid = userid
        self.cur_index = 0
        self.buttonObjs = []

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        try:
            setUI = SetUI(self)
            setUI.setupUi(self.centralwidget, self.userid)

            self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)
            # v_widget = QtWidgets.QWidget()
            # v_widget.setLayout(self.vbox)
            # v_widget.setFixedWidth(855)
            # self.vbox.setGeometry(QtCore.QRect(30, 160, 341, 855))
            self.StartButtonEvent()

        except Exception as arr:
            print(arr)

        # Group chats ui
        self.grpChatUi = GroupChat(self.centralwidget)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle(self.userid)
        self.show()

    def StartButtonEvent(self):
        self.btnThrd = BtnThread()
        self.btnThrd.finished.connect(self.thread_finished)
        self.btnThrd.my_signal.connect(self.createBtns)
        self.btnThrd.start()

    # Create buttons in thread
    def createBtns(self):
        print(self.cur_index, ". createBtns:\n")
        self.cur_index += 1
        for btnObj in self.buttonObjs:
            self.vbox.removeWidget(btnObj.userButton)
        self.buttonObjs.clear()
        index = 0
        try:
            time.sleep(0.02)
            for clientID, clientOBJ in self.userDict.items():
                if clientOBJ.online:
                    btnObj = ButtonComponent(self.vbox, index, clientOBJ, clientID, self.clientIns, self.userid)
                    self.buttonObjs.append(btnObj)
                    index += 1
            print(self.buttonObjs)
        except Exception as err:
            print("ERROR: ", err)

    def thread_finished(self):
        print("finished\n")


    # def buttonThread(self):
    #     # app = QtCore.QCoreApplication([])
    #     btn_thread = BtnThread(self.centralwidget, self.userDict, self.clientIns, self.userid)
    #     print("\nEntered buttonThread3")
    #     # btn_thread.finished.connect(app.exit)
    #     btn_thread.start()




        # for clID, clOBJ in self.clientIns.activeClients.items():
        #     print("\n" + clOBJ.username + " " + str(clOBJ.online) + "\n")
        # self.buttonObjs = []
        # index = 0
        # try:
        #     time.sleep(0.02)
        #     for clientID, clientOBJ in self.userDict.items():
        #         if clientOBJ.online:
        #             print(index)
        #             btnObj = ButtonComponent(self.centralwidget, index, clientOBJ, clientID, self.clientIns, self.userid)
        #             self.buttonObjs.append(btnObj)
        #             index += 1
        # except Exception as err:
        #     print(err)


'''
self.setObjectName("MainWindow")
            self.setFixedWidth(1183)
            self.setFixedHeight(855)
            self.centralwidget = QtWidgets.QWidget(self)
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

            self.setCentralWidget(self.centralwidget)
            self.setWindowTitle(self.userid)
            self.show()
'''