import string
import random
from PyQt5 import QtWidgets, QtGui, QtCore


class ChatInput(QtWidgets.QHBoxLayout):
    def __init__(self, parent,onClick_send):
        super(ChatInput, self).__init__()
        self.onClick_send = onClick_send
        self.parent = parent
        randomSTR = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=10))
        self.setObjectName(randomSTR + "_Hbox")

        self.lineEdit = QtWidgets.QLineEdit(self.parent)
        self.lineEdit.setStyleSheet(
            "padding: 10px 5px;\n"
            "font-size: 20px;"
        )
        self.lineEdit.setObjectName("lineEdit")
        self.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.parent)
        self.pushButton.setStyleSheet(
            "padding: 10px 5px;\n"
            "font-size: 20px;"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClick)
        self.addWidget(self.pushButton)
        self.setStretch(0, 10)
        self.setStretch(1, 1)

    def onClick(self):
        message = self.lineEdit.text()
        try:
            self.onClick_send(message)
            self.lineEdit.clear()
        except Exception as err:
            print(err)