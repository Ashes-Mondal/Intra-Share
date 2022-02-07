from PyQt5 import QtCore, QtGui, QtWidgets
from .options import Options_MainWindow
from .userWindow import UserWindow
from .UIComponents.MainHeading import MainHeading

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
        # self.MainWindow = QtWidgets.QMainWindow()
    
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()
    
    def startUI(self):
        self.setObjectName("MainWindow")
        self.setFixedWidth(1183)
        self.setFixedHeight(855)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(430, 470, 371, 32))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.submit_button.setFont(font)
        self.submit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submit_button.setStyleSheet("QPushButton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton::hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton::pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.submit_button.setObjectName("submit_button")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(430, 220, 371, 41))
        self.password_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.label_ip = QtWidgets.QLabel(self.centralwidget)
        self.label_ip.setGeometry(QtCore.QRect(310, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(430, 280, 371, 41))
        self.ip_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;")
        self.ip_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ip_input.setObjectName("ip_input")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(300, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        self.label_heading = MainHeading(self.centralwidget)

        self.label_uid = QtWidgets.QLabel(self.centralwidget)
        self.label_uid.setGeometry(QtCore.QRect(330, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_uid.setFont(font)
        self.label_uid.setObjectName("label_uid")
        self.uid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.uid_input.setGeometry(QtCore.QRect(430, 160, 371, 41))
        self.uid_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;")
        self.uid_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uid_input.setObjectName("uid_input")
        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setGeometry(QtCore.QRect(430, 340, 371, 41))
        self.port_input.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;")
        self.port_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.port_input.setObjectName("port_input")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(360, 340, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(300, 110, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("QLabel {\n"
        "    color: rgb(255, 0, 0)\n"
        "}")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.password_input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input_2.setGeometry(QtCore.QRect(430, 400, 371, 41))
        self.password_input_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
        "border:none;\n"
        "border-left:2px dashed rgba(105, 118, 132, 255);\n"
        "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
        "padding:10px;")
        self.password_input_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input_2.setObjectName("password_input_2")
        self.label_password_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_password_2.setGeometry(QtCore.QRect(230, 400, 191, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.label_password_2.setFont(font)
        self.label_password_2.setObjectName("label_password_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT"))
        self.submit_button.clicked.connect(self.validateCredentials)
        
        self.label_uid.setText(_translate("MainWindow", "UserID*"))
        self.uid_input.setPlaceholderText(_translate("MainWindow", "Enter User ID"))
        
        self.label_password.setText(_translate("MainWindow", "Password*"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        
        self.label_ip.setText(_translate("MainWindow", "Server IP*"))
        self.ip_input.setPlaceholderText(_translate("MainWindow", "Server IP"))
        
        self.label_port.setText(_translate("MainWindow", "Port*"))
        self.port_input.setPlaceholderText(_translate("MainWindow", "Port Number"))
        
        self.password_input_2.setPlaceholderText(_translate("MainWindow", "Enter Server Password"))
        self.label_password_2.setText(_translate("MainWindow", "Server Password"))
        self.label_error.setText(_translate("MainWindow", ""))

    def validateCredentials(self):
        # userid = "Agni"
        # password = "password"
        # serverip = "192.168.43.244"
        # port = 9999
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
                self.hide()
                self.ui = UserWindow(self.clientIns, userid)
                self.ui.setupUi()
        except Exception as error:
            self.submit_button.setEnabled(True)
            if str(error) == "timed out":
                self.label_error.setText("Server couldn't be reached!")
                self.label_error.adjustSize()
            else:
                self.label_error.setText(str(error))
            self.label_error.adjustSize()
