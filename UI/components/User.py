from PyQt5 import QtWidgets, QtGui, QtCore


class User(QtWidgets.QHBoxLayout):
    def __init__(self, clientOBJ, parent, msgCurrentUser,getFileListOfClient):
        super(User, self).__init__()
        self.clientOBJ = clientOBJ
        self.parent = parent
        self.msgCurrentUser = msgCurrentUser
        self.getFileListOfClient =  getFileListOfClient
        self.setObjectName("_Hbox" + clientOBJ.username)
        try:
            # username_label
            self.username_label = QtWidgets.QLabel(
                clientOBJ.username, self.parent)
            self.username_label.setStyleSheet(
                "text-align: left;\n"
                "padding-left: 10;\n"
                "padding-right: 10px;\n"
                "color: rgb(85, 0, 127);\n"
                "font: 75 11pt \"Verdana\";")
            self.username_label.setObjectName(clientOBJ.username)

            # msgPushButton
            self.msgPushButton = QtWidgets.QPushButton(self.parent)
            self.msgPushButton.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.msgPushButton.setStyleSheet(
                "QPushButton {\n"
                "font-size: 15px;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                "background-color: rgb(237, 237, 237);"
                "}\n"
                "QPushButton::hover {\n"
                "    border: 2px solid #ffffff;\n"
                "    background-color: #ffffff;\n"
                "}\n"
            )
            self.msgPushButton.setObjectName(
                "msgPushButton" + str(clientOBJ.clientID))
            self.msgPushButton.setIcon(QtGui.QIcon('images/chat.png'))
            self.msgPushButton.setIconSize(QtCore.QSize(32, 32))
            self.msgPushButton.clicked.connect(self.callCurrUser)

            # filePushButton
            self.filePushButton = QtWidgets.QPushButton(self.parent)
            self.filePushButton.setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.filePushButton.setStyleSheet(
                "QPushButton {\n"
                "font-size: 15px;\n"
                "border-radius: 20px;\n"
                "padding: 4;\n"
                "background-color: rgb(237, 237, 237);"
                "}\n"
                "QPushButton::hover {\n"
                "    border: 2px solid #f5f0bc;\n"
                "    background-color: #f5f0bc;\n"
                "}\n"
            )
            self.filePushButton.setObjectName(
                "filePushButton" + str(clientOBJ.clientID))
            self.filePushButton.setIcon(
                QtGui.QIcon('images/shared-folder.png'))
            self.filePushButton.setIconSize(QtCore.QSize(32, 32))
            self.filePushButton.clicked.connect(self.getClientFiles)

            # addwidgets
            self.addWidget(self.username_label)
            self.addWidget(self.msgPushButton)
            self.addWidget(self.filePushButton)

            # setting stretch
            self.setStretch(0, 5)
            self.setStretch(1, 1)
            self.setStretch(2, 1)
        except Exception as err:
            print(err)

    def callCurrUser(self):
        try:
            self.msgCurrentUser(self.clientOBJ)
        except Exception as err:
            print(err)

    def getClientFiles(self):
        try:
            self.getFileListOfClient(self.clientOBJ.clientID)
        except Exception as err:
            print(err)
