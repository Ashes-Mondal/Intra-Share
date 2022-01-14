from PyQt5 import QtCore, QtGui, QtWidgets
from functionality import Functionalities

class Ui_MainWindow(Functionalities):
    def __init__(self, clientIns) -> None:
        super().__init__(clientIns)
        self.MainWindow = QtWidgets.QMainWindow()
    
    def startUI(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedWidth(1183)
        self.MainWindow.setFixedHeight(855)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(410, 380, 371, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.submit_button.setFont(font)
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submit_button.setStyleSheet("QPushButton {\n"
        "    background-color : lightblue;\n"
        "}\n"
        "QPushButton::pressed {\n"
        "    background-color : red;\n"
        "}")
        self.submit_button.setObjectName("submit_button")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(410, 180, 371, 41))
        self.password_input.setStyleSheet("QLineEdit {\n"
        "    padding-left: 10\n"
        "}")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.label_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_ip.setGeometry(QtCore.QRect(290, 240, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(410, 240, 371, 41))
        self.ip_input.setStyleSheet("QLineEdit {\n"
        "    padding-left: 10\n"
        "}")
        self.ip_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ip_input.setObjectName("ip_input")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(290, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(290, 40, 601, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")
        self.label_uid = QtWidgets.QLabel(self.centralwidget)
        self.label_uid.setGeometry(QtCore.QRect(310, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_uid.setFont(font)
        self.label_uid.setObjectName("label_uid")
        self.uid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.uid_input.setGeometry(QtCore.QRect(410, 120, 371, 41))
        self.uid_input.setStyleSheet("QLineEdit {\n"
        "    padding-left: 10\n"
        "}")
        self.uid_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uid_input.setObjectName("uid_input")
        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setGeometry(QtCore.QRect(410, 300, 371, 41))
        self.port_input.setStyleSheet("QLineEdit {\n"
        "    padding-left: 10\n"
        "}")
        self.port_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.port_input.setObjectName("port_input")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(340, 300, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 26))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.submit_button.clicked.connect(self.validateCredentials)
        self.submit_button.clicked.connect(self.validateCredentials)
        self.password_input.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.label_ip.setText(_translate("MainWindow", "Server IP:"))
        self.ip_input.setPlaceholderText(_translate("MainWindow", "Server IP"))
        self.label_password.setText(_translate("MainWindow", "Password:"))
        self.label_heading.setText(_translate("MainWindow", "WELCOME TO THE LOCAL DC++ PROJECT"))
        self.label_uid.setText(_translate("MainWindow", "User ID:"))
        self.uid_input.setPlaceholderText(_translate("MainWindow", "Enter User ID"))
        self.port_input.setPlaceholderText(_translate("MainWindow", "Port Number"))
        self.label_port.setText(_translate("MainWindow", "Port:"))

    def validateCredentials(self):
        #TXTBOX
        # self.uid_input.text(),
        # self.password_input.text(),
        # self.ip_input.text(),
        # self.port_input.text()
        try:
            self.handleSubmit(self.uid_input.text(),
            self.password_input.text(),
            self.ip_input.text(),
            self.port_input.text())
        except Exception as e:
            print("ERROR ", str(e)) #TXTBOX
