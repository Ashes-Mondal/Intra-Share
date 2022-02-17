from PyQt5 import QtCore, QtGui, QtWidgets
from .MainWindow import MainWindow

def validateIP(serverip):
    dotIndex = []
    for i in range(0, len(serverip)):
        if serverip[i] == '.':
            dotIndex.append(i)
        elif serverip[i] > '9' or serverip[i] < '0':
            return False
    
    if len(dotIndex) != 3:
        return False    
    for i in range(0, 3):
        if serverip[dotIndex[i] - 1] == '.' or serverip[dotIndex[i] + 1] == '.':
            return False    
    return True


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, clientIns) -> None:
        super(Ui_MainWindow, self).__init__()
        self.clientIns = clientIns
    
    def startUI(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(948, 826)
        self.setWindowIcon(QtGui.QIcon('images/logo.svg'))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontallLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontallLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontallLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontallLayout_2.setObjectName("horizontallLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallLayout_2.addItem(spacerItem)
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_heading.setStyleSheet("border: 2px solid red;\n"
        "font: 75 17pt \"MS Sans Serif\";\n"
        "border-radius: 10px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "margin: 20px 0px;\n"
        "color: rgb(85, 255, 255);\n"
        "background-color: rgb(85, 0, 127);")
        self.label_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_heading.setWordWrap(False)
        self.label_heading.setObjectName("label_heading")
        self.horizontallLayout_2.addWidget(self.label_heading)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallLayout_2.addItem(spacerItem1)
        self.horizontallLayout_2.setStretch(0, 1)
        self.horizontallLayout_2.setStretch(1, 2)
        self.horizontallLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontallLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_uid = QtWidgets.QLabel(self.centralwidget)
        self.label_uid.setStyleSheet("padding: 10px;\n"
        "padding-right: 0px;\n"
        "font: 14pt \"Sylfaen\";\n"
        "color: rgb(85, 0, 127);")
        self.label_uid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_uid.setObjectName("label_uid")
        self.horizontalLayout_8.addWidget(self.label_uid)
        self.uid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.uid_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;\n"
        "margin-right: 70px;\n"
        "font: 12pt \"Sylfaen\";")
        self.uid_input.setObjectName("uid_input")
        self.horizontalLayout_8.addWidget(self.uid_input)
        self.horizontalLayout_8.setStretch(0, 4)
        self.horizontalLayout_8.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setStyleSheet("padding: 10px;\n"
        "padding-right: 0px;\n"
        "font: 14pt \"Sylfaen\";\n"
        "color: rgb(85, 0, 127);")
        self.label_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_7.addWidget(self.label_password)
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;\n"
        "margin-right: 70px;\n"
        "font: 12pt \"Sylfaen\";")
        self.password_input.setObjectName("password_input")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_7.addWidget(self.password_input)
        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_ip.setStyleSheet("padding: 10px;\n"
        "padding-right: 0px;\n"
        "font: 14pt \"Sylfaen\";\n"
        "color: rgb(85, 0, 127);")
        self.label_ip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout_6.addWidget(self.label_ip)
        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;\n"
        "margin-right: 70px;\n"
        "font: 12pt \"Sylfaen\";")
        self.ip_input.setObjectName("ip_input")
        self.horizontalLayout_6.addWidget(self.ip_input)
        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setStyleSheet("padding: 10px;\n"
        "padding-right: 0px;\n"
        "font: 14pt \"Sylfaen\";\n"
        "color: rgb(85, 0, 127);")
        self.label_port.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_4.addWidget(self.label_port)
        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;\n"
        "margin-right: 70px;\n"
        "font: 12pt \"Sylfaen\";")
        self.port_input.setText("")
        self.port_input.setObjectName("port_input")
        self.horizontalLayout_4.addWidget(self.port_input)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_password_2.setStyleSheet("padding: 10px;\n"
        "padding-right: 0px;\n"
        "font: 14pt \"Sylfaen\";\n"
        "color: rgb(85, 0, 127);")
        self.label_password_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password_2.setObjectName("label_password_2")
        self.horizontalLayout_2.addWidget(self.label_password_2)
        self.password_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;\n"
        "margin-right: 70px;\n"
        "font: 12pt \"Sylfaen\";")
        self.password_input_2.setObjectName("password_input_2")
        self.password_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.password_input_2)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_null = QtWidgets.QLabel(self.centralwidget)
        self.label_null.setText("")
        self.label_null.setObjectName("label_null")
        self.horizontalLayout_3.addWidget(self.label_null)
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setStyleSheet("QPushButton {\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "color:rgba(255, 255, 255, 210);\n"
        "border-radius:5px;\n"
        "padding: 10px;\n"
        "margin: 20px 70px 0 0;\n"
        "font: 14pt \"Sylfaen\";\n"
        "font-size: 22px\n"
        "}\n"
        "QPushButton::hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
        "}\n"
        "QPushButton::pressed {\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105, 118, 132, 200);\n"
        "}")
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout_3.addWidget(self.submit_button)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setStyleSheet("color: red;\n"
        "margin-top: 15px;\n"
        "font: 75 10pt \"Myanmar Text\";")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setWordWrap(True)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_5.addWidget(self.label_error)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 12)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Login"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.submit_button.clicked.connect(self.validateCredentials)
        
        self.label_heading.setText(_translate("MainWindow", "WELCOME TO 🦈 INTRA-SHARE 🦈"))
        self.label_uid.setText(_translate("MainWindow", "USER ID*"))
        self.uid_input.setPlaceholderText(_translate("MainWindow", "Enter your User Id"))
        self.label_password.setText(_translate("MainWindow", "PASSWORD*"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.label_ip.setText(_translate("MainWindow", "SERVER IP*"))
        self.ip_input.setPlaceholderText(_translate("MainWindow", "Enter Server IP"))
        self.label_port.setText(_translate("MainWindow", "PORT*"))
        self.port_input.setPlaceholderText(_translate("MainWindow", "Enter Port Number"))
        self.label_password_2.setText(_translate("MainWindow", "SERVER PASSWORD"))
        self.password_input_2.setPlaceholderText(_translate("MainWindow", "Enter Server Password"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.label_error.setText(_translate("MainWindow", ""))

        # self.port_input.setText(_translate("MainWindow", "9999"))
        # self.password_input.setText(_translate("MainWindow", "password"))
        # self.ip_input.setText(_translate("MainWindow", "192.168.xx.xx"))
        # self.password_input_2.setText(_translate("MainWindow", "qwerty"))
        
    def validateCredentials(self):
        
        userid = self.uid_input.text()
        password = self.password_input.text()
        serverip = self.ip_input.text()
        port = self.port_input.text()
        serverPassword = self.password_input_2.text()
        
        try:
            allValid = True
            errstr = ""
            # validate server ip
            allValid = validateIP(serverip)
            if not allValid:
                errstr = "Invalid IP entered"
            # validate port number
            try:
                port = int(port)
                if port < 1 or port > 65535:
                    errstr = "Invalid Port Number, should be an integer b/w 1 - 65535"
                    allValid = False
            except:
                errstr = "Invalid Port Number, should be an integer b/w 1 - 65535"
                allValid = False
            # check empty fields
            if len(userid) == 0 or len(password) == 0 or len(serverip) == 0:
                errstr = "Please fill up the required fields"
                allValid = False
            self.label_error.setText(errstr)
            self.label_error.adjustSize()
            if allValid:
                credentials = {"username": userid, "password": password}
                self.submit_button.setEnabled(False)
                self.clientIns.startClient(
                    server_addr = (serverip, port),
                    server_password=serverPassword,
                    clientCredentials=credentials
                )
                # move to main application file
                self.mainApp = MainWindow(self,self.clientIns)
                self.mainApp.setupUi()
                self.mainApp.show()
                self.hide()
                self.submit_button.setEnabled(True)
        except Exception as error:
            self.submit_button.setEnabled(True)
            if str(error) == "timed out":
                self.label_error.setText("Server couldn't be reached!")
                self.label_error.adjustSize()
            else:
                self.label_error.setText(str(error))
            self.label_error.adjustSize()
