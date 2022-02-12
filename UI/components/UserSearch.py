from PyQt5 import QtWidgets, QtGui, QtCore


class UserSearch(QtWidgets.QHBoxLayout):
    def __init__(self, parent, setSearchMode, searchUsers, displayOnlineUsers):
        super(UserSearch, self).__init__()
        self.parent = parent
        self.setSearchMode = setSearchMode
        self.searchUsers = searchUsers
        self.displayOnlineUsers = displayOnlineUsers
        self.setObjectName("file_search" + "_Hbox")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.parent)
        self.lineEdit_2.setStyleSheet(
            "text-align: left;\n"
            "padding: 4;\n"
            "padding-left: 10;\n"
            "border: 2px solid black;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"MS Sans Serif\";"
        )
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_1 = QtWidgets.QPushButton(self.parent)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setIcon(QtGui.QIcon('images/clear1.png'))
        self.pushButton_1.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_1.setStyleSheet(
            "QPushButton {\n"
            "border:none;\n"
            "padding: 4;\n"
            "padding-left: 7;\n"
            "padding-right: 7;\n"
            "}\n"
        )
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.clearSearch)

        self.pushButton_2 = QtWidgets.QPushButton(self.parent)
        self.pushButton_2.clicked.connect(self.searchForUsers)
        self.pushButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(
            "padding: 4;\n"
            "padding-left: 10;\n"
            "padding-right: 10;\n"
            "margin-left: 5;\n"
            "color: rgb(85, 0, 127);\n"
            "background-color: rgb(255, 255, 127);\n"
            "text-align: left;\n"
            "border: 2px solid black;\n"
            "border-radius: 10px;\n"
            "font: 75 11pt \"MS Sans Serif\";"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.addWidget(self.lineEdit_2)
        self.addWidget(self.pushButton_1)
        self.addWidget(self.pushButton_2)
        self.setSpacing(0)

    def clearSearch(self):
        self.lineEdit_2.clear()
        self.setSearchMode(False)
        self.displayOnlineUsers()

    def searchForUsers(self):
        text = self.lineEdit_2.text()
        self.searchUsers(text)
